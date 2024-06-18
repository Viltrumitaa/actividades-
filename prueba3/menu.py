

import funciones as fn

cliente = []

while True:
    print("Menu")
    print("1.-Registrar pedido")
    print("2.-listar los pedidos")
    print("3.-Imprimir hoja de ruta")
    print("4.-Salir")

    opc = int(input("Ingres opcion: "))

    if opc ==1:
        fn.registrar_pedido(cliente)
    elif opc ==2:
        fn.lista_pedidos(cliente)
    elif opc== 3:
       fn.imprimir_ruta (cliente)
    elif opc == 4:
        print("Saliendo...")
        break
    else:
        print("Ingrese opcion valida, del 1-4")