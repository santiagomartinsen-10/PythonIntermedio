from ca import CuentaAhorro
from cc import CuentaCorriente
from cb import CuentaBancaria



def menu_interaccion(cuenta):
        
       
        print("\n--- ¡Bienvenido! ---")
    
        while True:
            #Mostrar las opciones del menu
            print("\nSeleccione una operación:")
            print(" [1] Depositar")
            print(" [2] Extraer")
            print(" [3] Ver Saldo")
            print(" [4] Salir")
        
        #capturo la opcion que elije el usuarios
            opcion = input("Ingrese el número de la opción (1-4): ")
        
        #Procesar la elección del usuario
            if opcion == '1':
                #Depositar
                try:
                    monto = float(input("Ingrese el monto a depositar: "))
                    cuenta.depositar(monto)
                except ValueError:
                    print("Error: Por favor, ingrese un número válido para el monto.")
                
            elif opcion == '2':
                #Extraer
                try:
                    monto = float(input("Ingrese el monto a extraer: "))
                    cuenta.extraer(monto)
                except ValueError:
                    print("Error: Por favor, ingrese un número válido para el monto.")
                
            elif opcion == '3':
                #Ver Saldo
                cuenta.obtener_saldo()
                #print("Su saldo fue actualizado con el 0,001 de interes")   Este era otro mensaje pero queda muy repetitivo
            elif opcion == '4':
                #Salir
                print("\n Gracias!!")
                break
            
            else:
                # Manejo de opción inválida
                print(" Opción inválida. Por favor, intente de nuevo con 1, 2, 3 o 4.")

if __name__== "__main__":

    #Crea la instancia de la CuentaAhorro con los datos y saldo inicial
    
    micuenta = CuentaAhorro("Santiago", "1234567890", "1990/06/10",1000)#el saldo lo tomo del importe que le asigne en Cuenta Ahorro $85000

    #Llamar al menú y pasarle la cuenta

menu_interaccion(micuenta)