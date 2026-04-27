import os
from typing import List
from dotenv import load_dotenv
from supabase import create_client, Client
from google import genai
from google.genai import types
from src.lore_engine import CharacterLore

load_dotenv()

class MemoryEngine:
    """
    Responsável pela persistência e inteligência vetorial (Memória).
    Clean Code: Separação de preocupações entre Embeddings e Banco de Dados.
    """

    def __init__(self):
        self._initialize_supabase()
        self._initialize_embeddings()

    def _initialize_supabase(self):
        """Configura a conexão com o banco de dados Supabase."""
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.db: Client = create_client(url, key)

    def _initialize_embeddings(self):
        """Configura o motor de vetores do Google."""
        self.client = genai.Client()

    def save_character(self, lore: CharacterLore, image_url: str):
        """
        Salva o personagem completo no banco de dados.
        Clean Code: Orquestra a geração de vetor e a inserção.
        """
        embedding = self._generate_embedding(lore.biography)
        
        data = {
            "name": lore.name,
            "lore": lore.model_dump_json(), # Salvamos o objeto completo como JSON
            "image_url": image_url,
            "embedding": embedding
        }

        try:
            response = self.db.table("characters").insert(data).execute()
            print(f"💾 Personagem '{lore.name}' salvo com sucesso na memória.")
            return response
        except Exception as error:
            print(f"❌ Erro ao salvar na memória: {error}")
            return None

    def _generate_embedding(self, text: str) -> List[float]:
        """
        Converte texto em um vetor de 768 dimensões.
        Usa o modelo gemini-embedding-2 para compatibilidade com pgvector.
        """
        result = self.client.models.embed_content(
            model="gemini-embedding-2",
            contents=text,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_DOCUMENT",
                output_dimensionality=768
            )
        )
        return result.embeddings[0].values

if __name__ == "__main__":
    # Teste rápido
    from src.lore_engine import CharacterLore
    test_lore = CharacterLore(
        name="Teste", race="Humano", character_class="Bardo",
        biography="Uma lenda sobre o código limpo.",
        personality_traits=["Calmo"], abilities=["Refatoração"]
    )
    mem = MemoryEngine()
    mem.save_character(test_lore, "assets/test.png")
