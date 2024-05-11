#####venta de pasajes#########

entradas = int(input("cantidad de entradas que vendera: "))
totalingreso =0


for precioentradas in range (entradas):
    precioentradas = int(input("ingrese valor de entrada:   "))
    totalingreso =  entradas * precioentradas
    if precioentradas  <=0:
        print("valor invalido")
        break

print("total de ingresos fue:   ",totalingreso)



#######VENTA DE PASAJES CON WHILE#####################
entradas = float(input("cantidad de entras que vendera: "))




