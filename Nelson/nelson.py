import speech_recognition as sr
import json
import unidecode

#Brendo Gomes Prates
#Gustavo Elías (Mordekai)

# Leitura do arquivo json contendo as perguntas e as respostas
global nome_assistente
nome_assistente = "nelson"
with open('config.json', 'r') as f:
 data = json.load(f)

#Função para capturar a fala através do speech_recognition   
def ouvir_microfone():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source)
        print("Diga algo...")
        audio = reconhecedor.listen(source)
        try:
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            print("Você disse: {}".format(texto))
            return texto
        except:
            print("Não foi possível entender o que você disse.")
            return ""
#Função criado para buscar as respotas pela palavra chave da pergunta
def buscar_resposta(pergunta):
    # Inicializa as variáveis de pontuação e resposta
    pontuacao_maxima = 0
    resposta = "Desculpe, não entendi a pergunta."

    # Percorrendo a lista de dicionários procurando a resposta mais adequada
    for dicionario in data:
        # Dividindo a chave em palavras-chave para ver se elas estão presentes na pergunta
        palavras_chave = dicionario["nome"].split()
        pontuacao = 0
        for palavra in palavras_chave:
            if palavra in pergunta:
                pontuacao += 1
        if pontuacao > pontuacao_maxima:
            pontuacao_maxima = pontuacao
            resposta = dicionario["resposta"]

    # Retornando a resposta que teve a maior pontuação e consequentemente é a mais adequada para ser considerada a correta
    return resposta

if __name__ == "__main__":
    while True:
        pergunta = ouvir_microfone()
        pergunta_sem_acentos = unidecode.unidecode(pergunta) 
        if pergunta.lower().startswith(nome_assistente):
            resposta = buscar_resposta(pergunta_sem_acentos)
            print("Aqui está a sua resposta: ", resposta)

        else:
            print("O primeiro comando de voz deve ser o nome do assistênte (Nelson)")    
