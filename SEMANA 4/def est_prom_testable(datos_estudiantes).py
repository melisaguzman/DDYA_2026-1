def est_prom_testable(datos_estudiantes):
    promedios = []
    
    for datos in datos_estudiantes:
        nombre = datos[0]
        notas = datos[1]
        
        suma = 0
        cantidad = 0
        
        for nota in notas:
            suma = suma + nota
            cantidad = cantidad + 1
        
        promedio = suma / cantidad
        promedios.append(promedio)
    
    suma_total = 0
    for p in promedios:
        suma_total = suma_total + p
    
    promedio_general = suma_total / len(promedios)
    
    return promedios, promedio_general
# Caso 1
datos1 = [
    ("Ana", [4.0, 3.0, 5.0]),
    ("Luis", [2.0, 3.0])
]

proms, pg = est_prom_testable(datos1)

assert round(proms[0], 2) == 4.00
assert round(proms[1], 2) == 2.50
assert round(pg, 2) == 3.25


# Caso 2 – Una sola nota por estudiante
datos2 = [
    ("Carlos", [4.0]),
    ("Maria", [3.5]),
    ("Sofia", [2.8])
]

proms, pg = est_prom_testable(datos2)

assert round(proms[0], 2) == 4.00
assert round(proms[1], 2) == 3.50
assert round(proms[2], 2) == 2.80


print("Todos los tests pasaron correctamente.")
