import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from supabase import create_client, Client
from google import genai
from google.genai import types

load_dotenv()

class SemanticSearchEngine:
    """
    Motor de Busca Semântica do NexusArt.
    Clean Code: Responsabilidade única focada em recuperar dados via busca vetorial (Retrieval).
    """

    def __init__(self):
        self._initialize_infrastructure()

    def _initialize_infrastructure(self):
        """Inicializa as conexões necessárias (Supabase e Gemini Embeddings)."""
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        self.db: Client = create_client(supabase_url, supabase_key)
        self.client = genai.Client()

    def search_characters(self, query: str, match_limit: int = 5) -> List[Dict[str, Any]]:
        """
        Realiza a busca semântica por personagens similares à query fornecida.
        """
        print(f"🔍 Iniciando busca semântica por: '{query}'")
        
        query_embedding = self._generate_query_embedding(query)
        search_results = self._execute_vector_search(query_embedding, match_limit)
        
        return search_results

    def _generate_query_embedding(self, text: str) -> List[float]:
        """Converte a consulta de texto do usuário em um vetor de 768 dimensões."""
        try:
            result = self.client.models.embed_content(
                model="gemini-embedding-2",
                contents=text,
                config=types.EmbedContentConfig(
                    task_type="RETRIEVAL_QUERY", # Otimizado para queries de busca
                    output_dimensionality=768
                )
            )
            return result.embeddings[0].values
        except Exception as error:
            print(f"❌ Erro ao gerar vetor de busca: {error}")
            return []

    def _execute_vector_search(self, embedding_vector: List[float], limit: int) -> List[Dict[str, Any]]:
        """
        Invoca a Remote Procedure Call (RPC) no Supabase para calcular a distância coseno.
        """
        if not embedding_vector:
            return []

        try:
            # Invoca a função 'match_characters' que criamos na Fase 2 no Supabase
            response = self.db.rpc(
                "match_characters", 
                {"query_embedding": embedding_vector, "match_threshold": 0.5, "match_count": limit}
            ).execute()
            
            return response.data
        except Exception as error:
            print(f"❌ Erro na consulta vetorial ao Supabase: {error}")
            return []

if __name__ == "__main__":
    # Teste rápido
    searcher = SemanticSearchEngine()
    results = searcher.search_characters("Guerreiro elfo das sombras")
    
    if results:
        print(f"\n✅ {len(results)} personagem(ns) encontrado(s):")
        for res in results:
            print(f"- Nome: {res.get('name')} (Similaridade: {res.get('similarity'):.2f})")
    else:
        print("\nNenhum resultado encontrado ou ocorreu um erro.")
