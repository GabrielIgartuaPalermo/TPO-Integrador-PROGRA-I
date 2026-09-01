#Sistema de Venta de entradas para Espectaculos
#Modulos
import random
#Listas 
Clientes = []
ListadePreciosdeEntradas = [] 
Lista_EspectaculosEspectaculos = [] 
Fechas_Espectaculos = [] 
#Variables Globales
seguir = "Si"
#Contadores/Acumuladores
DiaValido = 0
#FUNCIONES
def Menu ():
    print("1-Ver espectaculos")
    print("2-Ingresar Espectaculo")
    print("3-Ingresar precio de la entrada")
    print("4-Comprar tickets de entrada")
    print("5-Ingresar Cliente")
    print("6-Ver Clientes")
    return

def VerEspectaculos(Espectaculos,FechaEspectaculos):
    print(Espectaculos[:], sep="/")
    print(FechaEspectaculos[:], sep="/")
    return

def GuardarEspectaculo(Espec,ListaE):
    ListaE.append(Espec)
    return ListaE

def GuardarPrecioEntrada (Precio,Precios=[]):
    Precios.append(Precio)
    return Precios

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

    fecha_completa = Armar_Fecha_Completa(DiaD, MesM, AñoA)
    return fecha_completa
def GuardarFechaEspectaculo (DiaD,MesM,AñoA,Espectaculos=[]):
    fecha = Armar_Fecha_Completa(DiaD, MesM, AñoA)
    Espectaculos.append(fecha)
    return Espectaculos

def Armar_Fecha_Completa(d, m, a):
    return "/".join(map(str, (d, m, a)))

def IngresarClientes (Cliente,ListaClientes):
    ListaClientes.append(Cliente)
    return
#MAIN
while seguir != "No":
    Menu() 
    Opcion = int(input("Ingresar una opcion"))
    if Opcion == 1: 
        VerEspectaculos(Lista_EspectaculosEspectaculos,Fechas_Espectaculos)
    if Opcion == 2:
        Espectaculo = input("Ingresar un espectaculo:")
        GuardarEspectaculo(Espectaculo,Lista_EspectaculosEspectaculos)
        print("A continuacion ingresar en formato D/M/A la fecha")
        Dia = int(input("Ingrese dia de 1 a 31:"))
        Mes = int(input("Ingrese mes del 1 al 12:"))
        Año = int(input("Ingrese año del 2026 en adelante:"))
        VerificarFormatoFecha(Dia,Mes,Año)
        GuardarFechaEspectaculo(Dia,Mes,Año,Fechas_Espectaculos)
    if Opcion == 3:
        precioEntrada = float(input("Ingresar precio: "))
        GuardarPrecioEntrada(precioEntrada,ListadePreciosdeEntradas)
    if Opcion == 4:
        pass
    if Opcion == 5:
        cliente = int(input("Ingrese su nombre y apellido:"))
        IngresarClientes(cliente,Clientes)
    if Opcion == 6:
        pass
    seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir:")
    if seguir == "Si":
        print("Continuamos")
    else:
        print("Terminando programa...")
        seguir = "No"