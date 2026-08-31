#Sistema de Venta de entradas para Espectaculos
#Modulos
import random
#Contadores/Acumuladores
DiaValido = 0
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
    while AñoA <2026:
        AñoA = int(input("Error,Ingresar un año que sea 2026 o en adelante"))
    if (AñoA % 4 == 0 and AñoA % 100 != 0) or (AñoA % 400 == 0):
        print("Año Bisiesto")
        if MesM == 2:
            while DiaD <1 or DiaD >29:
                print("Dia invalido, ingreselo nuevamente a continuacion")
                DiaD = int(input("Ingresar DiaD nuevamente entre 1 - 29 incluido el 29: "))
            if MesM <1 or MesM > 12:
                print("Mes invalido,Ingresar nuevamente el mes, entre 1 - 12 a continuacion ")
                MesM = int(input("Ingresar mes:"))
            elif MesM == 4 or MesM ==6 or MesM == 9 or MesM == 11:
                while DiaD <1 or DiaD > 30:
                    print("Dia invalido, ingresar nuevamente el dia a continuacion")
                    DiaD = int(input("Ingresar nuevamente el dia: ")) 
                    DiaValido =+ 1
            if DiaValido == 0:
                while DiaD < 1 or DiaD >31:
                    print("Error de dia, ingresar un dia entre el 1-31 a continuacion")
                    DiaD = int(input("Ingrese un numero de dia:"))
           

    else:
        print("Año no bisiesto")
        if MesM ==2:
            while DiaD <1 or DiaD >=29:
                print("Dia Invalido, Ingresar nuevamente el dia a continuacion")
                DiaD = int(input("Ingresar DiaD nuevamente entre 1 - 29 sin incluir el 29:"))
            if MesM <1 or MesM > 12:
                print("Mes invalido,Ingresar nuevamente el mes, entre 1 - 12 a continuacion ")
                MesM = int(input("Ingresar mes:"))
            elif MesM == 4 or MesM ==6 or MesM == 9 or MesM == 11:
                while DiaD <1 or DiaD > 30:
                    print("Dia invalido, ingresar nuevamente el dia a continuacion")
                    DiaD = int(input("Ingresar nuevamente el dia: ")) 
                    DiaValido =+ 1
            if DiaValido == 0:
                while DiaD < 1 or DiaD >31:
                    print("Error de dia, ingresar un dia entre el 1-31 a continuacion")
                    DiaD = int(input("Ingrese un numero de dia:"))
    
        
    
    
    return
def GuardarFechaEspectaculo (DiaD,MesM,AñoA,Espectaculos=[]):
    pass 
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
    Año = int(input("Ingrese año del 2026 en adelante:"))
    Opcion = int(input("Ingresar una opcion"))
    GuardarPrecioEntrada(precioEntrada,ListadePreciosdeEntradas)
    GuardarFechaEspectaculo(Dia,Mes,Año,Fechas_Espectaculos)
    VerificarFormatoFecha(Dia,Mes,Año)
    seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir:")
    if seguir == "Si":
        print("Continuamos")
    else:
        print("Terminando programa...")
        seguir = "No"