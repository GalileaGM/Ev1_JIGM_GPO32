import datetime
from heapq import merge
import openpyxl
import os
import os.path
import random
import sqlite3
from sqlite3 import Error
import sys
#///
libro = openpyxl.Workbook()
hoja = libro["Sheet"]
hoja.title = "Reporte "
listaEncontrados=[]
reservDisponibles=[]
if not os.path.isfile("PIA.db"):
    print("Ejecucion Inicial")
    try:
        with sqlite3.connect("PIA.db") as conn:
            cursor=conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS registrocliente (idcliente INTEGER PRIMARY KEY, clientes TEXT NOT NULL);")
            cursor.execute("CREATE TABLE IF NOT EXISTS registrosala (idsala INTEGER PRIMARY KEY, salas TEXT NOT NULL, cupo_sala INTEGER NOT NULL);")
            cursor.execute("CREATE TABLE IF NOT EXISTS TURNO (idturno INTEGER PRIMARY KEY, Nombreturno TEXT NOT NULL);")
            cursor.execute("CREATE TABLE IF NOT EXISTS RESERVACION(idreserv INTEGER PRIMARY KEY, nombrereservacion TEXT NOT NULL,fechareservacion timestamp,idcliente INTEGER NOT NULL, idturno INTEGER NOT NULL,idsala INTEGER NOT NULL,FOREIGN KEY(idcliente)REFERENCES registrocliente(idcliente),FOREIGN KEY(idturno) REFERENCES TURNO(idturno), FOREIGN KEY(idsala) REFERENCES registrosala(idsala));")
            #print("Tablas creadas")
            cursor.execute("INSERT INTO TURNO VALUES(1,'matutino')")
            cursor.execute("INSERT INTO TURNO VALUES(2,'vespertino')")
            cursor.execute("INSERT INTO TURNO VALUES(3,'nocturno')")
            #print("Turnos creados")
    except Error as e:
        print(e)
    except:
        print(f'Se produjo el siguiente error: {sys.exc_info()[0]}')
    finally:
        conn.close()
