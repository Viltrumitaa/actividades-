#######sandwiches####
 

print("menu\n")
print("1.-churrasco")
print("2.-completo")
print("3.-vegetariano")
print("4.-barrosluco")


resp = int(input("ingrese la opcion"))

cuenta  = 0

if resp == 1: 
    churrascos= int(input("ingrese cantidad de churrascos"))
    cuenta = churrascos * 1500
else:
    if resp ==2:
        completos= int(input("ingrese cantidad de completos"))
        cuenta = completos * 1000
    else:
        if resp >=3:
            vegetarianos= int(input("ingrese cantidad de vegetarianos"))
            cuenta = vegetarianos * 2000
        else:
            if resp>=4:
                barrosluco= int(input("ingrese cantidad de barrosluco"))
                cuenta = barrosluco * 3000


descuento = input(" pose algun descuento?(si/no)   ")

if descuento == "no":
    print("el total de venta es de :",cuenta)
else: 
    if descuento == "si":
        cuenta = cuenta * 0.90

        print(" su total con el descuento es:",cuenta)


########CORONAVIRUS#################

cantmascarillas = int(input("cuantas mascarillas va a llevar?   "))
mascarillas = 500


if cantmascarillas >= 30:
    cuenta = mascarillas * cantmascarillas
    print("el envio es gratis, el total es: ",cuenta)
else:
    envio = input("usted es de esta misma comuna o de una comuna aledaña o otro sector"   )
    if envio == "misma comuna":
        cuenta = mascarillas * cantmascarillas + 1000
    else:
        if envio == "comuna aledaña":
            cuenta = mascarillas * cantmascarillas + 2000
        else:
            if envio == "otro sector":
                cuenta = mascarillas * cantmascarillas + 300

print("su total con el envio es : ",cuenta)








    





