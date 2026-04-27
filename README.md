# 🌌 NexusArt

**Gerador de Lore e Concept Art para RPGs com Memória Semântica e Context Automation**

O **NexusArt** é uma aplicação completa (Full-Stack AI) que orquestra modelos do Google Gemini para gerar biografias ricas e artes conceituais de alta fidelidade para personagens de RPG em paralelo, entregando resultados em menos de 15 segundos.

Além da geração, o projeto inclui uma **Memória Vetorial** (via Supabase pgvector) que permite buscar personagens anteriores utilizando similaridade semântica (linguagem natural).

---

## 🚀 Funcionalidades

- 🎭 **Lore Engine**: Geração de histórias de fundo detalhadas usando `Gemini 2.5 Flash` e `Structured Output` (Pydantic).
- 🎨 **Art Engine**: Criação visual usando o motor de imagens mais avançado do Google (**Imagen 4.0** via `google-genai`), suportando múltiplos estilos artísticos.
- ⚡ **Orquestração Assíncrona**: O texto e a imagem são gerados simultaneamente usando `asyncio` e `ThreadPoolExecutor`.
- 🧠 **Busca Semântica**: Histórico salvo no **Supabase** com vetores de alta precisão (**gemini-embedding-2**).
- 🛡️ **Context Automation**: Integração com **Context7 MCP** para garantir que o código utilize sempre as documentações e APIs mais atualizadas das bibliotecas.
- 🖥️ **Interface Premium**: Dashboard interativo e responsivo construído com **Streamlit**.

## 🛠️ Stack Tecnológica

- **Linguagem**: Python 3.10+ (Homologado no Python 3.14)
- **Modelos de IA**: 
    - Orquestração: `Gemini 2.5 Flash`
    - Imagem: `Imagen 4.0` (`imagen-4.0-generate-001`)
    - Vetores: `gemini-embedding-2` (Configurado para 768-d)
- **Frameworks de IA**: LangChain, Google GenAI SDK (`google-genai`), Context7
- **Banco de Dados**: Supabase (PostgreSQL + pgvector)
- **Frontend**: Streamlit
- **Monitoramento de custos API de imagem**: LangSmith

## 📖 Arquitetura e Clean Code

Este projeto segue rigorosos padrões de **Clean Code** e **Spec-Driven Development (SDD)**. Toda a lógica de IA é isolada da interface, permitindo fácil migração de modelos e manutenção. 
👉 **[Guia Técnico Arquitetural](docs/TECHNICAL_GUIDE.md)** | **[Log de Debugging e Migração](docs/GOOGLE_GENAI_DEBUG_LOG.md)**.

---

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos

- Python 3.10+
- Uma conta no [Google AI Studio](https://aistudio.google.com/) (para a chave da API).
- Uma conta no [Supabase](https://supabase.com/) (para o banco vetorial).

### 2. Configuração do Banco de Dados (Supabase)

Execute o script SQL em `src/database_setup.sql` no painel SQL Editor do seu projeto Supabase para criar a tabela `characters` e habilitar o `pgvector`.

### 3. Instalação

```bash
git clone https://github.com/Projetos-AI-Design-JB/Lore-Generator-NexusArt
cd Lore-Generator-NexusArt
pip install -r requirements.txt
```

### 4. Variáveis de Ambiente

Crie o arquivo `.env` na raiz do projeto (UTF-8 sem BOM):

```env
GOOGLE_API_KEY="sua_chave_do_gemini"
SUPABASE_URL="sua_url_do_supabase"
SUPABASE_KEY="sua_chave_anon_do_supabase"

# Opcional (Para monitoramento)
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="sua_chave_langsmith"
```

### 5. Rodando a Aplicação

```bash
python -m streamlit run app.py
```

---
*Desenvolvido com Engenharia de Contexto Avançada e fluxo GSD. 
[arquivos GSD:](/.planning)*
