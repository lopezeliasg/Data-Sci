dataset = {
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

# Copiar dataset y llamarlo dataset_copia.
dataset_copia = dataset.copy()

# Utilizar dataset_copia y agregar Airbag a los accesorios del vehiculo Dodge.
dataset_copia['Dodge']['accesorios'].append('Airbag')
print(dataset_copia)

# Utilizando get, vizualizar accesorios del vehiculo Dodge de los diccionarios dataset y dataset_copia.
print("Esto es 'dataset' :", dataset['Dodge'].get('accesorios', 'Clave no encontrada'))
print("Esto es 'dataset_copia' : ", dataset_copia['Dodge'].get('accesorios', 'Clave no encontrada'))

# Actualizar diccionarios de informaciones de los vehiculos Dodge y Pajero. Para el vehiculo Dodge el año debe ser alteradao para 2016 y para el vehiculo Pajero el motor debe ser alterado para Motor Diesel V8. Utilizar metodo update().
dataset['Dodge'].update({'año' : 2016})
dataset['Pajero'].update({'motor' : 'Motor Diesel V8'})
print(dataset)