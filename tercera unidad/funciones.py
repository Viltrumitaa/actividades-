#funciones
#existen 4 tipos de funciones 
#1- sin argumentos ()y sin retorno
#2.- sin argumentos () y con retorno (return)
#3- con argumentos (x) y sin retorno 
#4.- con argumentos(x) y sin retornos (return)


#1
def saludo():
    print ("hola")


#2
def saludo2():
    return "hola como estan"

#3
def sumar (num1,num2)
    suma = num1 + num2
    print (suma)

#4
def restar (valor1, valor2):
    resta = valor1 - valor2
    return resta


#como llamamos a las funciones#
saludo()
print(saludo2())

num1 = int(input("ingrese el numero 1: "))
num2 = int(input("ingrese el numero 2: "))
sumar(num1,num2)
resta = restar (num1,num2)
print (resta)