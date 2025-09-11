try: 
    
    a = int(input("ingresa primer numero a dividir: "))
    b = int(input("ingrese segundo numero a dividir: "))
    
    resultado = a/b
    print(f"el resultado de la division es: {resultado}")

except ValueError:
    print(f"Ambos operadores deben ser numericos")
    print(ValueError)
except ZeroDivisionError:
    print(f"El divisor no puede ser 0")
    print(ZeroDivisionError)

