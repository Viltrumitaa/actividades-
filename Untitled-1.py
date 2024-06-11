


asientos_normales = 78900
asientos_vip = 240000
compra = 0


#todos disponibles
asientos_disponibles = {asiento for asiento in range(1, 43)}

def mostrar_asientos():
    print("Asientos disponibles (X = ocupado):")
    for i in range(1, 43):
       
        if [asientos_disponibles] == "ocupado":
            print("x")
        else:
            print(i, end=" ")
        
        # Saltar línea después de cada 6 asientos
        if i % 6 == 0:
            print()
        
        # Separación de secciones normales y VIP, si el numero es 30 imprime una linea de guiones x 20
        if i == 30:
            print("-" * 20)

asientos= {
    "normal" : {i: "disponible" for i in range(1,31)},
    "vip" : {i:"disponible" for i in range(31,43)}
}

def seleccion_de_asientos():
    try:
        mostrar_asientos()
        asientousuario= int(input("seleccione el asiento que desea comprar:   "))
        if asientousuario <=31 and asientousuario >= 1:
                asientousuario = "normal"
                compra = asientos_normales
                
        elif asientousuario <=43 and asientousuario>=32:
            compra = asientos_vip
            asientousuario = "vip"
        else:
            print("valor ingresado fuera del rango")
            return
            
                    
        print("Usted compro un asiento ",asientousuario,"con un valor de: ",compra)
        resp2= input("Confirme su compra (si/no)").lower()

        if resp2 == "si":
            
           asientos[asientousuario]= "ocupado"
           print("asiento reservado")

           datos_usuario = "nombrePasajero,nombrePasajero,rutPasajero, telefonoPasajero,bancoPasajero" #lo que debe ir 

 

           #intente con esto tmbn 
           # if asientousuario = "normal":
           #    asientos ["normal"][asientousuario]== "ocupado"  #---> si el asiento es normal, el asiento de usuario se marca como ocupado dentro del la seccion normal del diccionario asientos xd 
           #     print("asiento reservado")
           # elif asientousuario == "vip":
           #     asientos ["vip"][asientousuario]== "ocupado"#--> 
           #     print("asiento reservado") 
                
        else:
            print("su compra no fue confirmada")
            return


    except:
        print("ingrese valor numerico dentro del rango")


while True:
   try:
    print("1.-asientos disponibles")      
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    opc= int(input("ingrese opcion: "))
    if opc == 1:
        mostrar_asientos()
    elif opc ==2:
        seleccion_de_asientos()
   except:
       print("ingres opcion del 1-5")

        


