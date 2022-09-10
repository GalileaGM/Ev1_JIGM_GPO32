import random
clientes=[]
diccionario_clientes=[]

def registrocliente():
    while True:
        print('\n')
        print('*'*14)
        print('Desea un registrar un cliente: [S/N]')
        print('*'*14)
        opcliente=input('\nEscoge la opción: ')
        if (not opcliente.upper() in "SN"):
            print("Opción no válida, intenta de nuevo.")
            continue
        if (opcliente.upper()=="S"):
        
            idclientes=[f"Clave del cliente es {random.randint(1,100) } "]
            print(idclientes)
            clientes =[str(input('Nombre del cliente: '))]
        
        if (opcliente.upper()=="N"):
            print("Fin de la ejecución.")
            break
        diccionario_clientes.append({cliente:idclientes for cliente in clientes})
        print(diccionario_clientes)
        
        
print('*'*14)
print('MENU DE OPCIONES')
print('*'*14)
print('[A]. Registrar cliente')
print('[B]. Registrar sala ')
print('[C]. Registrar reservacion' )
print('[D]. Editar nombre del evento')
print('[E]. Consulta de reservaciones')
print('[F]. SALIR')

while True:
    
    opmenu=input('\nEscoge la opción: ')
    
    if (not opmenu.upper() in "ABCDEF"):
        print("Opción no válida, intenta de nuevo.")
        continue
    
    #OPCION=SALIR
    if (opmenu.upper()=="F"):
        print("Fin de la ejecución.")
        break
 
    #OPCION=REGISTRAR CLIENTE
    if (opmenu.upper()=="A"):
        registrocliente()