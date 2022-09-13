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
idreservacion=0

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
    fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
    fechareservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()   #fecha de reservacion
    fechaactual=datetime.datetime.today().date()                                        #fecha actual
    fechalimite= fechareservacion + datetime.timedelta(days=-2)                         #fecha 2 dias antes de reservacion
    if fechaactual >= fechalimite:                                                      #Compara que la fecha sea valida
        print('Fecha no valida. No puede realizarse la reservacion.')
    else:
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
        elif (opmenu.upper()=="V"):
            turno='Vespertino'
        elif (opmenu.upper()=="N"):
            turno='Nocturno'
        print('El nombre del evento es ',nombrereservacion,', en el turno ,',turno,'.')
        nombrereservacion.append(str(turno))
        diccionario_reservacion.append({idreservacion:nombrereservacion for reservacion in nombrereservacion})
        print(diccionario_reservacion)

def editarnombre():
    cambioNombre=''
    idevento=(int(input('Id del evento que deseas renombrar: ')))
    cambioNombre=(str(input('Nombre al que desea cambiar: ')))
    eventoedit=diccionario_reservacion[idevento]
    eventoedit[0]=cambioNombre
    diccionario_reservacion[idevento]=eventoedit
    print(diccionario_reservacion)


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

    #OPCION=REGISTRAR SALA
    if (opmenu.upper()=="B"):
        registrosala()

    #OPCION=REGISTRAR RESERVACION
    if (opmenu.upper()=="C"):
        registroreservacion()

    #OPCION=EDITAR NOMBRE
    if (opmenu.upper()=="D"):
        editarnombre()