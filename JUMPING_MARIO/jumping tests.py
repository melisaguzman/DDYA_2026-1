def contar_saltos(alturas):
    altos = 0
    bajos = 0
    i = 0
    while i < len(alturas) - 1:
        if alturas[i + 1] > alturas[i]:
            altos += 1
        elif alturas[i + 1] < alturas[i]:
            bajos += 1
        i += 1
    return altos, bajos


# TESTS
assert contar_saltos([1, 4, 2, 2, 3]) == (2, 1)
assert contar_saltos([4, 3, 2, 1]) == (0, 3)
assert contar_saltos([1, 1, 1, 1]) == (0, 0)
assert contar_saltos([1, 2, 3, 4]) == (3, 0)

print("Todos los tests pasaron correctamente")
