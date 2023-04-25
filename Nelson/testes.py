import unittest
from nelson import *

CHAMANDO_NELSON = "audios/nelson.wav"
CHAMANDO_OUTRO_NOME = "audios/glauber.wav"
PERGUNTA_ORIGEM = "audios/origem.wav"
PERGUNTA_INFLUENCIAS = "audios/influencias.wav"
PERGUNTA_CARACTERISTICAS = "audios/caracteristicas.wav"
PERGUNTA_LEGADO = "audios/legado.wav"
PERGUNTA_REPRESENTANTES = "audios/representantes.wav"
PERGUNTA_FILMES = "audios/filmes.wav"

class TesteNomeAssistente(unittest.TestCase):

    def testar_reconhecer_nome(self):
        comando = ouvir_microfone(CHAMANDO_NELSON)
        comando = comando.split()

        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()

        self.assertIn("nelson", nome_assistente)

    def testar_nao_reconhecer_outro_nome(self):
        comando = ouvir_microfone(CHAMANDO_OUTRO_NOME)
        comando = comando.split()

        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()

        self.assertEqual("nelson", nome_assistente)


class TestePerguntas(unittest.TestCase):

    def testar_responder_pergunta_sobre_origem(self):
        comando = ouvir_microfone(PERGUNTA_ORIGEM)
        print(f"resposta do assistente: {comando}")
        self.assertTrue(isinstance(comando, str) and comando != "" and "origem" in comando.lower())

    def testar_responder_pergunta_sobre_influencias(self):
        comando = ouvir_microfone(PERGUNTA_INFLUENCIAS)
        print(f"comando reconhecido: {comando}")
        self.assertTrue(isinstance(comando, str) and comando != "" and "influências" in comando.lower())

    def testar_responder_pergunta_sobre_caracteristicas(self):
        comando = ouvir_microfone(PERGUNTA_CARACTERISTICAS)
        print(f"comando reconhecido: {comando}")
        self.assertTrue(isinstance(comando, str) and comando != "" and "características" in comando.lower())

    def testar_responder_pergunta_sobre_legado(self):
        comando = ouvir_microfone(PERGUNTA_LEGADO)
        print(f"comando reconhecido: {comando}")
        self.assertTrue(isinstance(comando, str) and comando != "" and "legado" in comando.lower())

    def testar_responder_pergunta_sobre_filmes(self):
        comando = ouvir_microfone(PERGUNTA_FILMES)
        print(f"comando reconhecido: {comando}")
        self.assertTrue(isinstance(comando, str) and comando != "" and "filmes" in comando.lower())

    def testar_responder_pergunta_sobre_representantes(self):
        comando = ouvir_microfone(PERGUNTA_REPRESENTANTES)
        print(f"comando reconhecido: {comando}")
        self.assertTrue(isinstance(comando, str) and comando != "" and "representantes" in comando.lower())
    

        
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TestePerguntas))

    executor = unittest.TextTestRunner()
    executor.run(testes)