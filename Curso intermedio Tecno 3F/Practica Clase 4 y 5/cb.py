from datetime import date, datetime
from abc import ABC, abstractclassmethod


class CuentaBancaria(ABC):
    def __init__(self,nombre_titular,dni_titular, fecha_nacimiento, saldo=25000):
        self._nombre_titular = nombre_titular       #atributo privado
        self._dni_titular = dni_titular             #atributo privado
        self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y/%m/%d').date()
        self._saldo = saldo                         #atributo privado

    def obtener_saldo(self):
        return self._saldo
        
    classmethod
    @abstractclassmethod
    def depositar(self,monto):
        pass

    @classmethod
    @abstractclassmethod
    def extraer(self,monto):
        pass

    def _calcular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self._fecha_nacimiento
        return edad.days // 365
    
    def obtener_edad(self):
        return self._calcular_edad()
    
    def obtener_nombre(self):
       return self._nombre_titular
    
    def obtener_dni(self):
        return self._dni_titular
    
    