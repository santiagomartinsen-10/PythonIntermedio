
try:
    a= int(input("ingrese primer valor: "))

    b= input("ingrese texto: ")
    
    
    resultado = a + b
    print(resultado)

except ValueError:
    print("El primer valor debe ser numerico")

except TypeError as e:
    print("no se puede sumar entero con texto")
    print(e)