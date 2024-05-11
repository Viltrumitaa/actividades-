######sistema de compras#########
 
print("BIENVENIDO")
print("1.-AGUA")
print("2.-AZUCAR")
print("3.-ACEITE")
print("4.-ARROZ")
print("5.-FIDEOS")
print("6.-BEBIDA")
print("7.-CHOCOLATE")
print("8.-PAN DE MOLDE")

respuesta = int(input(" que desea llevar?   "))
cuenta = 0

if respuesta == 1:
   cantagua = int(input("ingrese cantidad de agua:  "))
   cuenta = cantagua * 600
else:
   if respuesta == 2:
      cantazucar = int(input("ingrese cantidad de azucar:   "))
      cuenta = cantazucar * 1200
   else:
      if respuesta == 3:
        cantaceite =  int(input("ingrese cantidad de aceite:    "))
        cuenta = cantaceite * 1500
      else:
         if respuesta == 4:
            cantarroz = int(input("ingrese cantidad de arroz:   "))
            cuenta = cantarroz * 1250
         else:
            if respuesta == 5:
               cantfideos = int(input("ingrese cantidad de fideos:  "))
               cuenta = cantfideos * 790
            else:
               if respuesta == 6 :
                  cantbebida= int(input(" ingrese cantidad de bebida:    "))
                  cuenta = cantbebida * 1780
               else:
                  if respuesta == 7:
                     cantchocolate = int(input("ingrese cantidad de chocolates: "))
                     cuenta = cantchocolate * 2500
                  else:
                    if respuesta == 8:
                       cantpanmolde = int(input("ingrese cantidad de pan molde: ")) 
                       cuenta = cantpanmolde * 1340



cliente = input("usted es preferencial?si/no ")                       
if cliente == "si":
    print ("felicidades!! por ser preferencial tiene un descuento del 25%")
    cuenta = cuenta*0.75
    print("su total es:  ",cuenta)
else:
   if cliente == "no":
      print("su total es:   ",cuenta)


efectivo = int(input("ingrese efectivo:  "))


if efectivo >= cuenta:
  print("su vuelto es: ",efectivo-cuenta)
else:
 if efectivo < cuenta:
    print("DINERO INSUFICIENTE, GUARDIAS¡¡¡¡")


