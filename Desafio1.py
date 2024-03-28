#desafio 1 - calculo IMC

#text
nome = input("Olá, qual é seu nome: ")
# Número Real
peso = float(input("Digite seu peso: "))
altura = float(input ("Digite sua altura: "))

imc = peso / (altura ** 2)
imc = round(imc, 2)
print(f" {nome} seu IMC é {imc}")

#print (nome, "seu IMC é", "% 2f" %imc )
