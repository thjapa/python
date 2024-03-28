# Desenvolver um programa para verificar a situacao do aluno
# em relação ao sua programaçao escola
# 1. O aluno deverá digitar sua nota através do teclado 
# 2. Verificar qual situação o aluno se encontra conforme notas abaixo:
#            2.1 nota > 70 - aprovado
#            2.2 nota < 40 - reprovado
#            2.3 nota entre 40 e 7(
nota_da_prova= int(input("Digite sua nota"))
if nota_da_prova >= 70:
    print("Você esta aprovado")

if nota_da_prova <= 40:
    print("Você está reprovado")

if nota_da_prova <70 and nota_da_prova >40:
    print("Você precisará realizar o exame")