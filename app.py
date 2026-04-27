import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_core")
warnings.filterwarnings("ignore", category=FutureWarning, module="google.generativeai")

import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env

from src.orchestrator import NexusOrchestrator
from src.memory_engine import MemoryEngine
from src.search_engine import SemanticSearchEngine
import json

# 1. Configuração da Página (Clean Code: Centralização de Setup)
st.set_page_config(
    page_title="NexusArt - Lore & Concept",
    page_icon="🌌",
    layout="wide"
)

# 2. Inicialização de Estado e Dependências
# Instanciamos os motores apenas uma vez por sessão usando cache_resource se possível,
# mas para simplicidade manteremos no session_state.
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = NexusOrchestrator()
if "memory_engine" not in st.session_state:
    st.session_state.memory_engine = MemoryEngine()
if "search_engine" not in st.session_state:
    st.session_state.search_engine = SemanticSearchEngine()

st.title("🌌 NexusArt")
st.markdown("Gerador de Lore e Concept Art alimentado por IA e Memória Semântica.")

# 3. Interface de Abas (Tabs)
tab_forge, tab_library = st.tabs(["⚒️ Forja (Gerador)", "📚 Biblioteca (Busca)"])

# ==========================================
# ABA 1: FORJA (Geração)
# ==========================================
with tab_forge:
    st.header("Crie um Novo Personagem")
    
    with st.form("forge_form"):
        desc_input = st.text_area(
            "Descrição do Personagem",
            placeholder="Ex: Uma ladina tiefling que usa magias de sombra e adagas envenenadas."
        )
        
        # Array de Estilos
        available_styles = ["Dark Fantasy", "Cyberpunk", "Watercolor", "Oil Painting", "Sketch"]
        selected_styles = st.multiselect("Estilos Artísticos", available_styles, default=["Dark Fantasy"])
        
        submit_button = st.form_submit_button("Gerar Personagem")
        
    if submit_button and desc_input:
        with st.spinner("Forjando lore e arte... (aguarde até 15s)"):
            try:
                # 4. Orquestração Assíncrona
                # O Streamlit é síncrono, então criamos um loop assíncrono para nossa função principal
                orchestrator = st.session_state.orchestrator
                char_lore, art_path = asyncio.run(orchestrator.generate_character_full(desc_input, selected_styles))
                
                # 5. Armazenamento (Memória)
                memory = st.session_state.memory_engine
                memory.save_character(char_lore, art_path)
                
                # 6. Exibição de Resultados (Clean Code: Divisão Visual)
                st.success("Personagem gerado e salvo com sucesso!")
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    if art_path:
                        st.image(art_path, caption=char_lore.name, use_container_width=True)
                    else:
                        st.warning("A imagem não pôde ser gerada.")
                        
                with col2:
                    st.subheader(f"{char_lore.name} - O {char_lore.character_class} {char_lore.race}")
                    st.markdown("### Personalidade")
                    st.write(", ".join(char_lore.personality_traits))
                    st.markdown("### Habilidades")
                    st.write(", ".join(char_lore.abilities))
                    st.markdown("### Biografia")
                    st.write(char_lore.biography)
                    
            except Exception as e:
                st.error(f"Erro ao gerar personagem: {e}")

# ==========================================
# ABA 2: BIBLIOTECA (Busca Semântica)
# ==========================================
with tab_library:
    st.header("Consulte o Histórico")
    
    search_query = st.text_input("O que você procura?", placeholder="Ex: Guerreiros de armadura pesada")
    search_button = st.button("Buscar")
    
    if search_button and search_query:
        with st.spinner("Consultando oráculos..."):
            searcher = st.session_state.search_engine
            results = searcher.search_characters(search_query)
            
            if results:
                st.success(f"Encontrado {len(results)} personagem(ns) similar(es).")
                for res in results:
                    # Clean Code: Isolamento da renderização de resultados
                    with st.expander(f"{res.get('name')} (Similaridade: {res.get('similarity', 0):.2f})"):
                        cols = st.columns([1, 3])
                        
                        # Exibição da Imagem (se existir localmente)
                        img_path = res.get('image_url')
                        if img_path and os.path.exists(img_path):
                            cols[0].image(img_path, use_container_width=True)
                        else:
                            cols[0].write("🖼️ Imagem não encontrada.")
                            
                        # Deserialização da Lore JSON
                        try:
                            lore_dict = json.loads(res.get('lore', '{}'))
                            cols[1].write(lore_dict.get('biography', 'Lore indisponível.'))
                        except:
                            cols[1].write(res.get('lore'))
            else:
                st.info("Nenhum personagem correspondente encontrado.")
