def fibonacci(num):
    if num < 0:
        return False
    valor1 = 5 * num * num + 4
    valor2 = 5 * num * num - 4

    s1  = int(valor1**0.5)
    s2 = int(valor2**0.5)
    if s1*s1 == valor1 or s2*s2==valor2:
       return True
    else:
        return False



def def_num():
   for i in range(5):
      
      num = int (input("Ingrese un número: "))
      print("Su número es:", num)
          
      
      
      if num > 0:
         print("\nEl número escogido es positivo")
      elif num < 0:
         print("\nEl número ingresado es negativo")
      else:
         print("El número es 0") 
      if num % 2 != 0 :
           print("\nEl número es primo")
      else:
           print("\nEl número no es primo")
      if fibonacci(num) == True:
           print("\nEl número es de la serie fibonacci")
      else:
           print("\nEl número no es de la serie fibonacci")

           
def_num()
         