carros	= ['Lamborghini', 'Versa', '207 Sedan', 'Dodge Charger', 'Aston Martin', 'Pajero TR4',
	'Tiggo', 'Kangoo Express', 'Mohave', 'Livina',	'207 SW', 'Palio Adventure', 'Tucson', 'Doblò',
    '500 Abarth', 'Jetta Variant', 'Range Rover Evoque', 'Up!',	'Grand Cherokee', 'HB20', 'Boxer',
    'NX 200t', 'Bongo', 'RAM', 'Parati', 'Tiida Hatch',	'CR-V',	'Boxster', 'Golf', '308 CC', 'Fox',
    'Z4 Roadster', 'Sandero', 'Polo Sedan',	'Veloster', 'Cadillac',	'Ford Edge', 'Discovery 4', 'EcoSport',
    'Hilux', 'Logan', 'Gol G4', 'Sorento', 'Santa Fe', 'Vantage Volante', 'Xsara Picasso', 'Volkswagen',	
    'Crossfox',	'Touareg', 'Gallardo LP	560-4',	'Optima', 'Jumper',	'Uno', 'J3', 'Edge', 'C3 Picasso',	
    'Voyage', 'Cayenne', 'Passat', 'Sonata', 'Aircross', 'Linea', 'Veracruz', 'Fit', 'Idea', 'A3', 'SpaceFox',
    'New Fiesta', 'DS5',	'Ford EcoSport', 'Jeep Renegade', 'Accord']

# Declarar un dic sin contenido y llamarlo nombres_carros.

nombres_carros = {}

# Construir un bucle for para leer cada item de la lista carros, dentro del bucle crear una variable llamada primera_letra y dentro de ella almcenar la primera letra del nombre de cada vehiculo.

for item in carros:
    primera_letra = item[0]
    print(primera_letra)

# Obtener diccionario, donde las claves sean las iniciales de los nombres de los vehiculos y los valores una lista con los nombres de todos los vehiculos iniciados por la letra.

    if (primera_letra in nombres_carros):
        nombres_carros[primera_letra].append(item)
    else:
        nombres_carros[primera_letra] = [item]
print(nombres_carros)

#print([item for item in nombres_carros if primera_letra in nombres_carros])
#print([item if primera_letra in nombres_carros else nombres_carros[primera_letra] for item in nombres_carros])