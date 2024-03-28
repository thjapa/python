lista_de_lanches = ["Big Mac", "Mc Cheedar", "Quarteirão", "Big Tasty"]
lista_de_precos = [29,90,27,18,50,35,60]
print("----BEM VINDO AO MC SENAI----")
opcao = int(input("Digite sua opcao de lanche:"))

print(lista_de_lanches[opcao-1])
print("O valor do lanche e R$", lista_de_precos[opcao -1])