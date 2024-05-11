###deuda de tarjeta###



while True:
  
  print("1.-realizar pago del cup de la tarjeta")
  print("2.-nueva compra")
  print("3.-salir")
  opc = int(input("ingrese opcion   "))
  if opc >0 and opc <4:
    if opc == 1:
        deuda = 100.000
        monto = (float(input("ingrese monto a pagar ")))
        if monto >= 0 and monto <= 100.000:
         deuda = deuda - monto
         print("su deuda queda en ",deuda)
         
    else:
      if opc == 2:
        for compra in range:
          monto = float(input("ingrese valor de la compra "))
          deuda = deuda + monto
          print("su saldo es:  ",deuda)

         


   
   
    
      
   
