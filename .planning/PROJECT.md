# PROJECT: NexusArt

## O Que É?
NexusArt é um orquestrador inteligente de lore e arte conceitual para RPGs. Ele transforma descrições de personagens em biografias detalhadas e representações visuais consistentes em tempo recorde (< 15s), utilizando memória vetorial para persistência e busca semântica.

## Valor Central
Proporcionar imersão instantânea para jogadores e mestres de RPG através da fusão de narrativa gerativa e arte de alta fidelidade, com rastreabilidade total de custos e performance via LangSmith.

## Contexto
- **Público**: Jogadores de RPG, Mestres de Jogo (GMs), Escritores.
- **Diferencial**: Geração simultânea (paralela) e memória de longo prazo (Supabase pgvector).

## Stack Tecnológica (Alinhada)
- **Interface**: Streamlit
- **Modelos**: 
  - Texto: Google Gemini (via LangChain/LangSmith)
  - Imagem: Google Gemini 2.5 Flash Image
- **Banco Vetorial**: Supabase (pgvector)
- **Monitoramento**: LangSmith
- **Linguagem**: Python 3.10+

## Requisitos (Hipóteses Ativas)
- [ ] Geração de Lore + Arte em menos de 15 segundos.
- [ ] Seleção de estilos artísticos via array de prompts (Dark Fantasy, Cyberpunk, etc).
- [ ] Busca semântica de personagens históricos.
- [ ] Documentação técnica com explicação bloco-a-bloco.
- [ ] Monitoramento de custos e performance no LangSmith.

## Decisões Chave
| Decisão | Racional | Resultado |
| :--- | :--- | :--- |
| Supabase pgvector | Aproveitar ecossistema robusto e busca vetorial integrada ao SQL. | Pendente |
| Google Gemini 2.5 Flash | Unificar Lore e Arte em um único provedor para maior consistência e simplicidade. | Pendente |
| Streamlit | Velocidade de desenvolvimento para interfaces de IA. | Pendente |

---
*Last updated: 2026-04-26 after initialization*
