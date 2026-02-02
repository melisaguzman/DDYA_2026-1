
def estudiantes_aprobados():

    cantidad = int(input("Digite la cantidad de estudiantes: "))

    aprobados = []
    nombres = []
    notas = []

    info = input("Digite los nombres y notas: ").split()

    for i in range(cantidad):
        nombres.append(info[2*i])
        notas.append(float(info[2*i + 1]))

    for i in range(cantidad):
        if notas[i] >= 3:
            aprobados.append(nombres[i])

    print("Estudiantes aprobados:", aprobados)

estudiantes_aprobados()
