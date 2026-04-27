import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import Client

# 1. Carregamento de Configurações
# O bloco abaixo carrega as variáveis de ambiente do arquivo .env.
# Isso é crucial para a segurança, evitando chaves de API expostas no código.
load_dotenv()

def test_nexus_connectivity():
    print("🚀 Iniciando teste de conectividade NexusArt...")
    
    # 2. Inicialização do Cliente LangSmith
    # O LangSmith monitora cada chamada de IA. Se as variáveis LANGCHAIN_TRACING_V2
    # e LANGCHAIN_API_KEY estiverem no .env, o rastreio é automático.
    ls_client = Client()
    
    # 3. Configuração do Modelo Gemini
    # Usamos o Gemini 2.5 Flash para garantir alta performance (< 15s).
    # O parâmetro 'temperature' define a criatividade (0.7 é ideal para Lore).
    try:
        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.7
        )
        
        # 4. Medição de Performance (Critério de Aceitação: < 15s)
        start_time = time.time()
        
        print("📝 Gerando Lore de teste...")
        response = model.invoke("Descreva um guerreiro anão de uma mina de cristal em 2 frases.")
        
        end_time = time.time()
        latency = end_time - start_time
        
        # 5. Exibição de Resultados
        print("\n--- Resultado do Teste ---")
        print(f"Lore: {response.content}")
        print(f"⏱️ Latência: {latency:.2f} segundos")
        
        if latency < 15:
            print("✅ Critério de Performance atingido!")
        else:
            print("⚠️ Latência acima de 15s. Precisamos otimizar.")
            
        print("\n🔗 Verifique seu dashboard no LangSmith para ver o trace completo.")

    except Exception as e:
        print(f"❌ Erro na conexão: {e}")

if __name__ == "__main__":
    test_nexus_connectivity()
