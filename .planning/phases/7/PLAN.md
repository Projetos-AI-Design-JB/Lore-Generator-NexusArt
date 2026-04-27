# PLAN: Fase 7 - Pipeline de Memória (Supabase Storage)

## Objetivo
Implementar a camada de persistência vetorial do NexusArt, permitindo que personagens gerados sejam salvos no Supabase com seus respectivos embeddings para busca semântica futura.

## Deliverables
- [ ] Script `src/memory_engine.py` com a classe `MemoryEngine`.
- [ ] Integração com `text-embedding-004` do Google (768 dimensões).
- [ ] Conexão robusta com o Supabase via `supabase-py`.

## User Acceptance Criteria (UAT)
- [ ] O sistema deve gerar um vetor de 768 números para cada lore de personagem.
- [ ] Os dados (Lore, URL da imagem e Vetor) devem ser inseridos com sucesso na tabela `characters`.
- [ ] O código deve seguir os princípios de Clean Code (SRP).

## Passo a Passo

### 1. Configuração do Cliente
- Inicializar `supabase-py` usando as credenciais do `.env`.
- Configurar o motor de embeddings do Google.

### 2. Implementação da Persistência
- Criar método `_generate_embedding(text)` para converter lore em vetor.
- Criar método `save_character(character_lore, image_path)` que orquestra a inserção no banco.

### 3. Teste de Inserção
- Criar script `src/test_memory.py` para validar a gravação de um personagem fictício.

---
*Status: Pronto para execução*
