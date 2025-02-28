def procesar_lista(numeros):
  
    suma = sum(numeros)
    max_num = max(numeros)
    min_num = min(numeros)
    
    promedio = suma / len(numeros)
    
    return suma, max_num, min_num, promedio


numeros_ingresados = []
while len(numeros_ingresados) < 10:
    entrada = input(f"Ingrese un número (máximo 10 números): ")
    if entrada == "":
        break
    try:
        numero = int(entrada)
        numeros_ingresados.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")

if numeros_ingresados:
    suma, max_num, min_num, promedio = procesar_lista(numeros_ingresados)
    print(f"Suma: {suma}")
    print(f"Número más grande: {max_num}")
    print(f"Número más pequeño: {min_num}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron números.")