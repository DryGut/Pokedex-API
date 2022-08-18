import requests
import json

"""
    Utilizando a API POKEDEX para criação de um arquivo JSON
    com dados sobre os pokemons
     
     dados a serem coletados:
          id = identificação do pokemon na API
          name = nome do pokemon
          types = o tipo do pokemon
          ability = habilidades que o pokemon possui
          stats = atributos do pokemon 
"""
TOTAL_POKEMONS = 151 #constante com a definição de quantos pokemons serão coletados

def req_api():
  """ 
  Requisição da API 
  e estruturação dos Dados coletados 
  """
    
  bichos = [] 
  
  #constroi a url com o parâmetro que será passado
  url = 'https://pokeapi.co/api/v2/pokemon/'
     
    
  #verifica a resposta da url e retorna o arquivo json da API
  try:
    for i in range(TOTAL_POKEMONS): #laço dos pokemons que serão utilizados
      resp = requests.get(f'{url}{i+1}')
      if resp.status_code == 200:
        conteudo = resp.json()
       
        #estrutura de dados que será salvo no arquivo JSON
        a_bichos = {
          'id': conteudo['id'],
          'name': conteudo['name'],
          'sprite': f"{i+1}.png",
          'types': [],
          'ability': [],
          'stats': []
        }
        #laços que farão a coleta dos dados a serem salvos
        for type in conteudo['types']:
          a_bichos['types'].append(type['type']['name'])
        for skill in conteudo['abilities']:
          a_bichos['ability'].append(skill['ability']['name'])
        for stats in conteudo['stats']:
          a_bichos['stats'].append({stats['stat']['name']: stats['base_stat']})
        
        bichos.append(a_bichos)
      else:
        return resp.status_code
        
  except:
    print("Erro na Conexao") #caso a resposta http seja diferente do code 200 retorna o erro
  
  return bichos

#função para baixar as imagens dos pokemons

def download_images():
  
  for i in range(TOTAL_POKEMONS):
      url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i+1}.png'
      resp = requests.get(url, allow_redirects=True)
      open(f'sprites/{i+1}.png', 'wb').write(resp.content)
      print(f'Baixando Sprite {i+1}')

#função para salvar a estrutura de dados em arquivo JSON
def write_to_json(pokemon_lista):
  with open('listapokemon.json', 'w') as arq:
    json.dump(pokemon_lista, arq, indent=4, ensure_ascii=False)
    arq.close()

def main():
  pokemon = req_api()
  write_to_json(pokemon)
  download_images()
if __name__ == '__main__':
  main()