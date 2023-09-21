# Pedir al usuario que ingrese un número
numero = float(input("Ingresa un número: "))

# Comprobar si el número es positivo, negativo o igual a cero
if numero > 0:
    print(f"{numero} es un número positivo.")
elif numero < 0:
    print(f"{numero} es un número negativo.")
else:
    print("El número es igual a 0.")