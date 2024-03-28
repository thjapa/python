# Descobrir se o triangulo é
# Equilátero (Todos os lados iguais)
# Isoceles (2 lados iguais)
# Escaleno (todos os lados diferentes)

l1 = int(input("Digite o lado 1: "))
l2 = int(input("Digite o lado 2: "))
l3 = int(input("Digite o lado 3: "))

if l1 == l2 and l2 == l3 and l1 == l3:
    print("Equilatero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Isoceles")
else:
    print("Escaleno")
   