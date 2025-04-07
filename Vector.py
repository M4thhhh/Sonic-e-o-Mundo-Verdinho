numeros = [10, 20, 30, 40, 50]

# Acessando o primeiro número (índice 0)
primeiro = numeros[0] # 10

# Acessando o terceiro número (índice 2)
terceiro = numeros[2] # 30

# Acessando o último número (índice -1)
# ultimo  = numeros[-1] # 50

#ATIVIDADE 01 DIA 07

cores = ["vermelho", "azul", "verde"]
cores[1] = "roxo"
print(cores) # Saída: ['vermelhos', 'roxo', 'verde']


#ATIVIDADE 02 DIA 07

carros = ["fusca", "gol", "palio", "uno"]

# Percorrendo a lista com for
print("lista de carros:")
for carro in carros:
    print(carro)

#FILMES

filmes = ["Matri", "Interestelar",
          "Vingadores", "Star Wars",
          "O Senhor dos Anéis"]

print("Meus filmes favoritos:")
for filme in filmes:
    print(filme)


#Lista
lista = []

while True:
    item = input('>>')
    if item == 'fim':
        lista.append(item)
        print(f'a lista tem {len(item)}')
        break
    else:
        lista.append(item)
        print(f'a lista tem {len(lista)}')
