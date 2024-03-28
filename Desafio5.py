# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   1. O aluno deverá digitar 3 notas através do teclado
#   2. Seu programa deverá calcular a média das notas    
#   3. A partir da média, verificar qual situação o aluno se encontra 
# conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   4. Não será permitido médias acima de 100 e abaixo de zero
#   5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de digitação
#   6. Mostrar na tela para o aluno a situação final baseado na nota digitada.

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
if media >= 0 and media <= 100:
    if media >= 70:
        print("Aprovado")
    elif media >= 40 and media < 70:
        print("Exame")
    else:
        print("Reprovado")
else:
        print("Erro no valoe da media, calcule novamente")

        

