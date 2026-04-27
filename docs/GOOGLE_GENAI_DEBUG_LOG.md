# Guia de Resolução de Erros: Google GenAI (Modernização)

Este guia documenta os erros recorrentes e as soluções implementadas na migração do **NexusArt** para as bibliotecas de produção mais recentes do Google. Use este guia sempre que encontrar erros de "AttributeError" ou "NotFound" em modelos do Google.

## 1. Migração de SDK: A Regra de Ouro
**Nunca misture as duas bibliotecas.**
- **LEGACY (Evite):** `import google.generativeai as genai`
- **MODERN (Produção):** `from google import genai` (da biblioteca `google-genai`)

## 2. Tabela de Substituição de Modelos
Se o código retornar `404 Not Found` para um modelo, substitua conforme abaixo:

| Funcionalidade | Modelo Antigo (Deprecado) | Novo Modelo (Produção) |
| :--- | :--- | :--- |
| **Geração de Arte** | `imagen-3-generate-001` | `imagen-4.0-generate-001` |
| **Embeddings (Vetores)** | `text-embedding-004` | `gemini-embedding-2` |
| **LLM (Orquestração)** | `gemini-1.5-flash` | `gemini-2.0-flash` (ou `gemini-2.5-flash`) |

## 3. Erros de Atributo (AttributeError)
**Erro:** `module 'google.generativeai' has no attribute 'ImageGenerationModel'`
- **Causa:** Você está tentando usar o SDK antigo para chamar o Imagen 4.
- **Solução:** Use o novo cliente unificado:
```python
from google import genai
client = genai.Client(api_key="SUA_CHAVE")
response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='seu prompt',
    config=types.GenerateImagesConfig(number_of_images=1)
)
```

## 4. Conflito de Dimensões (Supabase/pgvector)
**Erro:** `42P10: column "embedding" is of type vector(768) but expression is of type vector(3072)`
- **Causa:** O novo modelo `gemini-embedding-2` gera 3072 dimensões por padrão, mas o seu banco de dados foi criado com 768.
- **Solução:** Force a dimensionalidade no código:
```python
client.models.embed_content(
    model='gemini-embedding-2',
    contents=text,
    config=types.EmbedContentConfig(output_dimensionality=768)
)
```

## 5. Erros de Ambiente e Chaves (Pydantic/Dotenv)
**Erro:** `API key required for Gemini Developer API` (mesmo com a chave no .env)
- **Causa 1:** Arquivo `.env` salvo com codificação "UTF-8 with BOM". Isso adiciona caracteres invisíveis no início do arquivo que quebram a primeira variável.
- **Solução 1:** Salve o `.env` como **UTF-8 (sem BOM)**.
- **Causa 2:** Falta de `load_dotenv()`.
- **Solução 2:** Sempre inicie o script principal com:
```python
import os
from dotenv import load_dotenv
load_dotenv()
```

## 6. Depreciações de Interface (Streamlit)
**Aviso:** `The use_column_width parameter has been deprecated...`
- **Solução:** Substitua `use_column_width=True` por `use_container_width=True` em todas as chamadas de `st.image()`.

---
*Gerado automaticamente pelo Antigravity AI em 27/04/2026 para documentação de Portfólio.*
