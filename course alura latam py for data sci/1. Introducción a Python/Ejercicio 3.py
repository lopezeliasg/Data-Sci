# Indicar al usuario Indice de Masa Corporal (IMC).

print("-- Vamos averiguar tu IMC --")

kg = input("Introduce tu peso en kilos: ")
altura = input("Introduce tu altura en metros: ")

imc = float(kg) / (float(altura)**2)

print(f"Tu IMC es de: {imc}")
print("* * Recuerda qué: si tu IMC es entre 18.5 y 24.9, se encuentra dentro del rango de peso normal o saludable. * *" )