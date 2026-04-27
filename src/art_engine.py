import os
import time
from typing import List
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

class ArtEngine:
    """
    Motor visual do NexusArt.
    Clean Code: Separação entre Prototipagem de Estilo e Execução de Geração.
    """

    def __init__(self):
        self._load_style_presets()
        self.client = genai.Client()

    def _load_style_presets(self):
        """Define o catálogo técnico de estilos visuais."""
        self.styles = {
            "Dark Fantasy": "grim atmosphere, dramatic shadows, moody lighting",
            "Cyberpunk": "neon, futuristic, cinematic night",
            "Watercolor": "soft textures, artistic watercolor paint",
            "Oil Painting": "classic canvas, rich brushstrokes",
            "Sketch": "charcoal, rough hand-drawn concept"
        }

    def generate_portrait(self, name: str, description: str, style_list: List[str]) -> str:
        """Coordenador principal da geração de imagem."""
        visual_prompt = self._build_visual_prompt(name, description, style_list)
        
        try:
            image_response = self._execute_api_call(visual_prompt)
            return self._persist_image(image_response, name)
        except Exception as error:
            print(f"❌ Erro na geração de arte: {error}")
            return ""

    def _build_visual_prompt(self, name: str, desc: str, selected_styles: List[str]) -> str:
        """Clean Code: Transforma lore e estilos em um prompt técnico conciso."""
        technical_styles = [self.styles.get(s, "") for s in selected_styles]
        style_context = ", ".join(technical_styles)
        
        return (
            f"Concept art of {name}. Description: {desc}. "
            f"Art Style: {style_context}. RPG Portrait, professional lighting."
        )

    def _execute_api_call(self, prompt: str):
        """Invoca o motor de imagem do Gemini."""
        return self.client.models.generate_images(
            model='imagen-4.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                person_generation="ALLOW_ADULT",
                output_mime_type="image/jpeg"
            )
        )

    def _persist_image(self, response, name: str) -> str:
        """Salva a imagem no sistema de arquivos e retorna o caminho."""
        if not response.generated_images:
            return ""

        file_name = f"assets/char_{name.replace(' ', '_').lower()}.jpg"
        os.makedirs("assets", exist_ok=True)
        
        image = response.generated_images[0]
        with open(file_name, "wb") as f:
            f.write(image.image.image_bytes)
        
        return file_name

if __name__ == "__main__":
    # Teste rápido
    art = ArtEngine()
    print(art.generate_portrait("Grom", "Orc forte", ["Dark Fantasy"]))
