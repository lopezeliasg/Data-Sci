dataset = {
    'Lamborghini' : {
        'motor' : 'Motor V12',
        'año' : 2018,
        'km' : 25400,
        'accesorios' : ['Llantas de aleación', 'Cambio Automático', 'Cerraduras electricas', 'Bancos de cuero'],
        'valor' : 133529.84
    },
    'Dodge' : {
        'motor' : 'Motor 6.7',
        'año' : 2017,
        'km' : 45757,
        'accesorios' : ['Llantas de aleación', '4 x 4', 'Central multimedia', 'Cambio Automático'],
        'valor' : 926121
    },
    'Pajero' : {
        'motor' : 'Motor 2.4 Turbo',
        'Cero_km' : True,
        'km' : 80000,
        'accesorios' : ['Control de tracción', 'Bancos de cuero', 'Cambio Automático', 'Control de estabilidad', '4 x 4'],
        'valor' : 51606.59
    }
}

# Crear un bucle for para imprimir informaciones de los tres vehiculos del dataset.
for (valor) in dataset.values():
    print(valor)

# Imprimir las listas de accesorios de cada vehiculo.
for (valor) in dataset.values():
    print(valor['accesorios'])

# Crear una lista llamada accesorios y almacenar en ella todos los accesorios de los tres vehiculos.
accesorios = []
for (valor) in dataset.values():
    for item in valor['accesorios']:
        accesorios.append(item)
print(accesorios)

# Crear una nueva lista accesorios sin los items repetidos.
accesorios = list(set(accesorios))
print(accesorios)

