def est_prom():
    n = int(input("Digite la cantidad de estudiantes: "))
    m= int(input("Digite la cantidad de notas que desea calcular por estudiante: "))

    aprobados = []
    print("Digite por cada estudiante: nombre y luego sus notas, \n si es decimal use punto (todo separado por espacios) y de enter entre cada estudiante: ")
    for i in range(n):
        datos = input("ingrese los datos: ").split()
        while len(datos)!= m+1:
            datos=input("Hubo un error, digite nuevamente nombre y notas separado por espacio")

        nombre = datos[0]
        suma = 0.0

        for j in range(m):
            suma = suma +float(datos[j+1])

        promedio = suma / m
        if promedio >= 3.0:
            aprobados.append(nombre)
            print(nombre, "promedio:" , promedio, "aprobó ☺")
        else:
            print(nombre, "Promedio:",promedio,"no aprobó :c")

    print("ESTUDIANTES APROBADOS:", aprobados)
est_prom()


