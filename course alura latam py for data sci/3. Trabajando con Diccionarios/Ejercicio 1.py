'''El diccionario de abajo es un ejemplo de diccionario anidado'''

dataset = {
    'Lamborghini' : {
        'motor' : 'Motor V12',
        'año' : 2018,
        'km' : 25400,
        'accesorios' : ['Llantas de aleación', 'Cambio automatico', 'Cerraduras electricas'],
        'valor' : 133529.84
    },
    'Dodge' : {
        'motor' : 'Motor 6.7',
        'año' : 2017,
        'km' : 45757,
        'accesorios' : ['Llantas de aleacion', '4 x 4', 'Central multimedia'],
        'valor' : 926121
    },
    'Pajero' : {
        'motor' : 'Motor 2.4 Turbo',
        'Cero_km' : True,
        'km' : 80000,
        'accesorios' : ['Control de traccion', 'Bancos de cuero', 'Control de estabilidad'],
        'valor' : 51606.59
    }
}

# Seleccionar el diccionario que contiene datos del vehiculo 'Dodge'.
dataset['Dodge']
print(dataset['Dodge']) # Mostrar

# Seleccione solamente accesorios del vehiculo 'Dodge'.
dataset['Dodge']['accesorios']
print(dataset['Dodge']['accesorios']) 

# Verificar si el diccionario de datos del vehiculo 'Pajero' posee la clave 'año'.
print('año' in dataset['Pajero'])

# Agregar clave año al diccionario de datos del vehiculo 'Pajero' con el valor de 2012. Visualice el diccionario nuevamente.
dataset['Pajero']['año'] = 2012
print(dataset)

# Eliminar clave Cero_km del diccionario de datos del vehiculo Pajero para mantener la compatibilidad con las informaciones de los demas vehiculos. Visualizar contenido.
del dataset['Pajero']['Cero_km']
print(dataset)

# Agregar un nuevo item al diccionario dataset. Abajo tenemos las informaciones para el vehiculo Ford Edge. Utilizar dict y zip.
'''
claves = ['motor', 'año', 'km', 'accesorios', 'valor']
valores = ['Motor Diesel v6', 2002, 128590, 'Sensor crepuscular', 'Sensor de lluvia', 'Aire Acondicionado'], 71647.59
'''

claves = ['motor', 'año', 'km', 'accesorios', 'valor']
valores = ['Motor Diesel v6', 2002, 128590, 'Sensor crepuscular', 'Sensor de lluvia', 'Aire Acondicionado'], 71647.59

dataset['Ford Edge'] = dict(zip(claves, valores))
print(dataset)
