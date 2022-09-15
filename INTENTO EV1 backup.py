import random
import datetime
#registrocliente
clientes=[]
diccionario_clientes=[]
idcheck=''
#registrosala
salas=[]
cupo_sala=0
diccionario_salas=[]
#registroreservacion
diccionario_reservacion=[]
listafechas=[]
fecha=[]
lista_datos=[]
#editarnombre
tempList=[]
idlist=[]
#consulta
datos=[]


def registrocliente():
    while True:
        idclientes=(random.randint(1,100))                                              #crea id aleatorio *limite de ids en 5 para probar que no repitan
        idcheck=' '.join(str(diccionario_clientes))                                     #convierte diccionario en str para checar si hay dobles
        if str(idclientes) not in idcheck:                                              #si no hay dobles en el str del directorio, sale del While loop
            break
    print('Clave del cliente es ', idclientes)
    clientes =[str(input('Nombre del cliente: '))]
    diccionario_clientes.append({idclientes:cliente for cliente in clientes})
    print(diccionario_clientes)

def registrosala():
    while True:                                                                         #crea el id
        idsala=(random.randint(1,10))
        idcheck=' '.join(str(diccionario_salas))
        if str(idsala)not in idcheck:
            break
    print("Clave de la sala es",idsala)
    salas =[str(input('Nombre de la sala: '))]                                          #crea nombre sala
    cupo_sala=(input('Cupo de la sala: '))                                              #crea cupo sala
    salas.append(int(cupo_sala))                                                        #agrega cupo sala a lista de nombre
    diccionario_salas.append({ idsala:salas for sala in salas })                        #asigna id a lista de nombre
    print(diccionario_salas)



def registroreservacion():
    fecha=[]
    fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
    fechareservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()   #fecha de reservacion
    fecha.append(fechareservacion)                                                      #guarda fecha en lista temporal
    fechaactual=datetime.datetime.today().date()                                        #fecha actual
    fechalimite= fechareservacion + datetime.timedelta(days=-2)                         #fecha 2 dias antes de reservacion
    if fechaactual >= fechalimite:                                                      #Compara que la fecha sea valida
        print('Fecha no valida. No puede realizarse la reservacion.')
    else:
        datos.append(fechareservacion)
        while True:                                                                     #crea el id
            idreservacion=(random.randint(1,10))
            idcheck=' '.join(str(diccionario_reservacion))
            if str(idreservacion)not in idcheck:
                break
        print('Clave de la reservacion es ', idreservacion)
        nombrereservacion=[str(input('\nCuale es el nombre de la reservacion: '))]      #crea el nombre de evento
        print('*'*14)                                                                   #menu para Turnos
        print('TURNOS')
        print('*'*14)
        print('[M]. Matutino')
        print('[V]. Vespertino')
        print('[N]. Nocturno' )
        opmenu=input('\nEscoge la opción: ')                                            #escoje opcion de menu para Turnos
        if (not opmenu.upper() in "MVN"):
            print("Opción no válida. No puede realizarse la reservacion.")
        if (opmenu.upper()=="M"):
            turno='Matutino'
            fecha.append(turno)
        elif (opmenu.upper()=="V"):
            turno='Vespertino'
            fecha.append(turno)
        elif (opmenu.upper()=="N"):
            turno='Nocturno'
            fecha.append(turno)
        for x in range(len(listafechas)):
            if listafechas[x]==fecha:
                print('Turno ya ocupado. No puede realizarse la reservacion.')           #checa si la fecha y turno son iguales
                return
        listafechas.append(fecha)
        print(diccionario_salas)#agrega sala a datos
        numerosala=input('Escoje el numero de sala que quieres usar :')
        datos.append(numerosala)
        print(diccionario_clientes)#agrega nombre cliente a datos
        nombrecliente=input('Selecciona tu registro de cliente por id:')
        datos.append(diccionario_clientes[0][int(nombrecliente)])
        datos.append(nombrereservacion[0])
        datos.append(turno)
        print('El nombre del evento es ',nombrereservacion,', en el turno ',turno,'.')
        nombrereservacion.append(str(turno))#agregar fecha
        diccionario_reservacion.append({idreservacion:nombrereservacion for reservacion in nombrereservacion})
        lista_datos.append(datos)
        print('el diccionario de reservacion es ',diccionario_reservacion)
        print('los datos generados son ', datos)

def editarnombre():
    print(diccionario_reservacion)
    idBuscado=int(input('Ingrese el id deseado: '))                                #pregunta por id a cambiar
    nuevoNombre=str(input('ingrese nombre nuevo: '))                               #pregunta por nuevo nombre
    location=0
    for x in range(len(diccionario_reservacion)):
        tempList.append(list(diccionario_reservacion[x].keys()))                   #crea lista de ids como listas
        idlist.append(tempList[x][0])                                              #comvierte las ids a int
        if idlist[x] == idBuscado:                                                 #compara las ids con el id deseado hasta llegar a la posicion a cambiar
            break
        else:
            location=location+1
    diccionario_reservacion[location][idBuscado][0] = nuevoNombre                  #cambia el nombre
    print(diccionario_reservacion)

def consulta():
    fecha_capturada = input("Ingrese la fecha a consultar (dd/mm/aaaa): \n")
    fechareservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
    print('-'*76)
    print('--            REPORTE DE RESERVACIONES PARA EL DIA ', fechareservacion,'           --')
    print('-'*76)
    print('-- FECHA                      SALA   CLIENTE   EVENTO            TURNO             --')
    print('-'*76)
    print('', lista_datos)
    print('-'*76)
    print('--                                FIN DEL REPORTE                          --')
    
    #para generar la lista que puedes utilizar para hacer los prints, debes de crear un cliente,
    #una sala, y empezar la creacion de una reservacion. Todos los datos requiridos para crear la
    #consulta se guardaran en la lista lista_datos, la cual se puede extraer el info para poner en
    #la consulta.
    #cambien lo que quieran, tengo el codigo resguardado



while True:

    print('*'*14)
    print('MENU DE OPCIONES')
    print('*'*14)
    print('[A]. Registrar cliente')
    print('[B]. Registrar sala ')
    print('[C]. Registrar reservacion' )
    print('[D]. Editar nombre del evento')
    print('[E]. Consulta de reservaciones')
    print('[F]. SALIR')
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

    #OPCION=REGISTRAR SALA
    if (opmenu.upper()=="B"):
        registrosala()

    #OPCION=REGISTRAR RESERVACION
    if (opmenu.upper()=="C"):
        registroreservacion()

    #OPCION=EDITAR NOMBRE
    if (opmenu.upper()=="D"):
        editarnombre()

    #OPCION=CONSULTA DE RESERVACIONES
    if (opmenu.upper()=="E"):
        consulta()