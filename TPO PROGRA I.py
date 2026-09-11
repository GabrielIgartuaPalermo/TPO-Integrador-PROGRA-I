#Sistema de Venta de entradas para Espectaculos
#Modulosw
import random
#Listas 
Clientes = []
ListadePreciosdeEntradas = [] 
Lista_EspectaculosEspectaculos = [] 
Fechas_Espectaculos = [] 
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
    print("1 - Ver espectaculos")
    print("2 - Agregar espectaculo")
    print("3 - Comprar entradas")
    print("4 - Registrar cliente")
    print("5 - Ver clientes")
    print("6 - Buscar espectaculo")
    print("7 - Ver ventas")
    print("8 - Guardar datos en archivo")
    print("9 - Cargar datos desde archivo")
    print("10 - Salir")
#Funciones de Carga
def IngresarClientes (Cliente,ListaClientes):
    ListaClientes.append(Cliente)
    return  

def GuardarEspectaculo(Espec,ListaE):
    ListaE.append(Espec)
    return ListaE

def GuardarPrecioEntrada (Precio,Precios=[]):
    Precios.append(Precio)
    return Precios

def GuardarFechaEspectaculo (DiaD,MesM,AñoA,Espectaculos=[]):
    fecha = Armar_Fecha_Completa(DiaD, MesM, AñoA)
    Espectaculos.append(fecha)
    return Espectaculos
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
def VerEspectaculos(Espectaculos,FechaEspectaculos):
    print(Espectaculos[:], sep="/")
    print(FechaEspectaculos[:], sep="/")
    return
def BuscarEspectaculo(ShowsList,Busqueda):
    contadorENC = 1
    while contadorENC != 0:
        for SHOW in ShowsList:
            if Busqueda == SHOW:
                print("Se ha encontrado el espectaculo")
                contadorENC = 1
                return Busqueda
            else:
                print("No se ha encontrado")
                return print("No se ha encontrado el espectaculo")
def VerClientes(CL):
    for CLIENT in CL:
        print(CL)
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
        cliente = input("Ingrese su nombre y apellido:")
        IngresarClientes(cliente,Clientes)
    if Opcion == 5:
        VerClientes(Clientes)
    if Opcion == 6:
        EspectaculoB = input("Ingrese el espectaculo que quiere buscar:")
        BuscarEspectaculo(Lista_EspectaculosEspectaculos,EspectaculoB)
    seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir:")
    seguir = ContinuarPrograma(seguir)