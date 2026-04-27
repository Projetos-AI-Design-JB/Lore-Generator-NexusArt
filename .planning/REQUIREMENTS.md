# REQUIREMENTS: NexusArt

## 1. Interface (Streamlit)
- [ ] **Input**: Campo de texto para descrição do personagem.
- [ ] **Estilo**: Selectbox/Multiselect para estilos artísticos (ex: Watercolor, Oil Painting, Digital Art, Sketch).
- [ ] **Output**: Exibição lado-a-lado (Lore na esquerda, Arte na direita).
- [ ] **Busca**: Barra de busca semântica para recuperar personagens do banco.

## 2. Geração de Conteúdo (AI Engines)
- [ ] **Paralelismo**: Executar chamadas de Texto e Imagem simultaneamente para atingir o limite de 15s.
- [ ] **Lore Prompt**: Estruturado para gerar biografia, traços de personalidade e ganchos de aventura.
- [ ] **Art Engine**: Google Gemini 2.5 Flash Image com suporte a arrays de estilo.

## 3. Persistência (Supabase pgvector)
- [ ] **Schema**: Tabela `characters` com colunas: `id`, `name`, `lore`, `image_url`, `embedding` (vector), `metadata`.
- [ ] **Embeddings**: Gerar embeddings do texto da lore para busca semântica.
- [ ] **Security**: Uso obrigatório de `.env` para chaves.

## 4. Monitoramento (LangSmith)
- [ ] **Traces**: Cada geração deve ser rastreada no LangSmith.
- [ ] **Costs**: Implementar cálculo/visualização de tokens consumidos e latência.

## 5. Documentação e README
- [ ] **README.md**: Guia de instalação, configuração de env e explicação da arquitetura.
- [ ] **Code Docs**: Comentários explicativos em cada bloco funcional do código.
