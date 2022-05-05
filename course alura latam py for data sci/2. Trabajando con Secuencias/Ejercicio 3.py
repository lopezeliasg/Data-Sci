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

# Obtener los códigos que tienen como resultado el siguiente conjunto de selecciones en la secuencia 'carros'.
'''
1. 2002
2. ['Vidrios electricos', 'Piloto automatico', 'Techo panoramico', 'Aire acondicionado']
3. 'Cambio automatico'
4. ['Panel digital', 'Central multimedia']
'''
carros = carro_1, carro_2, carro_3
print(carros)

#1
print(carros[-1][2])
#2
print(carros[0][-2])
#3
print(carros[1][-2][-1])
#4
print(carros[1][-2][1:3])
