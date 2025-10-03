from cc import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento,saldo):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = 0.001
        
    
    def aplicar_interes(self):

        """Calcula y aplica el interés al saldo."""
        interes = self._tasa_interes #0.001
        self._saldo += interes #le sumo 0.001 al saldo
        print(f"Interés calculado y aplicado,se suma ({self._tasa_interes}%): Nuevo saldo: {self._saldo:.3f}")
        #return interes
    
    def obtener_saldo(self):
        """Obtiene el saldo y aplica el interés primero."""
        # Se aplica el interés antes de mostrar el saldo
        print("--- Aplicando interés antes de mostrar el saldo ---")
        self.aplicar_interes()
        #return self._saldo
    
    def extraer(self, monto):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            print(f"Extracción de ${monto} exitosa. Nuevo saldo:{self._saldo:.3f}") 
            #print("--- Aplicando interés por la operación ---")
            self.aplicar_interes()

        else:
            print("Monto inválido o saldo insuficiente.")  
        
    
    def depositar(self,monto):
        
        # Lógica mínima para depositar en cualquier cuenta
        if monto > 0:
            self._saldo += monto
            print(f"Depósito de ${monto} exitoso. Nuevo saldo: {self._saldo:.3f}")
            self.aplicar_interes()
        else:
            print("El monto a depositar debe ser positivo.")

        
    