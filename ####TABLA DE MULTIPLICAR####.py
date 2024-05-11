#######EJERCICIOS PYTHON##############

####TABLA DE MULTIPLICAR####


num = int(input("ingrese numero positivo:    "))


if num >0:
 print(num,"* 1 = \t",num*1)
 print(num,"* 2 = \t",num*2)
 print(num,"* 3 = \t",num*3)
 print(num,"* 4 = \t",num*4)
 print(num,"* 5 = \t",num*5)
 print(num,"* 6 = \t",num*6)
 print(num,"* 7 = \t",num*7)
 print(num,"* 8 = \t",num*8)
 print(num,"* 9 = \t",num*9)
 print(num,"* 10 = \t",num*10)
else:
 print ("numero es menor que cero")

####suma###

num1 = int(input("ingrese primer numero:\t"))
num2 = int(input("ingrese segundo numero:\t"))

if num1 >0:
 print(num1,"+",num2,"=",num1+num2)
else:
 print ("numero positivo")

######par o impar#############


a = int(input("ingrese primer numero:\t"))

if num>1 and num< 101:
 if num%2 == 0: #num mod(modulo o resto) 2 = 0
  print("es par")
 else:
  print("es impar")
else:
 print("el numero esta fuera del rango debe estar enre 1 y 101")

######MENORES A CERO######

b =int(input("Ingrese un numero:\t"))
c= int(input("ingrese segundo numero positivo:\t"))
d= int(input(" ingrese tercer numero:\t"))

cont = 0

if b<0:
 print("es menor a cero")
 cont = cont + 1
else:
 if b>0:
  print("es mayor")
 else:
  if c <0:
   print("es menor a 0")
   cont= cont+1
  else:
   if c>0:
    print(" es mayor que 0")
   else:
    if d<0:
     print("es menor a 0")
     cont = cont +1
    else:
     if c>0:
      print("es mayor a 0")


#########TIPO DE TRIANGULO#############    
e = int(input("ingrese mediada de un lado\t"))
f = int(input("ingrese medidas del siguiente lado\t"))
g = int(input(" ingrese medida del siguiente lado\t"))

if e == f and f == g:
 print (" es un triangulo equilatero")
else:
 if e==f and g != e:
  print("es un triangulo isosceles")
 else:
  if e != f and f != g:
   print("es un triangulo escaleno")


#######ZAPATERIA############

zapatos = 20000
cantzapatos = int(input("ingrese cantidad de zapatos"))

if cantzapatos >= 2:
 print("el envio es gratis")
 cantzapatos = cantzapatos * zapatos
 print("su total es:\t",cantzapatos)
else:
 if cantzapatos < 2:
  print("debe cancelar un monto extra de 30000 ")
  cantzapatos = zapatos - 3000
  print("su total es:\t", cantzapatos)


##############-DELIVERY DE SANDWICHES -##################  



   



 







 






