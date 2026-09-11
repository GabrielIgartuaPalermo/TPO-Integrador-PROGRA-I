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
    print()
    print("========== ESPECTACULOS ===========")
    for i in range(len(Espectaculos)):
        numero = str(i + 1)
        print(numero + "- [ " + Espectaculos[i] + " - " + FechaEspectaculos[i] + " ]")
    if len(Espectaculos) == 0:
        print("  -No se ingresaron espectaculos")
    print("===================================")
    print()

def GuardarEspectaculo(Espec,ListaE):
    ListaE.append(Espec)

def GuardarPrecioEntrada (Precio,Precios=[]):
    Precios.append(Precio)

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

def Armar_Fecha_Completa(d, m, a):
    return "/".join(map(str, (d, m, a)))

def IngresarClientes (Cliente,ListaClientes):
    ListaClientes.append(Cliente)

def ContinuarPrograma(seguir):
    while (seguir != "No" and seguir != "no" and seguir != "NO" and
           seguir != "Si" and seguir != "si" and seguir != "SI"):
        seguir = input('Error. La respuesta no es ni "Si" ni "No", Intente de nuevo: ')
    if seguir == "No" or seguir == "no" or seguir == "NO":
        seguir="No"
        return seguir
    else:
        seguir="Si"
        return seguir

def imprimirmatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%6d" %matriz[f][c], end="")
        print()
        
def VerClientes (ListaClientes):
    print()
    print("===== LISTA DE CLIENTES =====")
    for i in range(len(ListaClientes)):
        numero = str(i + 1)
        print(numero + "- [ " + Clientes[i] + " ]")
    if len(ListaClientes) == 0:
        print(" -No se encontraron clientes")
    print("=============================")
    print()

#Listas 
Clientes = []
ListadePreciosdeEntradas = [] 
Lista_EspectaculosEspectaculos = [] 
Fechas_Espectaculos = []
Lista_De_Asientos=[]

#Variables Globales
seguir = "Si"

#MAIN
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
        nueva_matriz = [[0 for c in range(10)] for f in range(10)]
        Lista_De_Asientos.append(nueva_matriz)
        print("A continuacion ingresar en formato D/M/A la fecha")
        Dia = int(input("Ingrese dia de 1 a 31: "))
        Mes = int(input("Ingrese mes del 1 al 12: "))
        Año = int(input("Ingrese año del 2026 en adelante: "))
        Dia, Mes, Año =VerificarFormatoFecha(Dia,Mes,Año)
        GuardarFechaEspectaculo(Dia,Mes,Año,Fechas_Espectaculos)
    if Opcion == 3:
        if len(Lista_EspectaculosEspectaculos) == 0:
            print("  -No se ingresaron espectaculos")
            print("===================================")
        else:
            print("Espectaculos disponibles:")
            for i in range(len(Lista_EspectaculosEspectaculos)):
                print(i + 1, "-", Lista_EspectaculosEspectaculos[i])
            num_esp = int(input("Seleccione el numero de espectaculo que desea ver: "))
            while num_esp < 1 or num_esp > len(Lista_EspectaculosEspectaculos):
                num_esp = int(input("Error. Seleccione un numero valido de la lista: "))
            indice_espectaculo = num_esp - 1
            asientos = Lista_De_Asientos[indice_espectaculo]
            print("A continuacion se mostrara los asientos disponibles en el estadio para comprar su entrada:")
            print("--------------------------------------------------------------")
            imprimirmatriz(asientos)
            print("--------------------------------------------------------------")
            deseacomprar=input("Desea comprar? (Responda Si o No): ")
            deseacomprar=ContinuarPrograma(deseacomprar)
            if deseacomprar == "Si":
                filacomprar=int(input("¿En que fila desea comprar su asiento?: "))
                while filacomprar > 10 or filacomprar < 1:
                    filacomprar=int(input("Error. Ingrese un valor de fila correcto (entre 1 y 10)"))
                columnacomprar=int(input("¿En que columna desea comprar su asiento?: "))
                while columnacomprar > 10 or columnacomprar < 1:
                    columnacomprar=int(input("Error. Ingrese un valor de columna correcto (entre 1 y 10)"))
                print("--------------------------------------------------------------------")
                filacomprar=filacomprar-1
                columnacomprar=columnacomprar-1
                while asientos[filacomprar][columnacomprar] == 1:
                    print("Error. La entrada que desea comprar ya ha sido vendida, Pruebe con otra")
                    filacomprar=int(input("¿En que fila desea comprar su asiento?: "))
                    while filacomprar > 10 or filacomprar < 1:
                        filacomprar=int(input("Error. Ingrese un valor de fila correcto (entre 1 y 10)"))
                        filacomprar=filacomprar-1
                    columnacomprar=int(input("¿En que columna desea comprar su asiento?: "))
                    while columnacomprar > 10 or columnacomprar < 1:
                        columnacomprar=int(input("Error. Ingrese un valor de columna correcto (entre 1 y 10)"))
                    print("--------------------------------------------------------------------")
                    columnacomprar=columnacomprar-1
                if asientos[filacomprar][columnacomprar] == 0:
                    print("El precio de la entrada es de $200.000 pesos argentinos")
                    deseacomprar=input("Quiere realizar la compra? (Si para continuar, No para cancelar): ")
                    deseacomprar=ContinuarPrograma(deseacomprar)
                    if deseacomprar == "Si":
                        asientos[filacomprar][columnacomprar]=1
    if Opcion == 4:
        cliente = input("Ingrese su nombre y apellido:")
        IngresarClientes(cliente,Clientes)
    if Opcion == 5:
        print()
        VerClientes(Clientes)
    if Opcion == 6:
        seguir="No"
        print("Terminando programa...")
        print("======================================")
    if Opcion != 6:
        seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir): ")
        seguir = ContinuarPrograma(seguir)
