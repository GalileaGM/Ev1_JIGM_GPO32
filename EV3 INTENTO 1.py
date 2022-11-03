import csv
import datetime
from heapq import merge
import openpyxl
import os
import os.path
import random
import sqlite3
from sqlite3 import Error
import sys


#/// CREACION DE BASE DE DATOS Y TABLAS
try:
    with sqlite3.connect("EVIDENCIA3.db") as conn:
        cursor=conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS cliente (Clavecliente INTEGER PRIMARY KEY, Nombrecliente TEXT NOT NULL);")
        cursor.execute("CREATE TABLE IF NOT EXISTS sala (Clavesala INTEGER PRIMARY KEY, Nombresala TEXT NOT NULL, Cuposala INTEGER NOT NULL);")
        cursor.execute("CREATE TABLE IF NOT EXISTS turno (Claveturno INTEGER PRIMARY KEY, Nombreturno TEXT NOT NULL);")
        cursor.execute("CREATE TABLE IF NOT EXISTS reservacion (Clavereservacion INTEGER PRIMARY KEY, Nombrecliente TEXT NOT NULL, Nombrereservacion TEXT NOT NULL, Fechareservacion timestamp, turnore INTEGER NOT NULL, salare INTEGER NOT NULL,FOREIGN KEY(turnore) REFERENCES turno(Claveturno), FOREIGN KEY(salare) REFERENCES sala(Clavesala));")
        print("Tablas creadas")
        cursor.execute("INSERT INTO turno VALUES(1,'matutino')")
        cursor.execute("INSERT INTO turno VALUES(2,'vespertino')")
        cursor.execute("INSERT INTO turno VALUES(3,'nocturno')")
        print("Turnos creados")
except Error as e:
    print(e)
except:
    print(f'Se produjo el siguiente error: {sys.exc_info()[0]}')
finally:
    conn.close()

while True:
    print('*'*14)
    print('MENU DE OPCIONES')
    print('*'*14)
    print('[A]. Registrar cliente')
    print('[B]. Registrar sala ')
    print('[C]. Reservación' )
    print('[D]. Reporte de reservaciones')
    print('[E]. SALIR')

    opmenu=input('\nEscoge la opción: ')

    if (not opmenu.upper() in "ABCDE"):
        print("Opción no válida, intenta de nuevo.")
        continue

    #OPCION=SALIR
    if (opmenu.upper()=="E"):
        print("Fin de la ejecución.")
        break

    #OPCION=REGISTRAR CLIENTE
    if (opmenu.upper()=="A"):
        while True:
            Nombrecliente=str(input("Ingrese el nombre del cliente : "))
            if Nombrecliente=='':
                print("No debe omitirse el nombre del cliente")
                continue
            else:
                try:
                    with sqlite3.connect("EVIDENCIA3.db") as conn:
                        cursor=conn.cursor()
                        valores={"Nombrecliente":Nombrecliente}
                        cursor.execute("INSERT INTO cliente (Nombrecliente) VALUES(:Nombrecliente)", valores)
                        print("Registro agregado exitosamente")
                except Error as e:
                    print(e)
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                    conn.close()
            break
        continue

    #OPCION=REGISTRAR SALA
    if (opmenu.upper()=="B"):
        while True:
            Nombresala=str(input("Ingrese el nombre de la sala : "))
            if Nombresala=='':
                print("No debe omitirse el nombre de la sala")
                continue
            else:
                while True:
                    try:
                        Cuposala=int(input("Ingrese el cupo de la sala: "))
                    except ValueError:
                        print("Respuesta no valida: Solo se acepta numero")
                        continue
                    if Cuposala<=0:
                        print("Incorrecto, el cupo de la sala debe de ser mayor a 0")
                        continue
                    else:
                        try:
                            with sqlite3.connect("EVIDENCIA3.db") as conn:
                                cursor=conn.cursor()
                                valores={"Nombresala":Nombresala, "Cuposala":Cuposala}
                                cursor.execute("INSERT INTO sala (Nombresala, Cuposala) VALUES(:Nombresala,:Cuposala)", valores)
                                print("Registro ha sido exitoso")
                        except Error as e:
                            print(e)
                        except:
                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                        finally:
                            conn.close()
                    break
            break
        continue

    #OPCION=SUBMENU RESERVACION
    if (opmenu.upper()=="C"):
        while True:
            print('*'*14)
            print('SUBMENU DE RESERVACIONES')
            print('*'*14)
            print('A. REGISTRAR NUEVA RESERVACIÓN')
            print('B. MODIFICAR NOMBRE RESERVACIÓN')
            print('C. CONSULTAR DISPONIBILIDAD DE SALA')
            print('D. ELIMINAR RESERVACIÓN')
            print('E. REGRESAR AL MENU')
            submenur=input('\nEscoge la opción: ')

            if (not submenur.upper() in "ABCD"):
                print("Opción no válida, intenta de nuevo.")
                continue
            if (submenur.upper()=="A"):
                continue
            
            if (submenur.upper()=="B"):
                continue

            if (submenur.upper()=="C"):
                continue

            if (submenur.upper()=="D"):
                continue

            if (submenur.upper()=="E"):
                break
            continue

    #OPCION=SUBMENU REPORTE
    if (opmenu.upper()=="D"):
        while True:
            print('*'*14)
            print('SUBMENU DE REPORTE')
            print('*'*14)
            print('A. REPORTE EN PANTALLA PARA RESERVACION DE UNA FECHA')
            print('B. EXPORTAR REPORTE EN EXCEL')
            print('C. REGRESAR AL MENU')
            submenure=input('\nEscoge la opción: ')

            if (not submenure.upper() in "ABCD"):
                print("Opción no válida, intenta de nuevo.")
                continue

            if (submenure.upper()=="A"):
                continue
            
            if (submenure.upper()=="B"):
                continue
            
            if (submenure.upper()=="C"):
                break
            continue
