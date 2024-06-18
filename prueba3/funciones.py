
cilindro5 = ["cil.15kg"]
cilindro15=["cil.15kg"]
cilindro45= ["cil.45kg"]


cont5=0
cont15=0
cont45 = 0


def registrar_pedido(cliente):
  
    nombre = input("Ingrese nombre y apellido: ")
    if nombre == "":
       print("ingrese nuevamente:")
       nombre = input("Ingrese nombre y apellido: ")
    comuna = input("Ingrese comuna: ")
    if comuna == "":
       print("ingrese nuevamente")
       comuna = input("Ingrese comuna: ")
       
    cant= ("cuantos cilindros llevara?")
    for cilindro  in cilindro:
      cilindro = input("Ingrese el cilindro que llebara(Cil.5kg,Cil.15kg,Cil.45kg)").lower
      if cilindro == "Cil.5kg":
         cont5 = cont5 + 1
         cilindro5_ = cilindro + cont5
         cilindro.append(cilindro5)
            
            
      elif cilindro == "cil.15kg" :
           cont15 = cont15 + 1
           cilindro15_= cilindro + cont15
           cilindro.append(cilindro15)

      elif  cilindro =="cil.45kg":
            cont45 = cont45 + 1
            cilindro45_= cont45 + 1
            cilindro.append(cilindro45)

    cliente = [{
                "Nombre" : nombre,
                "Comuna" : comuna,
                "Cil.5" : cilindro5_,
                "Cil.15" : cilindro15_,
                "CIL.45" : cilindro45_
            
               }]
               

            

        

      








def lista_pedidos(cliente):
    print (f/{"Nombre y apellido": "Nombre"})#/n no logre hacer la barra al otro lado
    print (f/{"Comuna": "Comuna"})#/n no logre hacer la barra al otro lado
    print (f/{"CIL.5kg": "Cil.5"})#/n no logre hacer la barra al otro lado
    print (f/{"CIL.15KG": "Cil.15"})#/n no logre hacer la barra al otro lado
    print (f/{"CIL.45KG": " Cil.45"})#/n no logre hacer la barra al otro lado
   

def imprimir_ruta (cliente):
  print()   