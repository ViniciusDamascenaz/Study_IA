from PyPDF2 import PdfReader
import ia


class PDF():

    def __init__(self):
        self.ia_agent = ia.Leitor()

    def estudo(self, nome_pdf, pergunta):
        leitor = PdfReader(nome_pdf)
        conteudo = ""
        for page in leitor.pages:
            conteudo = conteudo + page.extract_text()

        response_ia = self.ia_agent.Leitura(conteudo, pergunta)
        return response_ia
