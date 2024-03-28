frutas = ["pera", "limao", "abacate"]

# pessoas = ["Jose", "Pedro", "Ana"]
# print (frutas)
# print (pessoas)

frutas.append("laranja")
print (frutas)
frutas.insert(0, "uva")
print (frutas)
frutas.remove ("limao")
print (frutas)
print (elemento)
elemento = frutas.pop (2)
frutas.pop(2)
print(frutas)
frutas.reverse()
print(frutas)

frutas.sort()
print(frutas)

frutas.append("uva")
frutas.append("uva")
print(frutas)

nu_uvas = frutas.count("uva")
print("A quantidade de uvas apareceu", num_uvas)

cadastro = {
    "nome":                          "Jairo"
    "Sobrenome":                    "Candido"
    "idade":                           90
    "endereco":                 "Rua Luis Lacava"
    "Cidade":                        "Maua"
    "Estado":                      "Sao Paulo"

    print(cadastro.keys())
    print (cadastro.values())

    nome = cadastro.get("nome")
    print (cadastro)
    cadastro.clear()
    print (cadastro)
