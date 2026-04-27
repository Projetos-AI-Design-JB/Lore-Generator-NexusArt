import os
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

class CharacterLore(BaseModel):
    """
    Representa a estrutura de dados de um personagem gerado.
    Clean Code: Uso de nomes claros e descrições para Guided Generation.
    """
    name: str = Field(description="O nome épico do personagem")
    race: str = Field(description="A raça de fantasia (ex: Humano, Elfo, Orc)")
    character_class: str = Field(description="A classe de RPG (ex: Mago, Ladino)")
    biography: str = Field(description="História de fundo detalhada com 3 parágrafos")
    personality_traits: List[str] = Field(description="Lista de traços comportamentais")
    abilities: List[str] = Field(description="Lista de poderes ou competências")

class LoreEngine:
    """
    Motor central para criação de narrativas épicas.
    Segue SRP: Responsável apenas por transformar entrada de texto em Lore estruturada.
    """

    def __init__(self):
        self._initialize_model()
        self._setup_structured_output()

    def _initialize_model(self):
        """Configura o modelo Gemini com parâmetros narrativos."""
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.8,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    def _setup_structured_output(self):
        """Vincula o esquema Pydantic ao modelo para garantir tipos de dados."""
        self.structured_llm = self.llm.with_structured_output(CharacterLore)

    def create_character(self, user_description: str) -> CharacterLore:
        """
        Gera a lore completa.
        Clean Code: Função principal que delega a montagem do prompt.
        """
        prompt_template = self._build_lore_prompt()
        character_chain = prompt_template | self.structured_llm
        
        return character_chain.invoke({"description": user_description})

    def _build_lore_prompt(self) -> ChatPromptTemplate:
        """Centraliza as instruções de sistema para o modelo."""
        system_instruction = (
            "Você é um mestre de RPG épico. Crie lores ricas, consistentes "
            "e envolventes em português brasileiro."
        )
        return ChatPromptTemplate.from_messages([
            ("system", system_instruction),
            ("user", "Descrição do Personagem: {description}")
        ])

if __name__ == "__main__":
    # Teste rápido de sanidade
    engine = LoreEngine()
    print(engine.create_character("Um pirata amaldiçoado pelo mar."))
