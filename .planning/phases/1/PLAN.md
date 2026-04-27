# PLAN: Fase 1 - Fundação e Infraestrutura

## Objetivo
Configurar o ambiente de desenvolvimento Python, a estrutura de pastas do projeto NexusArt e os arquivos de configuração necessários para segurança e dependências.

## Deliverables
- [ ] Ambiente Virtual Python (`.venv`).
- [ ] Arquivo `requirements.txt` com dependências iniciais (Streamlit, LangChain, Supabase, Python-dotenv).
- [ ] Arquivo `.env.example` para segurança de chaves.
- [ ] Estrutura de diretórios `src/` inicial.

## User Acceptance Criteria (UAT)
- [ ] O comando `python --version` deve retornar 3.10 ou superior.
- [ ] As dependências devem ser instaláveis via `pip install -r requirements.txt`.
- [ ] O arquivo `.env` não deve ser rastreado pelo Git (verificar `.gitignore`).

## Passo a Passo

### 1. Ambiente Python
- Criar venv em `NexusArt/.venv`.
- Ativar venv e atualizar pip.

### 2. Dependências
- Criar `NexusArt/requirements.txt`:
  ```text
  streamlit
  langchain
  langchain-google-genai
  supabase
  python-dotenv
  langsmith
  pydantic
  fal-client
  ```

### 3. Estrutura e Segurança
- Criar `NexusArt/.env.example` com placeholders.
- Garantir que `NexusArt/.gitignore` inclua `.venv`, `.env` e `__pycache__`.
- Criar pastas `NexusArt/src/` e `NexusArt/src/components/`.

---
*Status: Pronto para execução*
