class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado {monto}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")
    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Has retirado {monto}. Saldo actual: {self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser mayor a 0.")
    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}")
cuenta1 = CuentaBancaria("Andres", 1000000)
cuenta1.consultar_saldo()      
cuenta1.depositar(50000)        
cuenta1.retirar(20000)           
cuenta1.retirar(2000000)          
cuenta1.consultar_saldo()      