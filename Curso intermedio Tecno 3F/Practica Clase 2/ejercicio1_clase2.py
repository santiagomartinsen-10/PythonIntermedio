
try:
    
    a = int(input("Ingrese primer numero a dividir"))
    b = int(input("Ingrese segundo numero a dividir"))
    if b == 0:
        print("no se puede dividir por cero")
    resultado = (a/b)

    print(f"El resultado es{resultado}")
except Exception as e:
    print(f"Error{e}")
