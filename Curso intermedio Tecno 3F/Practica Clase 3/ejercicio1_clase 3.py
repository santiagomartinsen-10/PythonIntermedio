#Ejercicio 1_Clase 3


def calcular_mayor():

    try:

        numero1 = int(input("Ingrese primer numero: "))
        numero2 = int(input("Ingrese segundo numero: "))

        numero_mayor = f'los numeros son iguales' if numero1 == numero2 else f'este numero es el mayor: {numero1}' if numero1 > numero2 else f'este numero es el mayor: {numero2}'

        print(numero_mayor)


    except ValueError:
        print("Ingresar numeros enteros.")


    except Exception as e:
        print(f"dio en Error: {e}")

calcular_mayor()