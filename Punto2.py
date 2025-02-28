numeros_ingresados = []
while len(numeros_ingresados) < 15:
    entrada = input(f"Ingrese un número (máximo 15 números): ")
    if entrada == "":
        break
    try:
        numero = int(entrada)
        numeros_ingresados.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")

cuadrado = map(lambda x: x ** 2, numeros_ingresados)

mayor_50 = filter(lambda x: x > 50, numeros_ingresados )