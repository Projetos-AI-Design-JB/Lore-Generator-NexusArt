# PLAN: Fase 2 - Configuração do Supabase (Memory)

## Objetivo
Configurar o banco de dados Supabase com suporte a busca vetorial (pgvector) para armazenar os personagens gerados pelo NexusArt e permitir buscas semânticas.

## Deliverables
- [ ] Script SQL para habilitação da extensão `vector`.
- [ ] Script SQL para criação da tabela `characters`.
- [ ] Script SQL para criação da função de busca semântica (`match_characters`).
- [ ] Documentação de configuração do Supabase no README do projeto.

## User Acceptance Criteria (UAT)
- [ ] A tabela `characters` deve ter uma coluna do tipo `vector(1536)` (ajustado para o modelo de embedding padrão do Google/OpenAI).
- [ ] Deve ser possível inserir um registro de teste via SQL.
- [ ] A função `match_characters` deve retornar resultados ordenados por similaridade de cosseno.

## Passo a Passo

### 1. Preparação SQL
- Criar `NexusArt/src/database_setup.sql`:
  - `CREATE EXTENSION IF NOT EXISTS vector;`
  - Tabela `characters` com colunas para Lore, Imagem e Embeddings.
  - Função `match_characters` para RPC (Remote Procedure Call).

### 2. Documentação de Setup
- Adicionar instruções no README de como o usuário deve rodar o SQL no painel do Supabase.

---
*Status: Pronto para execução*
