# PLAN: Fase 4 - Motores de Geração (Lore Engine)

## Objetivo
Implementar o motor de narrativa do NexusArt, capaz de gerar biografias estruturadas e ricas para personagens de RPG utilizando o Gemini 2.5 Flash com saída de dados tipada.

## Deliverables
- [ ] Script `src/lore_engine.py` com a classe `LoreEngine`.
- [ ] Esquema Pydantic `Character` para garantir que a IA retorne dados estruturados (JSON).
- [ ] Prompt System especializado em ambientação de RPG.

## User Acceptance Criteria (UAT)
- [ ] O motor deve retornar um objeto Python com campos: `nome`, `raca`, `classe`, `biografia`, `personalidade` e `habilidades`.
- [ ] A biografia deve ter pelo menos 3 parágrafos.
- [ ] As chamadas devem ser rastreadas no LangSmith.

## Passo a Passo

### 1. Definição do Schema (Pydantic)
- Criar a classe `Character` no `src/lore_engine.py`.
- Adicionar descrições em cada campo para orientar o modelo (Structured Output).

### 2. Implementação do Motor
- Criar a classe `LoreEngine` que herda/usa o `ChatGoogleGenerativeAI`.
- Configurar o prompt que integra a descrição do usuário com as regras do RPG.

### 3. Teste de Geração
- Criar um pequeno bloco de teste no final do arquivo para validar a geração.

---
*Status: Pronto para execução*
