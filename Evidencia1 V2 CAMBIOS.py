import random
import datetime

idcheckcliente=[]
diccionarioClientes={}
#///
idchecksala=[]
tuplasala=()
diccionarioSalas={}
#///
idcheckreserv=[]
listafechas=[]
tuplareserv=()
diccionarioreserv={}

def registrocliente():
    while True:
        idclientes=(random.randint(1,10))
        if str(idclientes) not in idcheckcliente:
            idcheckcliente.append(idclientes)
            break
    print('Clave del cliente es ', idclientes)#opcional
    cliente = input('Nombre del cliente: ')
    diccionarioTemp = {}
    diccionarioTemp = {idclientes:cliente}
    diccionarioClientes.update(diccionarioTemp)
    print(diccionarioClientes)

def registrosala():
    while True:
        idsala=(random.randint(1,10))
        if str(idsala) not in idchecksala:
            idcheckcliente.append(idsala)
            break
    salas = (input('Nombre de la sala: '))                                          #crea nombre sala
    cupo_sala = int((input('Cupo de la sala: ')))
    tuplasala = (salas,cupo_sala)
    diccionarioTemp = {}
    diccionarioTemp = {idsala:tuplasala}
    diccionarioSalas.update(diccionarioTemp)
    print(diccionarioSalas)

def registroreservacion():
    fecha=[]
    fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
    fechareservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()   #fecha de reservacion
    fecha.append(fechareservacion)                                                         #guarda fecha en lista temporal
    fechaactual=datetime.datetime.today().date()                                        #fecha actual
    fechalimite= fechareservacion + datetime.timedelta(days=-2)                         #fecha 2 dias antes de reservacion
    if fechaactual >= fechalimite:                                                      #Compara que la fecha sea valida
        print('Fecha no valida. No puede realizarse la reservacion.')
    else:
        while True:
            idreserv=(random.randint(1,10))
            if str(idreserv) not in idcheckreserv:
                idcheckcliente.append(idreserv)
                break
        nombrereservacion=(input('\nCuale es el nombre de la reservacion: '))       #nombre de reservacion
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
        print(diccionarioSalas)
        numerosala=input('Ingresa el numero de sala que quieres usar: ')
        print(diccionarioClientes)
        numerocliente=input('Ingresa tu id asignado: ')
        tuplareserv=(str(fecha[0]),int(numerosala),int(numerocliente),nombrereservacion,turno)  #dd/mm/aaaa,id sala,id cliente,nombre reserva,turno
        diccionarioTemp = {}
        diccionarioTemp = {idreserv:tuplareserv}
        diccionarioreserv.update(diccionarioTemp)
        print(diccionarioreserv)

def editarnombre():
    print(diccionarioreserv)
    idBuscado=int(input('Ingrese el id deseado: '))                                #pregunta por id a cambiar
    nuevoNombre=str(input('ingrese nombre nuevo: '))                               #pregunta por nuevo nombre
    templist = list(diccionarioreserv[idBuscado])
    templist[3]=nuevoNombre
    diccionarioreserv[idBuscado] = templist
    print(diccionarioreserv)

def consulta():
    fecha_capturada = input("Ingrese la fecha a consultar (dd/mm/aaaa): \n")
    fechareservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
    listabusqueda = []                                                                                  #lista temporal para buscar en el diccionario
    templist = list(diccionarioreserv.keys())
    for x in templist:
        if diccionarioreserv[x][0] != str(fechareservacion):
            continue
        else:
            listabusqueda.append(x)
            continue
    print('-'*76)
    print('--            REPORTE DE RESERVACIONES PARA EL DIA ', fechareservacion,'           --')
    print('-'*76)
    print('-- FECHA                      SALA   CLIENTE   EVENTO            TURNO    --')
    print('-'*76)
    for x in listabusqueda:
        print(' ',diccionarioreserv[x][0],' '*18,diccionarioreserv[x][1],' '*5,diccionarioreserv[x][2],' '*5,diccionarioreserv[x][3],' '*10,diccionarioreserv[x][4]) #diccionario reserva)
    print('-'*76)
    print('--                                FIN DEL REPORTE                         --')

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