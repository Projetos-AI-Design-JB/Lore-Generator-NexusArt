import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
from src.lore_engine import LoreEngine, CharacterLore
from src.art_engine import ArtEngine

class NexusOrchestrator:
    """
    Orquestrador de Fluxo Assíncrono.
    Clean Code: Encapsula a complexidade do paralelismo.
    """

    def __init__(self):
        self.lore_engine = LoreEngine()
        self.art_engine = ArtEngine()
        self.thread_pool = ThreadPoolExecutor(max_workers=4)

    async def generate_character_full(self, input_text: str, style_list: List[str]) -> Tuple[CharacterLore, str]:
        """
        Executa Lore e Arte em paralelo para máxima performance (< 15s).
        """
        start_mark = time.time()
        
        lore_task = self._run_async(self.lore_engine.create_character, input_text)
        art_task = self._run_async(self.art_engine.generate_portrait, "Hero", input_text, style_list)

        # Aguarda a conclusão simultânea
        lore_result, art_path = await asyncio.gather(lore_task, art_task)

        self._log_performance(start_mark)
        
        return lore_result, art_path

    async def _run_async(self, func, *args):
        """Clean Code: Helper para transformar funções bloqueantes em tarefas async."""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self.thread_pool, func, *args)

    def _log_performance(self, start_time: float):
        """Registra métricas de execução."""
        duration = time.time() - start_time
        print(f"⚡ [Orchestrator] Ciclo completo em {duration:.2f}s")

if __name__ == "__main__":
    async def run_test():
        nexus = NexusOrchestrator()
        l, a = await nexus.generate_character_full("Guerreiro Solar", ["Oil Painting"])
        print(f"Concluído: {l.name} -> {a}")

    asyncio.run(run_test())
