
#Ejercicio 5_Clase 3

def generando_error_lista(lista_obligatoria, *tupla, **dicc):

    print(f"Argumento obligatorio lista: {lista_obligatoria}")
    print(f"Argumentos posicionales (**tupla): {tupla}")
    print(f"Argumentos de palabra clave (**dicc): {dicc}")    

try:
    generando_error_lista() #Si pongo algun valor no me daria error ya que le doy un valor a lista obligatoria
except TypeError as e:
    print(f"No se paso algun argumento  {e}")


