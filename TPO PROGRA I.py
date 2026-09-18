#Sistema de Venta de entradas para Espectaculos
#Modulosw
import random
#Listas 
Clientes = []
ListadePreciosdeEntradas = [] 
Lista_EspectaculosEspectaculos = [] 
Fechas_Espectaculos = []
L_Stock = [] 
#Matriz 
matrizsinuso =       [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
for fila in range(3):
    for columna in range(3):
        matrizsinuso[fila][columna] = fila + columna

#Variables Globales
seguir = "Si"
#Contadores/Acumuladores

#FUNCIONES
#MENU
def Menu():
    print("================= MENU =================")
    print("1 - Ver espectaculos")
    print("2 - Agregar espectaculo")
    print("3 - Comprar Entrada")
    print("4 - Registrar cliente")
    print("5 - Ver clientes")
    print("6 - Buscar espectaculo")
    print("7 - Ver ventas")
    print("8 - Modificar Espectaculo")
    print(" - Salir")
    print("======================================")
    
#Funciones de Carga
def modificar_espectaculo(LE,LF,LS,LP,ESPEC):
    for indice, espec in enumerate(LE):
        if ESPEC in LE:
            print("Espectaculo encontrado")
            deseo = input("Que deseas cambiar?:").lower
            if deseo == "precio":
                for p in range(len(LP)):
                    if p == indice:
                        precionuevo = float(input("Ingrese el precio nuevo que desea que tenga el espectaculo:"))
                        LP[p].append(precionuevo)
            elif deseo == "stock":
                for s in range(len(LS)):
                    if s == indice:
                        STOCK = int(input("Ingrese el STOCK nuevo:"))
                        LS[s].append(STOCK)
            elif deseo == "nombre":
                for N in range(len(LE)):
                    if N == indice:
                        nombrenuevo = input("Ingrese el nombre nuevo para el espectaculo:")
                        LE[N].append(nombrenuevo) 
            elif deseo == "fecha":
                for f in range(len(LF)):
                    if f == indice:
                        d = int(input("Ingrese dia:"))
                        m = int(input("Ingrese el mes:"))
                        a = int(input("Ingrese el año:"))
                        VerificarFormatoFecha(d,m,a)
                        Armar_Fecha_Completa(d,m,a)
                        LF[f].append(Armar_Fecha_Completa)


def IngresarClientes(Cliente,ListaClientes):
    for C, elem in enumerate(ListaClientes):
        ListaClientes[C].append(Cliente)
    return  

def GuardarStock(ListaStocks,ListaEspec):
    for S,Nstock in enumerate(ListaStocks):
        if ListaEspec != []:
            ListaStocks[S].append(1)

def GuardarEspectaculo(Espec,ListaE):
    for e, elementos in enumerate(ListaE):
        ListaE(e).append(Espec)
        return 

def GuardarPrecioEntrada(Precio,Precios=[]):
    for P, elem in enumerate(Precios):
        Precios.append(Precio)
    return 

def GuardarFechaEspectaculo(DiaD,MesM,AñoA,Espectaculos=[]):
    for F, fecha in enumerate(Espectaculos):
        fecha = Armar_Fecha_Completa(DiaD, MesM, AñoA)
        Espectaculos[F].append(fecha)
    return
#FUNCIONES DE VALIDACION
def VerificarFormatoFecha(DiaD,MesM,AñoA):
    while AñoA < 2026:
        AñoA = int(input("Error. Ingresar un año que sea 2026 o en adelante: "))
    while MesM < 1 or MesM > 12:
        MesM = int(input("Mes invalido, ingresar nuevamente el mes (1-12): "))
    if MesM == 2:
        if (AñoA % 4 == 0 and AñoA % 100 != 0) or (AñoA % 400 == 0):
            max_dias = 29
        else:
            max_dias = 28
    elif MesM == 4 or MesM == 6 or MesM == 9 or MesM == 11:
        max_dias = 30
    else:
        max_dias = 31
    while DiaD < 1 or DiaD > max_dias:
        DiaD = int(input("Dia invalido, ingresar un dia entre 1 y" + str(max_dias) + ": "))
    return DiaD, MesM, AñoA

#Funciones de Formateo
def Armar_Fecha_Completa(d, m, a):
    return "/".join(map(str, (d, m, a)))
#Funciones de compra

#Funciones de Consulta
def VerVentas():
    pass
def VerEspectaculos(Espectaculos,FechaEspectaculos):
    print(Espectaculos[:], sep="/")
    print(FechaEspectaculos[:], sep="/")
    return
def BuscarEspectaculo(ShowsList,Busqueda):
    contadorENC = 1
    while contadorENC != 0:
        for SHOW in ShowsList:
            if Busqueda == SHOW:
                print(f"Se ha encontrado el espectaculo: {SHOW}")
                contadorENC = 1
                return 
            else:
                print("No se ha encontrado")
                return 
def VerClientes(CL):
    for CLIENT in CL:
        print(CLIENT)
    return 
#Otras funciones
def ContinuarPrograma(seguir):
    while (seguir != "No" and seguir != "no" and seguir != "NO" and
           seguir != "Si" and seguir != "si" and seguir != "SI"):
        seguir = input('Error. La respuesta no es ni "Si" ni "No", Intente de nuevo: ')
    if seguir == "No" or seguir == "no" or seguir == "NO":
        print("Terminando programa...")
        return "No"
    else:
        print("Continuamos")
        return "Si"

def ComprarEntradas(ListaE,ENTRADAC,Lista_Stock):
    for E, ENTRADAS in enumerate(ListaE):
        for S, STOCK in enumerate(Lista_Stock):
            if Lista_Stock[E] != 0:
                Lista_Stock[E] - 1
            else:
                print("No quedan entradas para el espectaculo")
    return
#Funciones de archivo
#MAIN
while seguir != "No":
    Menu() 
    Opcion = int(input("Ingresar una opcion:"))
    if Opcion == 1: 
        VerEspectaculos(Lista_EspectaculosEspectaculos,Fechas_Espectaculos)
    if Opcion == 2:
        Espectaculo = input("Ingresar un espectaculo:")
        GuardarEspectaculo(Espectaculo,Lista_EspectaculosEspectaculos)
        GuardarStock(L_Stock,Lista_EspectaculosEspectaculos)
        print("A continuacion ingresar en formato D/M/A la fecha")
        Dia = int(input("Ingrese dia de 1 a 31:"))
        Mes = int(input("Ingrese mes del 1 al 12:"))
        Año = int(input("Ingrese año del 2026 en adelante:"))
        VerificarFormatoFecha(Dia,Mes,Año)
        GuardarFechaEspectaculo(Dia,Mes,Año,Fechas_Espectaculos)
        precioEntrada = float(input("Ingresar precio: "))
        GuardarPrecioEntrada(precioEntrada,ListadePreciosdeEntradas)
    if Opcion == 3:
        print("Espectaculos disponibles:")
        VerEspectaculos(Lista_EspectaculosEspectaculos,Fechas_Espectaculos)
        CEntrada = input("Ingresar espectaculo a comprar")
        ComprarEntradas(Lista_EspectaculosEspectaculos,CEntrada,L_Stock)
    if Opcion == 4:
        cliente = input("Ingrese su nombre y apellido:")
        IngresarClientes(cliente,Clientes)
    if Opcion == 5:
        VerClientes(Clientes)
    if Opcion == 6:
        EspectaculoB = input("Ingrese el espectaculo que quiere buscar:")
        BuscarEspectaculo(Lista_EspectaculosEspectaculos,EspectaculoB)
    if Opcion == 7:
        pass
    if Opcion == 8:
        seguir = input("¿Estas Seguro que deseas salir?:")
        seguir = ContinuarPrograma(seguir)
    if Opcion == 9:
        especmodificado = input("Ingrese el nombre del espectaculo a modificar:")
        modificar_espectaculo(Lista_EspectaculosEspectaculos,Fechas_Espectaculos,L_Stock,ListadePreciosdeEntradas,especmodificado)
