# PLAN: Fase 6.1 - Refatoração Clean Code

## Objetivo
Refatorar a base de código atual para aderir estritamente aos princípios de Clean Code (Uncle Bob), focando em legibilidade, funções pequenas, responsabilidade única (SRP) e nomes significativos.

## Deliverables
- [ ] Refatoração do `src/lore_engine.py`.
- [ ] Refatoração do `src/art_engine.py`.
- [ ] Refatoração do `src/orchestrator.py`.

## Critérios de Limpeza
- **Small Functions**: Nenhuma função deve ter mais que 20 linhas (idealmente).
- **One Thing**: Cada função deve fazer apenas uma coisa.
- **Meaningful Names**: Variáveis e funções devem ter nomes que revelem intenção.
- **No Side Effects**: Funções puras sempre que possível.

## Passo a Passo

### 1. Refatorar LoreEngine
- Separar a configuração do Prompt da lógica de execução.
- Melhorar a legibilidade do Pydantic.

### 2. Refatorar ArtEngine
- Extrair `_build_visual_prompt` para um método privado.
- Criar um método dedicado para salvar a imagem (`_save_image_to_assets`).

### 3. Refatorar Orchestrator
- Isolar a lógica de execução do pool de threads.

---
*Status: Pronto para execução*
