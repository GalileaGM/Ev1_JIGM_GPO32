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
#///
turnos={1:"Matutino",2:"Vespertino",3:"Nocturno"}
listaEncontrados=[]
reservDisponibles=[]

def registrocliente():
    idclientes=max(diccionarioClientes.keys(), default=0)+1
    print('Clave del cliente es ', idclientes)#opcional
    cliente = input('Nombre del cliente: ')
    diccionarioTemp = {}
    diccionarioTemp = {idclientes:cliente}
    diccionarioClientes.update(diccionarioTemp)
    print(diccionarioClientes)

def registrosala():
    idsala=max(diccionarioSalas.keys(), default=0)+1
    salas = (input('Nombre de la sala: ')) #crea nombre sala
    try:
        cupo_sala = int((input('Cupo de la sala: ')))
    except ValueError:
        print("Respuesta no valida: Solo se acepta numero")
        return
    tuplasala = (salas,cupo_sala)
    diccionarioTemp = {}
    diccionarioTemp = {idsala:tuplasala}
    diccionarioSalas.update(diccionarioTemp)
    print(diccionarioSalas)

def registroreservacion():
    fecha=[]
    try: #try para prevenir error de mal fecha ingresada
        fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
        fechareservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()   #fecha de reservacion
    except ValueError:
        print("Respuesta no valida: Solo se acepta fecha")
        return
    fecha.append(fechareservacion)                                                         #guarda fecha en lista temporal
    fechaactual=datetime.datetime.today().date()                                        #fecha actual
    fechalimite= fechareservacion + datetime.timedelta(days=-2)                         #fecha 2 dias antes de reservacion
    if fechaactual >= fechalimite:                                                      #Compara que la fecha sea valida
        print('Fecha no valida: Ingrese una fecha con dos dias de anticipacion.')
    else:
        idreserv=max(diccionarioreserv.keys(), default=0)+1
        nombrereservacion=(input('\nCuale es el nombre de la reservacion: '))       #nombre de reservacion
        print('*'*14)                                                                   #menu para Turnos
        print('TURNOS')
        print('*'*14)
        print('[M]. Matutino')
        print('[V]. Vespertino')
        print('[N]. Nocturno' )
        opmenu=input('\nEscoge la opción: ')                                            #escoje opcion de menu para Turnos
        if (not opmenu.upper() in "MVN"):
            print("Opción no válida: Favor de seleccionar opcion en la lista.")
        if (opmenu.upper()=="M"):
            turno=1
            fecha.append(turnos[turno])
        elif (opmenu.upper()=="V"):
            turno=2
            fecha.append(turnos[turno])
        elif (opmenu.upper()=="N"):
            turno=3
            fecha.append(turnos[turno])
        for x in range(len(listafechas)):
            if listafechas[x]==fecha:
                print('Turno ya ocupado. No puede realizarse la reservacion.')           #checa si la fecha y turno son iguales
                return
        listafechas.append(fecha)
        if diccionarioSalas=={}:        #checa si hay salas registradas
            print('Error: No hay salas registradas')
            return
        print(diccionarioSalas)
        numerosala=input('Ingresa el numero de sala que quieres usar: ')
        if diccionarioClientes=={}:     #checa si hay clientes registrados
            print('Error: No hay clientes registrados')
            return
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
    try:
        fecha_capturada = input("Ingrese la fecha a consultar (dd/mm/aaaa): \n")
        fechareservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
    except ValueError:
        print('Respuesta no valida: solo se acepta fecha')
        return
    listabusqueda = []                                                                                  #lista temporal para buscar en el diccionario
    templist = list(diccionarioreserv.keys())
    for x in templist:
        if diccionarioreserv[x][0] != str(fechareservacion):
            continue
        else:
            listabusqueda.append(x)
            continue
    print('-'*76)
    print('--\t\t\tREPORTE DE RESERVACIONES PARA EL DIA ', fechareservacion,'\t\t\t--')
    print('-'*76)
    print('--FECHA\t\t\t\tSALA\t\tCLIENTE\t\tEVENTO\t\tTURNO\t--')
    print('-'*76)
    if listabusqueda == []:
        print(' '*23, 'No hay eventos para ', fechareservacion)
    else:
        for x in listabusqueda:
            print(f'{diccionarioreserv[x][0]}\t\t\t{diccionarioSalas[diccionarioreserv[x][1]][0]}\t\t{diccionarioClientes[diccionarioreserv[x][2]]}\t\t{diccionarioreserv[x][3]}\t\t{diccionarioreserv[x][4]}') #diccionario reserva
    print('-'*76)
    print('--                                FIN DEL REPORTE                         --')

def consultasala():
    fechaInput = input("Dime una fecha (dd/mm/aaaa): \n")
    fechaBuscada = datetime.datetime.strptime(fechaInput, "%d/%m/%Y").date()
    for clave,valor in diccionarioreserv.items():   #crea lista de salas en uso
        sala,fecha,turno=(valor[1],valor[0],valor[4])
        if str(fecha) == str(fechaBuscada):
            listaEncontrados.append((sala,turno))
            reservEncontradas=set(listaEncontrados)
    for sala in diccionarioSalas.keys():            #crea lista de todas las posibilidades
        for turno in turnos.keys():
            reservDisponibles.append((sala,turno))
            combinacionReservDisponibles=set(reservDisponibles)
    salasTurnosDisponibles=sorted(combinacionReservDisponibles-reservEncontradas)

    print('*'*30)
    print(f"*Salas disponibles para rentar el {fechaBuscada.strftime('%d/%m/%Y')}*\n")
    print("Salas\t\tTurnos")
    for sala,turno in salasTurnosDisponibles:
        print(f"{sala},{diccionarioSalas[sala][0]}\t\t{turnos[turno]}")

while True:
    print('*'*14)
    print('MENU DE OPCIONES')
    print('*'*14)
    print('[A]. Registrar cliente')
    print('[B]. Registrar sala ')
    print('[C]. Registrar reservacion' )
    print('[D]. Editar nombre del evento')
    print('[E]. Consulta de reservaciones')
    print('[F]. Consulta de salas disponibles')
    print('[G]. SALIR')
    opmenu=input('\nEscoge la opción: ')

    if (not opmenu.upper() in "ABCDEFG"):
        print("Opción no válida, intenta de nuevo.")
        continue

    #OPCION=SALIR
    if (opmenu.upper()=="G"):
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

    #OPCION=CONSULTA DE DIAS SALAS DISPONIBLES
    if (opmenu.upper()=="F"):
        consultasala()