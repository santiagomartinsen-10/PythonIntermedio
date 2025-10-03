from cb import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=3800,limite_extraccion = 1800):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def extraer(self, monto):
        
        if monto <= self.obtener_saldo() and monto <= self._limite_extraccion:
            self._saldo -= monto
            print(f"Extracción exitosa. ${monto} Nuevo saldo: {self._saldo}")
            #super().extraer(monto) le saque el super por que me daba error
            
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")
    
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito de ${monto} exitoso. Nuevo saldo: {self._saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def ver_limite_ext(self):
        print(f'tu limite de extracion es de: ${self._limite_extraccion}')