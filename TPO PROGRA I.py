#Modulos
import random
#Sistema de Venta de entradas para Espectaculos
#FUNCIONES
def GuardarPrecioEntrada (Precio,Precios=[]):
    Precios.append(Precio)
    return Precios
def Menu ():
    print("1-Ver espectaculos")
    print("2-Comprar tickets")
    print("3-Ver clientes")
    
    return
def VerificarFormatoFecha(DiaD,MesM,AñoA):
    if AñoA % 400 == 0:
        if MesM == 2:
            while DiaD <1 or DiaD >29:
                print("Dia invalido, ingreselo nuevamente a continuacion")
                DiaD = int(input("Ingresar DiaD nuevamente entre 1 - 29 incluido el 29: "))
        if MesM <1 or MesM > 12:
            print("Mes invalido,Ingresar nuevamente el mes, entre 1 - 12 a continuacion ")
            MesM = int(input("Ingresar mes:"))
    else:
        if MesM ==2:
            while DiaD <1 or DiaD >=29:
                print("Dia Invalido, Ingresar nuevamente el dia a continuacion")
                DiaD = int(input("Ingresar DiaD nuevamente entre 1 - 29 sin incluir el 29:"))
                
        
    
    
    return
def GuardarFechaEspectaculo (FechaE,Espectaculos=[]):
    Espectaculos.append(FechaE)
    return 
#Listas 
Clientes = []
ListadePreciosdeEntradas = [] 
Lista_EspectaculosEspectaculos = [] 
Fechas_Espectaculos = [] 
#MAIN
seguir = "Si"
while seguir != "No":
    Menu() 
    precioEntrada = float(input("Ingresar precio: "))
    Dia = int(input("Ingrese dia de 1 a 31:"))
    Mes = int(input("Ingrese mes del 1 al 12:"))
    Año = int(input("Ingrese año del 2026 en adelante"))
    Opcion = int(input("Ingresar una opcion"))
    GuardarPrecioEntrada(precioEntrada,ListadePreciosdeEntradas)
    GuardarFechaEspectaculo(Fecha,Fechas_Espectaculos)
    VerificarFormatoFecha(Dia,Mes,Año)
    seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir:")
    if seguir == "Si":
        print("Continuamos")
    else:
        print("Terminando programa...")
        seguir = "No"