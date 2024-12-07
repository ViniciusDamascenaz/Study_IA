from groq import Groq

class Leitor():
    def __init__(self):
        self.client = Groq(
            api_key="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",
        )

    def Leitura(self, conteudo, pergunta):
        self.chat_sinistro = self.client.chat.completions.create(
            messages=[

                {
                    "role": "system",
                    "content": f"Use esse conteudo e responda, mas não mencione o conteudo: '{conteudo}'"
                },
                {
                    "role": "user",
                    "content": f"Pergunta: {pergunta}. "
                }

            ],
            model="llama3-70b-8192",
            #model="llama3-8b-8192",
        )
        return self.chat_sinistro.choices[0].message.content