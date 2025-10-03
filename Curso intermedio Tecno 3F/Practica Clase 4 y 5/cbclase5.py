class CuentaBancaria:
    def __init__(self, nombre_titular, dni_titular, fecha_nac, saldo = 0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nac = fecha_nac
        self._saldo = saldo

    def get_name(self):
        print(self._nombre_titular)
    
    def set_name(self,nombre):
        self._nombre_titular = nombre
    
    def get_saldo(self):
        print(self._saldo)
