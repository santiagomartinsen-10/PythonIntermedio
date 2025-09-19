#Ejercicio 4_Clase 3
def calcular_promedio(*numeros):
    
    longitud = len(numeros)

    print(f"La cantidad de numeros que ingreso para promediar son: {longitud}")
    return sum(numeros)/len(numeros) if numeros else "ERROR: No se ingresaron numeros"

promedio = calcular_promedio(10,20,30)


print(f"el promedio de los numeros ingresados es: {promedio}")
