persona= {"nombre": "belen",
        "apellido": "perez",
        "edad": "30"
        }

clave_elegida = input("ingrese clave a buscar: ")

try :
    
    valor = persona[clave_elegida]
    print(f"la clave elegida es {clave_elegida} = {valor}")

except KeyError:
    #print(f"la clave es incorrecta {persona[clave_elegida]}no se encuentra")
    print(f"La clave ingresada no se encuentra:{KeyError}")