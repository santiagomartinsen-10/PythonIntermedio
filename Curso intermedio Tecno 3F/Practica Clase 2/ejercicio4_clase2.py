###Practica Con Archivo json:

import json

datos_ejemplo = {"nombre:":"Mario",
                "apellido":"Gonzalez",
                "Telefonos:": ["cel: 111579986","Casa: 4548-4855"]}

try:
    with open('json.json','r',encoding="utf-8") as archivo: #con 'r' intenta leer el archivo, si no existe FilenotfounError
        datos_json = archivo.read()
        print(f"contenido del archivo {datos_json}")
        #archivo.close()

except FileNotFoundError:
    print("El archivo no existe, se intenta crear.... \n")
    
    with open('json.json','w',encoding="utf-8") as archivo:
        datos_json = open('json.json','w',encoding="utf-8")
        json.dump(datos_ejemplo,archivo,indent=4,ensure_ascii=False)
        print(f"archivo creado con exito!! \n")
        #archivo.close()

    with open('json.json','r',encoding="utf-8") as archivo: #con 'w' intenta crear el archivo.
        datos_json = archivo.read()
        print(f"contenido del archivo creado \n{datos_json}")
        #archivo.close()
    

except Exception as e:
    print(f"Ocurrio un Error inesperado {e}")





'''
#Practica Con archivo TXT:


try:
    archivo = open('texto.txt','r',encoding="utf-8") #con 'r' intenta leer el archivo, si no existe FilenotfounError
    contenido = archivo.read()
    print(f"contenido del archivo \n{contenido}")
    #archivo.close()

except FileNotFoundError:
    print("El archivo no existe, se intenta crear.... \n")
    archivo = open('texto.txt','w',encoding="utf-8")#con 'w' crea el archivo
    archivo.write("Prueba linea 1\n")#escribe en el archivo linea 1
    archivo.write("Prueba linea 2\n")#escribe en el archivo linea 2
    archivo.write("Prueba linea 3\n")#escribe en el archivo linea 3
    print(f"archivo creado con exito!! \n")
    #archivo.close()
    
    archivo = open('texto.txt','r',encoding="utf-8") #con 'r' intenta leer el archivo, si no existe FilenotfounError
    contenido = archivo.read()
    print(f"contenido del archivo creado \n{contenido}")#Muestra el contenido del archivo creado
    archivo.close()
#print({contenido})

except Exception as e:
    print(f"Ocurrio un Error inesperado {e}")

'''