if os.path.isfile("PIA.db"):
    while True:
        print("\n")
        print('*'*14)
        print('MENU PRINCIPAL')
        print('*'*14)
        print('[A]. RESERVACIONES')
        print('[B]. REPORTES ')
        print('[C]. REGISRAR UNA SALA' )
        print('[D]. REGISTRAR UN CLIENTE')
        print('[E]. SALIR')
        opmenu=input('\nEscoge la opci??n: ')
        if (not opmenu.upper() in "ABCDE"):
            print("Opci??n no v??lida, intenta de nuevo.")
            continue
        
        if (opmenu.upper()=="A"):#RESERVACION
            while True:
                print("\n")
                print('*'*14)
                print('SUBMENU DE RESERVACIONES')
                print('*'*14)
                print('A. REGISTRAR NUEVA RESERVACI??N')
                print('B. MODIFICAR NOMBRE RESERVACI??N')
                print('C. CONSULTAR DISPONIBILIDAD DE SALA')
                print('D. ELIMINAR RESERVACI??N')
                print('E. REGRESAR AL MENU')
                submenur=input('\nEscoge la opci??n: ')

                if(not submenur.upper() in "ABCDE"):
                    print("Opci??n no v??lida, intenta de nuevo.")
                    continue

                if(submenur.upper()=="A"):#REGISTRAR NUEVA RESERVACI??N
                    while True:
                        try:
                            with sqlite3.connect("PIA.db") as conn:
                                cursor = conn.cursor()
                                cursor.execute("SELECT * FROM registrocliente ORDER BY idcliente")
                                regclie = cursor.fetchall()
                                if regclie:
                                    print("--" * 30)
                                    print("\nCLIENTES REGISTRADOS....")
                                    print("--" * 30)
                                    print("**idcliente**\t**clientes**")
                                    print("--" * 30)

                                    for idcliente, clientes in regclie:
                                        print(f"{idcliente:^10}\t{clientes}")

                                Cliente=(input("Ingresa el id del cliente a reservar: ")).strip()

                                if Cliente=='':
                                    print("No debe omitirse el cliente")
                                    continue
                                else:
                                    valores = {"Clavecliente":Cliente}
                                    Cliente=int(Cliente)

                                    cursor.execute("SELECT * FROM registrocliente WHERE idcliente = :Clavecliente", valores)
                                    regclie = cursor.fetchall()
                                    if regclie:
                                        for Clavecliente, clientes in regclie:
                                            print(f"SE REGISTRO CORRECTAMENTE EL CLIENTE: {clientes}")
                                            continue
                                    else:
                                        print("No se encontraron registros en la respuesta")
                                        break

                        except Error as e:
                            print(e)
                        except:
                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                        finally:
                            conn.close()

                        while True:
                            try:

                                with sqlite3.connect("PIA.db") as conn:
                                    cursor = conn.cursor()
                                    cursor.execute("SELECT * FROM  registrosala ORDER BY idsala")
                                    regsala = cursor.fetchall()
                                    if regsala:

                                        print("\nSALAS REGISTRADAS....")
                                        print("--" * 30)
                                        print("***idsala***\t***salas***\t***cupo_sala***")
                                        print("--" * 30)

                                        for idsala, salas, cupo_sala in regsala:
                                            print(f"{idsala:^10}\t{salas}\t{cupo_sala}")
                                            continue

                                    Sala=input("Ingresa el numero de la sala que desea reservar : ").strip()

                                    if Sala=='':
                                        print("No debe omitirse el sala")
                                        continue

                                    else:
                                        try:
                                            with sqlite3.connect("PIA.db") as conn:
                                                cursor=conn.cursor()
                                                valores = {"Clavesala":Sala}
                                                Sala=int(Sala)
                                                cursor.execute("SELECT * FROM RESERVACION WHERE idsala=:Clavesala ", valores)
                                                regreserva = cursor.fetchall()
                                                if regreserva:
                                                    for idreserv ,nombrereservacion,fechareservacion,idcliente,idturno,idsala in regreserva:
                                                        print("****LO SENTIMOS, LA SALA YA SE ENCUENTRA OCUPADA****")
                                                    break

                                                else:

                                                    cursor.execute("SELECT * FROM registrosala WHERE idsala = :Clavesala", valores)
                                                    regsala = cursor.fetchall()

                                                    if regsala:
                                                        for Clavesala, salas, cupo_sala in regsala:
                                                            print(F"SE REGISTRO CORRECTAMENTE LA SALA:  {salas} ")
                                                            continue
                                                    else:
                                                        print("No se encontraron registros en la respuesta")
                                                        continue
                                        except Error as e:
                                            print(e)
                                        except:
                                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                        finally:
                                            conn.close()

                            except Error as e:
                                print(e)
                            except:
                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                            finally:
                                conn.close()

                            while True:
                                try: #try para prevenir error de mal fecha ingresada
                                    fecha_capturada=input("\nIngrese la fecha para la reservacion: ").strip()

                                    if fecha_capturada=='':
                                        print("No debe omitirse la fecha de la reservacion")
                                        continue

                                    else:
                                        fechareservacion=datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()  #fecha de reservacion

                                except ValueError:
                                    print("Respuesta no valida: Solo se acepta fecha")
                                    break

                                fechaactual=datetime.datetime.today().date()                                        #fecha actual
                                fechalimite= fechareservacion + datetime.timedelta(days=-1)                         #fecha 2 dias antes de reservacion
                                if fechaactual>=fechalimite:                                                      #Compara que la fecha sea valida
                                    print('Fecha no valida: Ingrese una fecha con dos dias de anticipacion.')
                                    break

                                with sqlite3.connect("PIA.db") as conn:
                                    cursor=conn.cursor()
                                    valores = {"FechaReservada":fechareservacion}
                                    cursor.execute("SELECT * FROM RESERVACION WHERE DATE(fechareservacion)=:FechaReservada", valores)
                                    regreserva = cursor.fetchall()
                                    if regreserva:
                                        for idreserv ,nombrereservacion,fechareservacion,idcliente,idturno,idsala in regreserva:
                                            print("****LO SENTIMOS, LA FECHA YA SE ENCUENTRA OCUPADA****")
                                            break
                                    else:
                                        print(f"Se registro correctamente la fecha: {fechareservacion}")
                                        while True:#
                                            try:

                                                with sqlite3.connect("PIA.db") as conn:
                                                    cursor = conn.cursor()
                                                    cursor.execute("SELECT * FROM TURNO ORDER BY idturno")
                                                    regturno = cursor.fetchall()
                                                        #Procedemos a evaluar si hay registros en la respuesta
                                                    if regturno:
                                                        print("\nTURNOS....")
                                                        print("--" * 30)
                                                        print("**idturno**\t**Nombreturno**")
                                                        print("--" * 30)
                                                        for idturno, Nombreturno in regturno:
                                                            print(f"{idturno:^10}\t{Nombreturno}")
                                                            continue


                                                        Turno=input("Ingrese el turno que desea reservar : ").strip()

                                                        if Turno=='':
                                                            print("No debe omitirse el turno")
                                                            continue


                                                        else:
                                                            try:
                                                                with sqlite3.connect("PIA.db") as conn:
                                                                    cursor=conn.cursor()
                                                                    Turno=int(Turno)
                                                                    valores = {"Claveturno":Turno}
                                                                    cursor.execute("SELECT * FROM RESERVACION WHERE idturno=:Claveturno", valores)
                                                                    regreserva = cursor.fetchall()
                                                                    if regreserva:
                                                                        for idreserv ,nombrereservacion,fechareservacion,idcliente,idturno,idsala in regreserva:
                                                                            print("****LO SENTIMOS, EL TURNO YA SE ENCUENTRA OCUPADO****")
                                                                        break
                                                                    else:
                                                                        cursor.execute("SELECT * FROM TURNO WHERE idturno = :Claveturno", valores)
                                                                        regturno = cursor.fetchall()
                                                                        if regturno:
                                                                            for Claveturno, Turno in regturno:
                                                                                print(f"SE REGISTRO CORRECTAMENTE EL TURNO: {Turno}")
                                                                                continue
                                                                        else:
                                                                            print("No se encontraron registros en la respuesta")
                                                                            continue
                                                            except Error as e:
                                                                print(e)
                                                            except:
                                                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                                            finally:
                                                                conn.close()
                                            except Error as e:
                                                print(e)
                                            except:
                                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                            finally:
                                                conn.close()

                                            while True:
                                                try:
                                                    NomRes=str(input("\nIngrese el nombre de la reservacion : ")).strip()
                                                    if NomRes=='':
                                                        print("No debe omitirse el nombre de la reservacion")
                                                        continue

                                                    else:
                                                        print(f"Se registro correctamente el nombre: {NomRes}")
                                                except Error as e:
                                                    print(e)
                                                except:
                                                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                                try:
                                                    with sqlite3.connect("PIA.db") as conn:
                                                        cursor=conn.cursor()
                                                        valores={"Nombrereservacion":NomRes, "fechareservacion":fechareservacion, "idcliente":Cliente,"idturno":Turno,"idsala":Sala}
                                                        cursor.execute("INSERT INTO RESERVACION(nombrereservacion,fechareservacion,idcliente,idturno,idsala) VALUES(:Nombrereservacion,:fechareservacion,:idcliente,:idturno,:idsala)", valores)
                                                        print(f"SE REGISTRO CORRECTAMENTE SU RESERVACION: {valores}")
                                                except Error as e:
                                                    print(e)
                                                except:
                                                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                                finally:
                                                    conn.close()
                                        
                                                break
                                            break
                                        break
                                break
                            break
                        break
                    continue
                if(submenur.upper()=="B"):#MODIFICAR NOMBRE RESERVACI??N
                    while True:
                        try:
                            with sqlite3.connect("PIA.db") as conn:
                                cursor = conn.cursor()
                                cursor.execute("SELECT * FROM RESERVACION ORDER BY idreserv")
                                regreserva = cursor.fetchall()
                                cursor.execute("SELECT idcliente, clientes FROM registrocliente ORDER BY idcliente")
                                regclie= cursor.fetchall()
                                cursor.execute("SELECT idsala,  salas FROM registrosala ORDER BY idsala")
                                regsala=cursor.fetchall()
                                if regreserva:
                                    if regclie:
                                        if regsala:
                                            print("")
                                            print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<10}".format('idreserv','nombrereservacion','fechareservacion','cliente','turno','sala' ))
                                            print("*" * 120)
                                            for idreserv ,nombrereservacion,fechareservacion,Nomcliente,idturno,Nomsala in regreserva:
                                                for idcliente, clientes in regclie:
                                                    for idsala, salas in regsala:
                                                        print(f"{idreserv}\t\t\t{nombrereservacion}\t\t{fechareservacion}\t\t{clientes}\t\t{idturno}\t{salas}")
                                                        continue
                                buscarclave=input("Ingrese la clave del registro que va a editar : ")
                                if buscarclave=='':
                                    print("No debe omitirse la clave")
                                    continue

                                valor={"Clavereser":buscarclave}
                                buscarclave=int(buscarclave)
                                cursor.execute("SELECT * FROM RESERVACION WHERE idreserv= :Clavereser",valor)
                                regreserva = cursor.fetchall()
                                cursor.execute("SELECT idcliente, clientes FROM registrocliente ORDER BY idcliente")
                                regclie= cursor.fetchall()
                                cursor.execute("SELECT idsala,  salas FROM registrosala ORDER BY idsala")
                                regsala=cursor.fetchall()
                                if regreserva:
                                    if regclie:
                                        if regsala:
                                            print("")
                                            nuevo_nombre=input("Ingrese el nuevo nombre de la reservacion  : ").strip()
                                            if nuevo_nombre=='':
                                                print("No debe omitirse")
                                                continue
                                            valores = {"Nombrereservacion":nuevo_nombre,"Clavereser":buscarclave}
                                            cursor.execute("UPDATE RESERVACION SET nombrereservacion = :Nombrereservacion WHERE idreserv=:Clavereser",valores)
                                            regreserva = cursor.fetchall()
                                            print(f"El registro se edito exitosamente a : {valores}")
                                            break
                                else:
                                    if not idreserv in regreserva:
                                        print("No existe este registro")
                                        continue
                        except Error as e:
                            print(e)
                        except:
                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                        finally:
                            conn.close()
                        break
                    continue
                
                if(submenur.upper()=="C"):#CONSULTAR DISPONIBILIDAD DE SALA
                    while True:
                        try:
                            fechaInput = input("Dime una fecha (dd/mm/aaaa): \n")

                            if fechaInput =='':
                                print("No debe omitirse la fecha de la reservacion")
                                continue
                            else:
                                fechaBuscada = datetime.datetime.strptime(fechaInput, "%d/%m/%Y").date()
                                try:
                                    with sqlite3.connect("PIA.db") as conn:
                                        cursor = conn.cursor()
                                        valor = {"fecha":fechaBuscada}
                                        cursor.execute("SELECT idsala,idturno FROM RESERVACION WHERE DATE(fechareservacion) = :fecha;", valor)
                                        regreserva = cursor.fetchall()
                                        cursor.execute("SELECT idsala,  salas FROM registrosala ORDER BY idsala")
                                        regsala=cursor.fetchall()

                                        reservaciones_ocupadas = set(regreserva)

                                        cursor.execute("SELECT idsala FROM registrosala")
                                        id_sala=cursor.fetchall()
                                        
                                        cursor.execute("SELECT Nombreturno FROM TURNO")
                                        Nombre_turno=cursor.fetchall()

                                        salas_si = []
                                        for sals in id_sala:
                                            sal = sals[0]
                                            salas_si.append(sal)

                                        turnos_si = [] #SE UTILIZA LOS CONJUNTOS ANIDADOS 
                                        for turnos in Nombre_turno: #RECORRE EL FOR PARA OBTENER CADA UNO DE LOS TURNOS 
                                            turno = turnos[0]
                                            turnos_si.append(turno)

                                        #print(salas_si)
                                        #print(id_sala)
                                        #print(turnos_si)
                                        #print(Nombre_turno)

                                        for sala in salas_si:
                                            for Nombreturno in turnos_si:
                                                reservDisponibles.append((sala,Nombreturno))
                                            combinaciones_reservaciones_disponibles = set(reservDisponibles)

                                        salas_turnos_disponibles = sorted(list(combinaciones_reservaciones_disponibles-reservaciones_ocupadas))

                                        print(combinaciones_reservaciones_disponibles)
                                        print(reservaciones_ocupadas)
                                        print("\n Las opciones disponibles para rentar en esa fecha son : ")
                                        print(f"Salas que se encuentran disponibles para rentar el {fechaBuscada}\n")
                                        print("***Salas***\t\t***Turnos***")

                                        for salas, Nombreturno in salas_turnos_disponibles:
                                            for idsala, salas in regsala:
                                                print(f"{salas}\t\t{Nombreturno}")
                                except Error as e:
                                    print(e)
                                except:
                                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                finally:
                                    conn.close()
                        except Error as e:
                            print (e)
                        except:
                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                        break
                    continue
                if(submenur.upper()=="D"):#ELIMINAR RESERVACI??N
                    while True:
                        try:
                            with sqlite3.connect("PIA.db") as conn:
                                cursor = conn.cursor()
                                cursor.execute("SELECT * FROM RESERVACION ORDER BY idreserv")
                                regreserva = cursor.fetchall()
                                cursor.execute("SELECT idcliente, clientes FROM registrocliente ORDER BY idcliente")
                                regclie= cursor.fetchall()
                                cursor.execute("SELECT idsala,  salas FROM registrosala ORDER BY idsala")
                                regsala=cursor.fetchall()
                                if regreserva:
                                    if regclie:
                                        if regsala:
                                            print("")
                                            print("{:<20} {:<20} {:<20} {:<40} {:<20} {:<20}".format('idreserv','nombrereservacion','fechareservacion','cliente','turno','sala' ))
                                            print("*" * 150)
                                            for idreserv ,nombrereservacion,fechareservacion,Nomcliente,idturno,Nomsala in regreserva:
                                                for idcliente, clientes in regclie:
                                                    for idsala, salas in regsala:
                                                        print("{:<20} {:<20} {:<20} {:<40} {:<20} {:<20}".format(idreserv ,nombrereservacion,fechareservacion,clientes,idturno,salas))
                                                        continue
                                            EliminarReg=int(input("Ingrese la clave del registro que desea eliminar : "))

                                            valor={"Eliminado":EliminarReg}
                                            cursor.execute("SELECT * FROM RESERVACION WHERE idreserv=:Eliminado",valor)
                                            regreserva = cursor.fetchall()

                                            if regreserva:
                                                elire =input("Desea eliminar la reservacion [Si/No ]: ")
                                            if (not elire.upper() in "SN"):
                                                print("Opcion no valida")
                                            if (elire.upper() == "S"):
                                                try: #try para prevenir error de mal fecha ingresada
                                                    fecape=input("Ingrese la fecha a eliminar: \n")
                                                    if fecape=='':
                                                        print("No debe omitirse la fecha de la reservacion")
                                                        continue
                                                    else:
                                                        fechre=datetime.datetime.strptime(fecape, "%d/%m/%Y").date()  #fecha a eliminar
                                                except ValueError:
                                                    print("Respuesta no valida: Solo se acepta fecha")
                                                fechac=datetime.datetime.today().date()                                        #fecha actual
                                                fechli= fechre + datetime.timedelta(days=-2)                         #fecha 3 dias antes de reservacion
                                                if fechac >=fechli:                                                      #Compara que la fecha sea valida
                                                    print('Fecha no valida: Ingrese una fecha con tres dias de anticipacion.')
                                                else:
                                                    cursor.execute("DELETE FROM RESERVACION WHERE idreserv = :Eliminado",valor)
                                                    print("Se ha eliminado la reservacion ")
                                                    break
                                            elif (elire.upper() == "N"):
                                                break
                        except Error as e:
                            print(e)
                        except:
                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                        finally:
                            conn.close()
                        break
                    continue
                if(submenur.upper()=="E"):#REGRESAR AL MENU
                    break
                break
            continue


        if(opmenu.upper()=="B"):#REPORTES
            while True:
                print('\n')
                print('*'*14)
                print('SUBMENU DE REPORTE')
                print('*'*14)
                print('A. REPORTE EN PANTALLA PARA RESERVACION DE UNA FECHA')
                print('B. EXPORTAR REPORTE EN EXCEL')
                print('C. REGRESAR AL MENU')

                submenure=input('\nEscoge la opci??n: ')

                if (not submenure.upper() in "ABC"):
                    print("Opci??n no v??lida, intenta de nuevo.")
                    continue

                if (submenure.upper()=="A"):
                    while True:
                        try:
                            fechaRep = input("Ingrese la fecha del evento (dd/mm/aaaa): ")
                            if fechaRep =='':
                                print("No debe omitirse la fecha de la reservacion")
                                continue
                            fecRer = datetime.datetime.strptime(fechaRep, "%d/%m/%Y").date()
                        except ValueError:
                            print('Respuesta no valida: solo se acepta fecha')
                        try:
                            with sqlite3.connect("PIA.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
                                cursor = conn.cursor()
                                valor = {"fecha":fecRer}
                                cursor.execute("SELECT nombrereservacion,DATE(fechareservacion),idcliente,idturno,idsala FROM RESERVACION WHERE DATE(fechareservacion) = :fecha;", valor)
                                regreserva = cursor.fetchall()
                                cursor.execute("SELECT idcliente, clientes FROM registrocliente ORDER BY idcliente")
                                regclie= cursor.fetchall()
                                cursor.execute("SELECT idsala,  salas FROM registrosala ORDER BY idsala")
                                regsala=cursor.fetchall()
                                if regreserva:
                                    if regclie:
                                        if regsala:
                                            print("")
                                            print("--"*48)
                                            print("-" + " "*23 + f"REPORTE DE RESERVACIONES PARA EL D??A {fecRer}" + " "*23 + "-")
                                            print("--"*48)
                                            print("{:<20} {:<20} {:<20} {:<20}".format('SALA','CLIENTE','EVENTO','TURNO'))
                                            print("--" * 48)

                                            for  fechareservacion,Nomsala,Nomcliente,nombrereservacion,idturno in regreserva:
                                                for idsala, salas in regsala:
                                                    for idcliente, clientes in regclie:
                                                        print(f"{salas}\t\t{clientes}\t\t{fechareservacion}\t\t{nombrereservacion}")
                                                        continue
                                            print("")
                                            print("-"*30 + f"FIN DEL REPORTE PARA EL D??A {fecRer}" + "-"*30)

                                else:
                                    print(f"***** NO HAY EVENTOS PARA EL DIA : {fecRer}*****")
                        except sqlite3.Error as e:
                            print(e)
                        except Exception:
                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                        finally:
                            conn.close()

                        break
                    continue
                
                if (submenure.upper()=="B"):
  
                    while True:
                        try:
                            fechaEx = input("Ingrese la fecha del evento (dd/mm/aaaa): ")
                            if fechaEx =='':
                                print("No debe omitirse la fecha de la reservacion")
                                continue
                            fecEx = datetime.datetime.strptime(fechaEx, "%d/%m/%Y").date()
                        except ValueError:
                            print('Respuesta no valida: solo se acepta fecha')

                        with sqlite3.connect("PIA.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
                            cursor = conn.cursor()
                            valor = {"fecha":fecEx}
                            cursor.execute("SELECT nombrereservacion,DATE(fechareservacion),idcliente,idturno,idsala FROM RESERVACION WHERE DATE(fechareservacion) = :fecha;", valor)
                            regreserva = cursor.fetchall()

                            if regreserva:
                                hoja["B1"].value = f"REPORTE DE RESERVACIONES PARA EL D??A {fecEx}"
                                hoja["A2"].value = "EVENTO"
                                hoja["B2"].value = "CLIENTE"
                                hoja["C2"].value = "TURNO"
                                hoja["D2"].value = "SALA"
                                for  nombrereservacion,fechareservacion,idcliente,idturno,idsala in regreserva:
                                    valoresRe=[(nombrereservacion,idcliente,idturno,idsala)]
                                    for valor in valoresRe:
                                        hoja.append(valor)
                                    libro.save(f"ReporteDeReservaciones{fecEx}.xlsx")
                                    print("\nLibro del reporte creado exitosamente!")
                            else:
                                print(f"***** NO HAY EVENTOS PARA EL DIA :{fecEx}*****")
                        break
                    continue

                if (submenure.upper()=="C"):
                    break
                break
            continue

        if(opmenu.upper()=="C"):#REGISRAR UNA SALA
            while True:
                Nomsala=str(input("Ingrese el nombre de la sala : ")).strip()
                if Nomsala=='':
                    print("No debe omitirse el nombre del sala")
                    continue
                else:
                    while True:
                        try:
                            CupSala=int(input("Ingrese el cupo de la sala: "))
                        except ValueError:
                            print("Respuesta no valida: Solo se acepta numero")
                            continue
                        if CupSala<=0:
                            print("Incorrecto, el cupo de la sala debe de ser mayor a 0")
                            continue
                        elif CupSala=='':
                            print("No debe omitirse la sala")
                        else:
                            try:
                                with sqlite3.connect("PIA.db") as conn:
                                    cursor=conn.cursor()
                                    valores={"Nombresala":Nomsala, "Cuposala":CupSala}
                                    cursor.execute("INSERT INTO registrosala(salas,cupo_sala) VALUES(:Nombresala,:Cuposala)", valores)
                                    print(f"Registro ha sido exitoso: {valores}")
                            except Error as e:
                                print(e)
                            except:
                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                            finally:
                                conn.close()
                        break
                break
            continue
        if(opmenu.upper()=="D"):#REGISTRAR UN CLIENTE
            while True:
                Nomcliente=str(input("Ingrese el nombre del cliente : ")).strip()
                if Nomcliente=='':
                    print("No debe omitirse el nombre del cliente")
                    continue
                else:
                    try:
                        with sqlite3.connect("PIA.db") as conn:
                            cursor=conn.cursor()
                            valores={"Nombrecliente":Nomcliente}
                            cursor.execute("INSERT INTO registrocliente (clientes) VALUES(:Nombrecliente)", valores)
                            print(f"Su registro ha sido exitosamente: {valores}")
                    except Error as e:
                        print(e)
                    except:
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                    finally:
                        conn.close()
                break
            continue
        if(opmenu.upper()=="E"):#SALIR
            print("Ejecucion Finalizada")
            break
        break