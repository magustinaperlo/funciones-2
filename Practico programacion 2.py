#paso por acá a dejar asentado que está excelente éste práctico, nada más !! 
import random
import datetime

#reciben 2 parametros:
def sumar(a, b):
    resultado = a + b
    return resultado
resultado= int(sumar(10,12))
print(resultado)

def restar(a, b):
    resultado = a - b
    return resultado
resultado=int(restar(12,10))
print(resultado)

def multiplicar(a, b, c):
    resultado = a* b * c
    return resultado
resultado= int(multiplicar(10,2,5))
print(resultado)

def dividir(a, b):
    if b == 0:
        return "Error: division por cero"
    resultado = a / b
    return resultado
resultado= int(dividir(12,6))
print(resultado)

def generar_oracion(nombre, curso):
    oracion = "Mi nombre es " + nombre + " y voy a: " + curso
    return oracion
oracion=generar_oracion("Ricardo" , "segundo")
print(oracion)


#toman un parametro y tiene uno ya definido

def calcular_costo_estadia(noches, precio_base=8500):
    costo_total = precio_base * noches
    print(f"El costo total de la estadia por {noches} noches es: {costo_total} pesos")
calcular_costo_estadia(1) 

def reservar_habitacion(noches, tipo_habitacion="Estandar"):
    print(f"Reservaste una habitacion {tipo_habitacion} por {noches} noches")
reservar_habitacion(5, "doble") 

def verificar_disponibilidad_habitaciones(cantidad_habitaciones, total_habitaciones=10):
    if cantidad_habitaciones <= total_habitaciones:
        print(f"Si tenemos disponibilidad")
    else:
        print(f"No tenemos disponible esa cantidad de habitaciones, podemos ofrecer: {total_habitaciones}")
verificar_disponibilidad_habitaciones(20)

def informacion_contacto(nombre_hotel, mensaje="Nuestro correo es abcd@hhurl.com, nustros telefonos (xxx-xxxxxx), ahora no podemos contestar comuniquese con nuestras lineas gracias, Hotel  {}"):
    print(mensaje.format(nombre_hotel))
informacion_contacto("Hurlingham") 

def calcular_tarifa_promedio(precios, divisor=3): #Esta funcion calcula la tarifa promedio por noche por persona en base triple
    tarifa_promedio =int(sum(precios) / divisor)
    print(f"La tarifa promedio por noche por persona en habitacion triple es: {tarifa_promedio} pesos")
calcular_tarifa_promedio([5300, 8000, 13000])



#funiones que no reciben parametros


def imprimir_tipo_habitaciones(): #esta funcion imprime los tipos de habitaciones de un hotel
    print("---Los tipo de habitaciones disponibles son: ")
    print("1-SINGLE")
    print("2-DOBLE")
    print("3-TRIPLE")
    print("4-CUADRUPLE")
imprimir_tipo_habitaciones()

def ladrar():#Esta funcion ladra
    print("GUAAAAUUU GUAUUUUUUUUUUUUUUU")
ladrar()

def laHora_actual():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora es: {hora_actual}")
laHora_actual()

def elDia_actual():
    dia_actual = datetime.datetime.now().strftime("%d de %B de %Y")
    print(f"Hoy es: {dia_actual}")
elDia_actual()

def randomNumeros_quiniela():
    numeros_quiniela = random.sample(range(49), 6)
    print("Los numeros de la quiniela son:")
    for numero in numeros_quiniela:
        print(numero, end=" ")
    print("")
randomNumeros_quiniela()


