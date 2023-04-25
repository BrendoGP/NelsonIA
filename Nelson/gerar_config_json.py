import json

# Código responsável por ler o arquivo json que foi gerado automaticamente para guardar as respostas;
with open('cinema_novo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# Criando uma relação de chave e valor para obter uma correspondência entre a palavra chave de cada pergunta e sua resposta
perguntas_respostas = [
    {"nome": "influencias", "resposta": data["influencias"]},
    {"nome": "origem", "resposta": data["origem"]},
    {"nome": "caracteristicas", "resposta": data["caracteristicas"]},
    {"nome": "legado", "resposta": data["legado"]},
    {"nome": "representantes", "resposta": data["representantes"]},
    {"nome": "filmes", "resposta": data["filmes"]}
]

# Gerando um arquivo JSON com as perguntas e respostas já em estrutura de chave e valor
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(perguntas_respostas, f, ensure_ascii=False, indent=4)
