class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor, marca, modelo):
        self.motor = motor
        self.marca = marca
        self.modelo = modelo

motor_gasolina = Motor("Gasolina", 150)

carro_gasolina = Carro(motor_gasolina, "Toyota", "Corolla")

print(f"Carro: {carro_gasolina.marca} {carro_gasolina.modelo}")
print(f"Motor: Tipo: {carro_gasolina.motor.tipo}, Potência: {carro_gasolina.motor.potencia} cavalos")
