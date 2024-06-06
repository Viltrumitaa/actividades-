


lista_de_numeros = []
numeros_pares =[]
numeros_impares = []
cant = int(input("cuantos numeros ingresara: "))
i=0
par = 0
impar = 0

    
   
def validar_lista_numeros(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

while i<cant:
    try:
        print ("ingrese numero", i + 1)
        num = int(input())
    
        if validar_lista_numeros(num):
         lista_de_numeros.append(num)
         i = i+1
         
        
         for x in lista_de_numeros:
             if x %2 == 0:
                 par+=1
                 numeros_pares.append(x)
                 
             else:
                 impar += 1
                 numeros_impares.append(x)
                 
             
        
    except ValueError:
        
            print("valor numero debe ser entero, ingrese la lista nuevamente    ")
            break
print(lista_de_numeros)   
print ("numeros pares: ",numeros_pares) 
print("numeros impares: ",numeros_impares)


    




