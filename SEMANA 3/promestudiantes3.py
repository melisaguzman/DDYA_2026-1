def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])
    
    return merge(izquierda, derecha)


def merge(izq, der):
    resultado = []
    i = 0
    j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado


def est_prom():
    n = int(input("Digite la cantidad de estudiantes: "))
    m = int(input("Digite la cantidad de notas que desea calcular por estudiante: "))

    aprobados = []
    print("Digite por cada estudiante: nombre y luego sus notas, \n"
          "si es decimal use punto (todo separado por espacios) y de enter entre cada estudiante: ")

    for i in range(n):
        datos = input("Ingrese los datos: ").split()

        while len(datos) != m + 1:
            datos = input("Hubo un error, digite nuevamente nombre y notas separado por espacio: ").split()

        nombre = datos[0]
        suma = 0.0

        for j in range(m):
            suma += float(datos[j + 1])

        promedio = suma / m

        if promedio >= 3.0:
            aprobados.append(nombre)
            print(nombre, "Promedio:", promedio, "aprobó ☺")
        else:
            print(nombre, "Promedio:", promedio, "no aprobó :c")

    aprobados = merge_sort(aprobados)

    print("ESTUDIANTES APROBADOS ORDENADOS:", aprobados)


est_prom()