from groq import Groq

client = Groq(
    api_key="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"
)

def mandar_mensagem(historico):
    chat_completion = client.chat.completions.create(
        messages=historico,
        model="llama3-8b-8192",
    )
    return chat_completion

# Inicializa o histórico de mensagens
historico = []

while True:
    mensagem_usuario = input("\fVocê: ")
    if mensagem_usuario.lower() in ["sair", "exit"]:
        print("Saindo...")
        break
    
    # Adiciona a mensagem do usuário ao histórico
    historico.append({"role": "user", "content": mensagem_usuario})
    
    # Envia o histórico para o chatbot
    mensagem = mandar_mensagem(historico)
    
    # Captura e imprime a resposta do chatbot
    resposta_chatbot = mensagem.choices[0].message.content
    print("ChatBot:", resposta_chatbot)
    
    # Adiciona a resposta do chatbot ao histórico
    historico.append({"role": "assistant", "content": resposta_chatbot})
