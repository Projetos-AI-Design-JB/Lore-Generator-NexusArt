# PLAN: Fase 5 - Motores de Geração (Art Engine)

## Objetivo
Implementar o motor de geração de imagens do NexusArt, utilizando as capacidades multimodais do Gemini 2.5 Flash para criar artes conceituais consistentes com a lore gerada e o estilo selecionado.

## Deliverables
- [ ] Script `src/art_engine.py` com a classe `ArtEngine`.
- [ ] Dicionário de estilos artísticos pré-configurados.
- [ ] Função de orquestração de prompt visual.

## User Acceptance Criteria (UAT)
- [ ] O motor deve receber um objeto `Character` e um array de estilos e retornar uma URL ou objeto de imagem.
- [ ] A imagem deve respeitar os traços físicos descritos na lore.
- [ ] O tempo de geração da imagem deve ser monitorado via LangSmith.

## Passo a Passo

### 1. Mapeamento de Estilos
- Criar um catálogo de prompts técnicos para estilos (ex: "Dark Fantasy" -> "high contrast, moody lighting, detailed armor").

### 2. Implementação do Motor
- Configurar o `ArtEngine` para usar o modelo Gemini de imagem.
- Criar método `generate_portrait` que sintetiza a lore em um prompt visual otimizado.

### 3. Integração de Saída
- Garantir que a imagem possa ser exibida ou salva localmente para teste.

---
*Status: Pronto para execução*
