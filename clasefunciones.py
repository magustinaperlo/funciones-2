import random
import datetime
numeroRandom=0

def suma(num1, num2): # funcion para sumar dos numeros
    return num1 + num2
resultado = suma(1,3)
print(resultado)  

def noticia_del_dia(noticia): # funcion que comunica la noticia del dia
    print(noticia)
noticia=("Sonia y su enojo porque no le sale estudiar programacion")
print(noticia)

def multiplicacion(num1, num2, num3): # funcion para multiplicar 3 números
    return num1 * num2 * num3
resultado_multiplicacion= multiplicacion(4,9,7)
print(resultado_multiplicacion)

def nombre_curso(nombre,curso): # funcion que dice nombre del alumno y curso
    print(nombre,curso)
nombre=("ALVARO ")
curso=("2")
print("Mi nombre es " + (nombre) + "y voy a " + (curso))


def multiplicacionAleatoria(num1, numeroRandom):#Hace una multiplicacion con un numero definido y otro random
    numeroRandom=random.randint (1,100)
    return num1 * numeroRandom
resultadoRandom= multiplicacionAleatoria(7,(numeroRandom))
print(resultadoRandom)


def hora():
    horario = datetime.datetime.now()
    horario = horario.strftime()
print