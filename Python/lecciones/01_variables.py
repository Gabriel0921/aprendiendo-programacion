# =================================
# LECCION 01 - VARIABLES
# =================================

# Datos personales
nombre = "Gabriel"
edad = 30
estatura = 1.75
es_estudiante = True
ciudad = "Lorica"
profesion = "Desarrollador"
hobby = "Aprender cosas nuevas"
lenguaje = "A un es muy pronto para saberlo"
horas_estudio = 2 

# Mostrar informacion
print("Hola, mundo!")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿Soy estudiante?", es_estudiante)
print("Mi ciudad es" , ciudad)
print("Mi profesion es" , profesion)
print("Mi hobby es" , hobby)
print("Mi lenguaje de programacion favorito es" , lenguaje)
print("Mis horas de estudio son" , horas_estudio)

# Mostrar tipos de datos
print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(es_estudiante))

print("\n=== NUEVO EJERCICIO ===")

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿En qué ciudad vives? ")

edad_futura = edad + 1

print("\n=== MIS DATOS ===")
print("Nombre:", nombre)
print("Edad actual:", edad)
print("Ciudad:", ciudad)
print("Edad el próximo año:", edad_futura)
