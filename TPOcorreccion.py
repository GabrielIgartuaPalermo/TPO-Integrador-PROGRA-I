#Sistema de Venta de entradas para Espectaculos

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
    print("-------------- MENU --------------")
    print("  1-Ver espectaculos")
    print("  2-Ingresar Espectaculo")
    print("  3-Ingresar precio de la entrada")
    print("  4-Comprar tickets de entrada")
    print("  5-Ingresar Cliente")
    print("  6-Ver Clientes")
    print("--------------------------------------")
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

def GuardarFechaEspectaculo (DiaD,MesM,AñoA,Espectaculos=[]):
    fecha = Armar_Fecha_Completa(DiaD, MesM, AñoA)
    Espectaculos.append(fecha)
    return Espectaculos

def Armar_Fecha_Completa(d, m, a):
    return "/".join(map(str, (d, m, a)))

def IngresarClientes (Cliente,ListaClientes):
    ListaClientes.append(Cliente)
    return

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

#MAIN
while seguir != "No":
    Menu() 
    Opcion = int(input("Ingresar una opcion: "))
    while Opcion > 6 or Opcion < 1:
        Menu()
        Opcion=int(input("Error. La opcion ingresada no existe, intente de nuevo: "))
    if Opcion == 1: 
        VerEspectaculos(Lista_EspectaculosEspectaculos,Fechas_Espectaculos)
    if Opcion == 2:
        Espectaculo = input("Ingresar un espectaculo:")
        GuardarEspectaculo(Espectaculo,Lista_EspectaculosEspectaculos)
        print("A continuacion ingresar en formato D/M/A la fecha")
        Dia = int(input("Ingrese dia de 1 a 31: "))
        Mes = int(input("Ingrese mes del 1 al 12: "))
        Año = int(input("Ingrese año del 2026 en adelante: "))
        Dia, Mes, Año =VerificarFormatoFecha(Dia,Mes,Año)
        GuardarFechaEspectaculo(Dia,Mes,Año,Fechas_Espectaculos)
    if Opcion == 3:
        precioEntrada = float(input("Ingresar precio: "))
        GuardarPrecioEntrada(precioEntrada,ListadePreciosdeEntradas)
    if Opcion == 4:
        pass
    if Opcion == 5:
        cliente = input("Ingrese su nombre y apellido:")
        IngresarClientes(cliente,Clientes)
    if Opcion == 6:
        pass
    seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir): ")
    seguir = ContinuarPrograma(seguir)