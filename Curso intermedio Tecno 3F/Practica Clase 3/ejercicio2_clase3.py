#Ejercicio 2_Clase 3
#Con lista y una tupla trasformando tupla a lista

def buscar_palabra(lista,*listaargs):

    
    palabra_buscada = input("Ingrese elemento buscado: ")

    encontrado = f'elemento encontrado: {palabra_buscada}' if palabra_buscada in lista or palabra_buscada in listaargs else f'palabra no encontrada' 

    print(encontrado)

listita=[""]
print(listita)
listaargs = ["pc","monitor","mouse"]
print(listaargs)

agregar_elemento = input("ingrese elemento para agregar: ")
listita.append(agregar_elemento)
agregar_elemento2 = input("ingrese otro elemento: ")
listita.append(agregar_elemento2)


buscar_palabra(listita, *listaargs)
