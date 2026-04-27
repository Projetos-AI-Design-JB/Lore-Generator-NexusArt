# PLAN: Fase 9 - Interface com Streamlit

## Objetivo
Desenvolver a interface gráfica (UI) do NexusArt usando a biblioteca `streamlit`, consolidando os motores de Geração, Orquestração e Memória em um painel interativo e visual.

## Deliverables
- [ ] Script `app.py` na raiz do projeto NexusArt.
- [ ] Integração com `NexusOrchestrator` (para gerar), `MemoryEngine` (para salvar) e `SemanticSearchEngine` (para buscar).
- [ ] Interface contendo inputs de texto, seleção de estilo e abas (Tabs) para separar "Gerador" de "Biblioteca/Busca".
- [ ] Adicionar `streamlit` ao `requirements.txt`.

## User Acceptance Criteria (UAT)
- [ ] O usuário deve conseguir digitar uma descrição, selecionar estilos e gerar um personagem clicando em um botão.
- [ ] A tela deve mostrar a biografia (em texto) e o retrato (imagem) após a geração assíncrona.
- [ ] O usuário deve conseguir buscar personagens passados usando a barra de busca e obter resultados relevantes.
- [ ] Código escrito com foco em Clean Code (separando responsabilidades visuais da lógica de estado).

## Passo a Passo

### 1. Preparação
- Instalar/Adicionar `streamlit` às dependências.
- Criar a estrutura base do `app.py`.

### 2. Tab "Forja" (Gerador)
- Input text para descrição e Selectbox/Multiselect para Estilos.
- Botão "Forjar Personagem".
- Usar `st.spinner` durante a chamada ao `NexusOrchestrator`.
- Exibição de 2 colunas: uma para a imagem e outra para a biografia e atributos.
- Lógica de persistência automática usando `MemoryEngine` ao gerar.

### 3. Tab "Biblioteca" (Busca Semântica)
- Barra de busca textual.
- Exibição dos resultados do `SemanticSearchEngine` usando cards ou colunas.

---
*Status: Pronto para execução*
