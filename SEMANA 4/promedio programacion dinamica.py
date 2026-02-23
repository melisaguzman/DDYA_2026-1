def est_prom():
    n = int(input("Digite la cantidad de estudiantes: "))

    promedios = []
    estudiantes = []

    for i in range(n):
        datos = input("Ingrese nombre y sus notas (puede ser cantidad diferente para cada estudiante) separadas por espacio: ").split()

        while len(datos) < 2:
            datos = input("Error, digite nuevamente: ").split()

        nombre = datos[0]
        suma = 0.0
        cantidad = 0
        notas = []

        for j in range(1, len(datos)):
            nota = float(datos[j])
            suma = suma + nota
            cantidad = cantidad + 1
            notas.append(nota)

        promedio = suma / cantidad
        promedios.append(promedio)
        estudiantes.append((nombre, notas, promedio))

    print()

    for estudiante in estudiantes:
        nombre = estudiante[0]
        notas = estudiante[1]
        promedio = estudiante[2]

        print("Nombre:", nombre)
        print("Notas:", notas)
        print("Promedio:", promedio)

        if promedio >= 3.0:
            print("Aprobó")
        else:
            print("No aprobó")
        print()

    dp = []
    for i in range(n + 1):
        dp.append(0)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + promedios[i - 1]

    promedio_general = dp[n] / n

    print("Promedio general del curso:", promedio_general)

est_prom()