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

carros = [carro_1, carro_2, carro_3]

# Seleccionar la lista de acccesorios de cada vehiculo y crea una nueva lista con la concatenacion de los accesorios de los tres vehiculos. Llame esta lista de accesorios.
print(carros)
accesorios = carros[0][-2] + carros[1][-2] + carros[2][-2]
print(accesorios)

# Colocar los items de la lista creada arriba en orden alfabetica.
accesorios.sort()
print(f"Ordenado: {accesorios}")

# Note que los items 'Aire Acondicionado' y 'Techo panoramico' estan duplicados en nuestra lista accesorios. Elimina el item 'Aire Acondicionado'.
accesorios.remove('Aire Acondicionado')
print(accesorios) 

# Elimine el item 'Techo panoramico' con el uso del metodo pop.
accesorios.pop(-2)
print(accesorios)

# Agrega el item 'Bancos de cuero' en nuestraa lista de accesorios en la segunda posicion.
accesorios.insert(1, 'Bancos de cuero')
print(accesorios)

# Agregue al final de la lista de accesorios el item 'Camara de estacionamiento'.
accesorios.append('Camara de estacionamiento')
print(accesorios)