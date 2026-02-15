
#PUNTO 1

def encontrar_minimo(arr, low, high):
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2
    
    if arr[mid] > arr[mid + 1]:
        return encontrar_minimo(arr, mid + 1, high)
    else:
        return encontrar_minimo(arr, low, mid)


#PUNTO 2

def encontrar_faltante(arr, low, high):
    if low > high:
        return low + 1
    
    mid = (low + high) // 2
    
    if arr[mid] == mid + 1:
        return encontrar_faltante(arr, mid + 1, high)
    else:
        return encontrar_faltante(arr, low, mid - 1)

#PUNTO 3

def potencia(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    
    mitad = potencia(a, n // 2)
    
    if n % 2 == 0:
        return mitad * mitad
    else:
        return a * mitad * mitad

#PUNTO 4

def merge(left, right):
    resultado = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    
    return resultado

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

#PUNTO 5

def contar_bits(n):
    return bin(n).count("1")

def suma_bits_hasta(N):
    total = 0
    for i in range(1, N + 1):
        total += contar_bits(i)
    return total

def encontrar_N(X, low, high):
    if low >= high:
        return low
    
    mid = (low + high) // 2
    
    if suma_bits_hasta(mid) >= X:
        return encontrar_N(X, low, mid)
    else:
        return encontrar_N(X, mid + 1, high)
