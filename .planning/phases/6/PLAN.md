# PLAN: Fase 6 - Orquestração Assíncrona

## Objetivo
Criar o orquestrador central do NexusArt que executa os motores de Lore e Arte simultaneamente usando `asyncio`, garantindo que o tempo total de resposta seja inferior a 15 segundos.

## Deliverables
- [ ] Script `src/orchestrator.py` com a classe `NexusOrchestrator`.
- [ ] Implementação de métodos assíncronos (`async/await`) para os motores.
- [ ] Benchmarking integrado para validar a latência.

## User Acceptance Criteria (UAT)
- [ ] O tempo total de geração de Lore + Arte deve ser menor que 15 segundos em condições normais.
- [ ] Erros em um motor não devem travar o outro (graceful degradation).
- [ ] O resultado final deve consolidar os dados do `Character` e o caminho da imagem.

## Passo a Passo

### 1. Refatoração para Async
- Adaptar as chamadas dos motores no `orchestrator.py` para rodar em threads ou de forma assíncrona (visto que as SDKs de IA costumam ser bloqueantes por padrão).

### 2. Implementação do Orquestrador
- Criar `generate_all(description, styles)` que dispara ambas as tarefas em paralelo via `asyncio.gather`.

### 3. Validação de Performance
- Criar script de teste `src/test_orchestrator.py` para medir a velocidade real da integração.

---
*Status: Pronto para execução*
