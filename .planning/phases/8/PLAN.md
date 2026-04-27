# PLAN: Fase 8 - Busca Semântica Vetorial

## Objetivo
Implementar a funcionalidade de busca inteligente no NexusArt, permitindo que os usuários recuperem personagens do histórico através de consultas em linguagem natural (ex: "guerreiro das neves") usando cálculos de similaridade de vetores.

## Deliverables
- [ ] Script `src/search_engine.py` contendo a classe `SemanticSearchEngine`.
- [ ] Integração com a função RPC `match_characters` do Supabase pgvector.
- [ ] Refinamento Clean Code: Isolar a lógica de busca (Retrieval) da lógica de gravação (Storage).

## User Acceptance Criteria (UAT)
- [ ] O sistema deve aceitar uma string de busca do usuário e gerar seu respectivo embedding.
- [ ] O motor deve consultar o Supabase e retornar os personagens mais similares (com base no vetor).
- [ ] A resposta deve conter o nome, a lore e a URL da imagem do personagem encontrado.

## Passo a Passo

### 1. Preparação (Clean Code / SRP)
- Criar a classe `SemanticSearchEngine` isolada. O foco desta classe é exclusivamete consultar dados (Read), enquanto a `MemoryEngine` construída na fase 7 focava na inserção (Write).

### 2. Geração do Vetor de Busca
- Reutilizar ou reimplementar a chamada ao `text-embedding-004` para converter a consulta de texto do usuário em um array de 768 floats.

### 3. Chamada ao Supabase (RPC)
- Invocar a função RPC `match_characters` configurada na Fase 2 no Supabase, passando o vetor de busca e recebendo os registros ordenados por similaridade.

---
*Status: Pronto para execução*
