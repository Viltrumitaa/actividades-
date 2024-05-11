#menu otaku#
pikachuroll = 4500
otakuroll = 5000
pulpovenenoso = 5200
anguilaelectrica = 4800

#####
contpikachu = 0
total = 0
contotaku = 0
contpulpo = 0
contanguila = 0
desc = 0

while True:
    try:
        print("*********************")
        print("MENU")
        print("1.-pikachu roll ($4500)")
        print("2.-otaku roll ($5000)")
        print("3.-pulpo venenoso roll ($5200")
        print("4.-anguila electrica roll ($4800)")
        print("5.-terminar pedido")
       
        opc=int(input("agregue una orden"))


        if opc == 1:
           contpikachu += 1
           total += pikachuroll
        elif opc ==2:
            contotaku += 1
            total += otakuroll
        elif opc == 3:
            contpulpo += 1
            total += pulpovenenoso
        elif opc ==4:
            contanguila += 1
            total += anguilaelectrica
        elif opc == 5:
            break
    except ValueError: 
        print("ingrese opcion valida del 1 al 5")

respuestadecuento = input("tiene codigo de descuento? si/no").lower()
if respuestadecuento == "si":
    while True:
        codigo = input("ingrese codigo")
        if codigo == "soy otaku":
            desc = total * 0.1
            break
        else:
            print("codigo no valido")
            print("desea reingresar presione x").lower()
            respx = input().lower()
            if respx == "si":
             break
else: 
  desc = 0


totalapagar = total -desc
suma = contotaku+ contpulpo+contanguila+contpikachu
print("************************************")
print("Total productos: ",suma)
print("************************************")
print("pikachu roll",contpikachu)
print("otaku roll",contotaku)
print("pulpo venenoso roll",contpulpo)
print("anguila electrica roll",contanguila)
print("************************************")
print("subtotal a pagar:",total)
print ("descuento por codigo:",desc)
print("total:",totalapagar)

resp= input("¿desea volver a comprar?si/no").lower()




