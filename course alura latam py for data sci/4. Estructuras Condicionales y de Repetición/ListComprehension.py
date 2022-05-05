# Seleccionar Letras
letras = []
for letra in 'Data Science':
    letras.append(letra)
print(letras)

print("listcomprehension: ", [letra for letra in 'Data Science'])

# Par o Impar
lista = []
for i in range(10):
    if (i % 2 == 0):
        lista.append(2 ** i)
    else:
        lista.append(3 ** i)
print(lista)

print("listcomprehension: ", [2 ** i if (i % 2 == 0) else (3 ** i) for i in range(10)])

# Estirando listas
listas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
secuencia = []
for lista in listas:
    for item in lista:
        secuencia.append(item)
print(secuencia)

print("listcomprehension: ", [item for lista in listas for item in lista])

# Haciendo Consultas

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
    'DS5' : {
        'motor' : 'Motor 2.4 Turbo',
        'año' : 2012,
        'km' : 80000,
        'accesorios' : ['Control de tracción', 'Bancos de cuero', 'Control de estabilidad'],
        'valor' : 51606.59
    }
}

consulta = []
for clave, valor in dataset.items():
    if (clave[0] == 'D'):
        for item in valor['accesorios']:
            consulta.append(item)
print(consulta)

print("listcomprehension: ", [item for clave, valor in dataset.items() if (clave[0] == 'D') for item in valor['accesorios']])