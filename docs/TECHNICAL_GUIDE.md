# NexusArt - Guia Técnico e Arquitetural 🧙‍♂️📖

Este guia detalha a engenharia por trás do NexusArt, construído com foco em **Clean Code** (Princípios SOLID / Uncle Bob) e Alta Performance.

## 1. O Cérebro: `lore_engine.py`
O **Lore Engine** é responsável por criar a biografia detalhada do personagem.
- **Tecnologia**: Google Gemini 2.5 Flash via `langchain_google_genai`.
- **Clean Code (Structured Output)**: Usamos Pydantic (`CharacterLore`) para forçar a IA a retornar um objeto JSON perfeitamente tipado. Isso elimina a necessidade de fazer "parsers" manuais de texto e garante que a UI nunca quebre por falta de um campo.
- **Separação de Preocupações**: A classe `LoreEngine` não sabe nada sobre banco de dados ou imagens. Seu único papel é receber texto e devolver um objeto `CharacterLore`.

## 2. A Visão: `art_engine.py`
O **Art Engine** transforma a lore gerada em uma pintura conceitual.
- **Tecnologia**: Google Imagen 4.0 (via `google-genai`).
- **Engenharia de Prompt Privada**: O método `_build_visual_prompt` encapsula a lógica de juntar os estilos escolhidos pelo usuário (ex: "Dark Fantasy") com a descrição. A API recebe instruções precisas de iluminação cinematográfica.
- **Persistência Local**: O motor baixa a imagem gerada e a salva na pasta `assets/`, devolvendo apenas o caminho do arquivo para o resto do sistema.

## 3. A Memória: `memory_engine.py` e `search_engine.py`
- **Memory Engine (Write)**: Gera um vetor numérico (Embedding) da biografia usando `text-embedding-004` e salva os dados na tabela `characters` do **Supabase**.
- **Search Engine (Read)**: Uma classe isolada (respeitando o SRP) que pega a busca do usuário, transforma num vetor, e chama a função RPC `match_characters` no PostgreSQL para calcular a Similaridade Coseno usando **pgvector**.

## 4. O Maestro: `orchestrator.py`
Para batermos a meta de gerar personagens em **menos de 15 segundos**, a orquestração é vital.
- **Paralelismo Assíncrono**: O `NexusOrchestrator` usa `asyncio` e `ThreadPoolExecutor`.
- Ao invés de esperar a Lore terminar para então gerar a Arte, ele dispara ambas as requisições de rede ao mesmo tempo. O tempo total de espera do usuário é apenas o tempo do motor que demorar mais (geralmente a imagem), poupando pelo menos 5 a 8 segundos preciosos.

## 5. O Palco: `app.py`
A interface foi escrita em **Streamlit**.
- Ela não contém regras de negócio. Apenas coleta os inputs, roda o `NexusOrchestrator` dentro de um `asyncio.run()`, e usa colunas e abas para renderizar os resultados.

---
*Este projeto foi desenvolvido utilizando a metodologia GSD (Get Shit Done) e práticas rigorosas de engenharia de software.*
