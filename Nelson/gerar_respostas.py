import requests
from bs4 import BeautifulSoup
import json

# Página da wikipedia que escolhi para extrair as informações
url = 'https://pt.wikipedia.org/wiki/Cinema_novo'

# Pegando o conteúdo da página através do método de requisição GET na url
response = requests.get(url)
html_content = response.text

# Realizando a análise dos caracteres do conteúdo da página com a biblioteca BeautifulSoup, para extrair as partes que me interessa
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrando os subtítulos chaves, visto que os parágrafos que serão minha resposta sempre vem depois deles
#Na estrutura html das páginas da wikipedia os subtítulos também são guardados na tag span
influencias = soup.find('span', {'id': 'Influências'})
origem = soup.find('span', {'id': 'Antecedentes'})
caracteristicas = soup.find('span', {'id': 'Temas_e_estilo'})
legado = soup.find('span', {'id': 'Embrafilme'})
representantes = soup.find('span', {'id': 'Principais_nomes_do_cinema_novo'})
filmes = soup.find('span', {'id': 'Primeira_fase'})


#Encontrando todos os parágrafos de resposta e guardando em cada variável separada, além de definir o tamanho de parágrafo de cad auma
paragrafos_origem = [sibling.text for sibling in origem.parent.next_siblings if sibling.name == 'p'][:3]
paragrafos_influencias = [sibling.text for sibling in influencias.parent.next_siblings if sibling.name == 'p'][:2]
paragrafos_caracteristicas = [sibling.text for sibling in caracteristicas.parent.next_siblings if sibling.name == 'p'][:2]
paragrafos_legado = [sibling.text for sibling in legado.parent.next_siblings if sibling.name == 'p'][:2]

#No caso dos representantes e filmes eles não são extruturados de forma de parágrafo, então foi necessário extrair todo conteúdo dentro do li
paragrafos_representantes = representantes.find_next('ul')
representantes_nomes =[]
for item in paragrafos_representantes.find_all('li'):
     representantes_nomes.append(item.text.strip())

paragrafos_filmes = filmes.find_next('ul')
filmes_nomes =[]
for item in paragrafos_filmes.find_all('li'):
     filmes_nomes.append(item.text.strip())     



# A partir dos dados extraídos da página do wikipedia é criado um dicionário com as informações extraídas
info_cinema_novo = {'influencias': paragrafos_influencias,
                    'origem': paragrafos_origem,
                    'caracteristicas': paragrafos_caracteristicas,
                    'legado': paragrafos_legado,
                    'representantes': representantes_nomes,
                    'filmes': filmes_nomes}




# Todas as informações extraidas são salvas em um arquivo JSON que é gerado levando como base o dicionário info_cinema_novo
with open('cinema_novo.json', 'w', encoding='utf-8') as f:
    json.dump(info_cinema_novo, f, ensure_ascii=False, indent=4)



