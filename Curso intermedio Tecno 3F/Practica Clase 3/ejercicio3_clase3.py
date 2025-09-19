#Ejercicio 3_Clase 3

def numero_par_impar():

    numero = int(input("Ingrese un numero para saber si es par o impar: "))

    residuo = numero % 2

    par_impar = f"El numero ingresado {numero} es PAR" if residuo == 0 else f"El numero ingresado {numero} es IMPAR"

    print(par_impar)

numero_par_impar()