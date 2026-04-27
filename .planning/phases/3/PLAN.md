# PLAN: Fase 3 - Integração LangSmith (Monitoramento)

## Objetivo
Configurar o rastreamento (tracing) das chamadas de IA para garantir que a performance (< 15s) e os custos sejam monitorados desde o início do desenvolvimento.

## Deliverables
- [ ] Script `src/test_connectivity.py` para validar chamadas ao Gemini 2.5 Flash com LangSmith ativo.
- [ ] Implementação de logs de custo e latência no console.
- [ ] Documentação de ativação do LangSmith no `.env`.

## User Acceptance Criteria (UAT)
- [ ] Ao rodar o script de teste, um novo trace deve aparecer no dashboard do LangSmith.
- [ ] O script deve capturar o tempo de resposta da chamada de IA.
- [ ] As variáveis `LANGCHAIN_TRACING_V2` e `LANGCHAIN_API_KEY` devem estar configuradas no `.env`.

## Passo a Passo

### 1. Script de Conectividade
- Criar `NexusArt/src/test_connectivity.py`.
- Usar `langchain_google_genai` para instanciar o Gemini.
- Envelopar a chamada em um contexto de tracing do LangSmith.

### 2. Validação de Performance
- Adicionar medição de tempo (`time.time()`) para validar a meta de < 15s.

---
*Status: Pronto para execução*
