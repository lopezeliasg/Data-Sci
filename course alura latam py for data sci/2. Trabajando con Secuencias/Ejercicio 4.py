'''
Orden:
- Nombre del vehiculo
- Motor
- Año de fabricacion
- Kilometraje
- ¿Es cero km? (booleano)
- Accesorios
- Valor de mercado
'''
carro_1 = ['Dodge Jorney', 'Motor 3.0 32v', 2010, 99197, False, ['Vidrios Electricos', 'Piloto automatico', 'Techo panoramico', 'Aire Acondicionado'], 120716.27]
carro_2 = ['Carens', 'Motor 5.0 vv8 Bi-Turbo', 2011, 37978, False, ['Aire Acondicionado', 'Panel digital', 'Central multimedia', 'Cambio Automatico'], 76566.49]
carro_3 = ['Ford Edge', 'Motor Diesel V6', 2002, 12859, False, ['Sensor crepuscular', 'Llantas de aleacion', 'Techo panoramico', 'Sensor de lluvia'], 71647.59]

# Obtener sumatoria de los valores de mercado de los tres vehiculos de la secuencia 'carros'.

carros = carro_1, carro_2, carro_3
print(carros)

# Sumatoria
print(carros[0][-1] + carros[1][-1] + carros[2][-1])
