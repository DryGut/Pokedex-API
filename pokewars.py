import json
"""
Programa que simulará uma batalha pokemon
utilizando o arquivo JSON com os dados 
baixados da API pokedex.

"""
#abrindo o arquivo para utilização
with open('listapokemon.json', 'r') as arq:
    pokemon = json.load(arq)

def poder(nome):
  for poke in pokemon:
    if poke['name'] == nome:
      for i in poke['stats']:
        for k, v in i.items():
          if k == 'attack':
            return v

def defesa(nome):
  for poke in pokemon:
    if poke['name'] == nome:
      for i in poke['stats']:
        for k, v in i.items():
          if k == 'defense':
            return v
    
def vida(nome):
  for poke in pokemon:
    if poke['name'] == nome:
      for i in poke['stats']:
        for k, v in i.items():
          if k == 'hp':
            return v

def dano(poder, nome):
  dano = int(nome) - int(poder) * 0.2
  return dano
              

def luta(poder, defesa):
  dano = poder * 0.2
  if poder > defesa:
    return f"Ataque causou {dano} de dano"
  else:
    return 'Ataque Defendido'

a = input("Player1 digite o nome do pokemon: ")
b = input("Player2 digite o nome do pokemon: ")

print(luta(poder(a), defesa(b)))
print(f"{b.title()} Hp: {dano(poder(a), vida(b))}")
