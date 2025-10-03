from ca import CuentaAhorro
from cc import CuentaCorriente
from cb import CuentaBancaria

print("\t")

#esta es la cuenta del ejercicio, Obtengo la Edad Dni el saldo, deposito, extraigo dinero, calculo interes y vuelvo a mostrar el saldo
ahorro = CuentaAhorro("Ana García", "12345678", "1990/01/15",50000)


print("---------Cuenta Ahorro-----------")
print(f'cuenta de {ahorro.obtener_nombre()}')
print(f'Edad: {ahorro.obtener_edad()} años')
print(f'numero de DNI: {ahorro.obtener_dni()}')
print("\t")
ahorro.obtener_saldo()
print("\t")
print("\t")
ahorro.depositar(1864)
print("\t")
print("\t")
ahorro.extraer(180)
print("\t")
print("\t")
ahorro.obtener_saldo()
print("\t")
ahorro.obtener_saldo()
print("\t")
print("\t")


#Trabajando con la CuentaCorriente para hacer pruebas
#En esta cuenta no aplica intereses, solo en la de Cuenta Ahorro
print("---------Cuenta Corriente-----------")
ahorrocc = CuentaCorriente("Santiago","48156198","1950/02/28",45000,4000)
print(f'Saldo actual {ahorrocc.obtener_saldo()}')
ahorrocc.depositar(1800)
print(f'Saldo actual {ahorrocc.obtener_saldo()}')
ahorrocc.ver_limite_ext()
ahorrocc.extraer(10000)
ahorrocc.extraer(500)
print(f'Saldo actual {ahorrocc.obtener_saldo()}')
