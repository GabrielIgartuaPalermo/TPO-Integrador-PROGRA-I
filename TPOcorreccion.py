#Sistema de Venta de entradas para Espectaculos

#FUNCIONES
def Menu ():
    print("================= MENU =================")
    print("  1 - Ver espectaculos")
    print("  2 - Ingresar Espectaculo")
    print("  3 - Comprar tickets de entrada")
    print("  4 - Ingresar Cliente")
    print("  5 - Ver Clientes")
    print("  6 - Salir")
    print("======================================")
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
        DiaD = int(input("Dia invalido, ingresar un dia entre 1 y " + str(max_dias) + ": "))
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

def rellenarmatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = 0

def imprimirmatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%6d" %matriz[f][c], end="")
        print()

#Listas 
Clientes = []
ListadePreciosdeEntradas = [] 
Lista_EspectaculosEspectaculos = [] 
Fechas_Espectaculos = []

#Matrices
filas = 10
columnas = 10
asientos = [[0 for c in range(columnas)] for f in range(filas)]

#Variables Globales
seguir = "Si"

#MAIN
rellenarmatriz(asientos)
while seguir != "No":
    Menu()
    Opcion = int(input("Ingresar una opcion: "))
    print("--------------------------------------------------------------------")
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
        print("A continuacion se mostrara los asientos disponibles en el estadio para comprar su entrada:")
        print("--------------------------------------------------------------")
        imprimirmatriz(asientos)
        print("--------------------------------------------------------------")
        deseacomprar=input("Desea comprar? (Responda Si o No): ")
        deseacomprar=ContinuarPrograma(deseacomprar)
        if deseacomprar == "Si":
            filacomprar=int(input("¿En que fila desea comprar su asiento?: "))
            while filacomprar > 10 or filacomprar < 0:
                filacomprar=int(input("Error. Ingrese un valor de fila correcto (entre 1 y 10)"))
            columnacomprar=int(input("¿En que columna desea comprar su asiento?: "))
            while columnacomprar > 10 or columnacomprar < 0:
                columnacomprar=int(input("Error. Ingrese un valor de columna correcto (entre 1 y 10)"))
            print("--------------------------------------------------------------------")
            filacomprar=filacomprar-1
            columnacomprar=columnacomprar-1
            if asientos[filacomprar][columnacomprar] == 1:
                while asientos[filacomprar][columnacomprar] == 1:
                    print("Error. La entrada que desea comprar ya ha sido vendida, Pruebe con otra")
                    filacomprar=int(input("¿En que fila desea comprar su asiento?: "))
                    while filacomprar > 10 or filacomprar < 1:
                        filacomprar=int(input("Error. Ingrese un valor de fila correcto (entre 1 y 10)"))
                    columnacomprar=int(input("¿En que columna desea comprar su asiento?: "))
                    while columnacomprar > 10 or columnacomprar < 1:
                        columnacomprar=int(input("Error. Ingrese un valor de columna correcto (entre 1 y 10)"))
                        print("--------------------------------------------------------------------")
            else:
                print("El precio de la entrada es de $200.000 pesos argentinos")
                deseacomprar=input("Quiere realizar la compra? (Si para continuar, No para cancelar): ")
                ContinuarPrograma(deseacomprar)
                if deseacomprar == "Si":
                    asientos[filacomprar][columnacomprar]=1
                    imprimirmatriz(asientos)
    if Opcion == 4:
        cliente = input("Ingrese su nombre y apellido:")
        IngresarClientes(cliente,Clientes)
    if Opcion == 5:
        pass
    if Opcion == 6:
        seguir="No"
        print("Terminando programa...")
        print("======================================")
    if Opcion != 6:
        seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir): ")
        seguir = ContinuarPrograma(seguir)
