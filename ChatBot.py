from groq import Groq

client = Groq(
    api_key="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"
)

def mandar_mensagem(mensagem):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": mensagem,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion

while True:
    mensagem_usuario = input("\fVocê: ")
    if mensagem_usuario.lower() in ["sair", "exit"]:
        print("Saindo...")
        break
    mensagem = mandar_mensagem("Responda em português: " + mensagem_usuario)
    print("ChatBot:", mensagem.choices[0].message.content)
