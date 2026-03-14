T = int(input("ingrese el número de casos"))

for caso in range(T):
    N = int(input("ingrese el número de paredes"))
    alturas = input("ingrese las alturas").split()
    
    i = 0
    while i < N:
        alturas[i] = int(alturas[i])
        i = i + 1

    altos = 0
    bajos = 0

    i = 0
    while i < N - 1:
        if alturas[i + 1] > alturas[i]:
            altos = altos + 1
        elif alturas[i + 1] < alturas[i]:
            bajos = bajos + 1
        i = i + 1

    print("Case", caso + 1, ":", altos, bajos)
