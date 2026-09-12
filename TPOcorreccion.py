#Sistema de Venta de entradas para Espectaculos

#FUNCIONES
def Menu ():
    '''Muestra el menu principal de opciones en pantalla'''
    print("================= MENU =================")
    print("  1 - Ver espectaculos")
    print("  2 - Ingresar Espectaculo")
    print("  3 - Comprar tickets de entrada")
    print("  4 - Ingresar Cliente")
    print("  5 - Ver Clientes")
    print("  6 - Salir")
    print("========================================")

def VerEspectaculos(Espectaculos,FechaEspectaculos):
    '''Imprime la lista de espectaculos registrados con sus fechas'''
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
    '''Agrega un nuevo espectaculo a la lista correspondiente'''
    ListaE.append(Espec)

def VerificarFormatoFecha(DiaD,MesM,AñoA):
    '''Valida que el dia, mes y año sean valores correctos y devuelve la fecha valida'''
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

def Armar_Fecha_Completa(d, m, a):
    '''Convierte dia mes y año en un texto en formato dia mes año con separadores'''
    return "/".join(map(str, (d, m, a)))

def GuardarFechaEspectaculo (DiaD,MesM,AñoA,Espectaculos):
    '''Genera la fecha formateada y la guarda en la lista de fechas'''
    fecha = Armar_Fecha_Completa(DiaD, MesM, AñoA)
    Espectaculos.append(fecha)

def IngresarClientes (Cliente,ListaClientes):
    '''Agrega un nuevo cliente a la lista de clientes'''
    ListaClientes.append(Cliente)

def ContinuarPrograma(seguir):
    '''Valida y normaliza la respuesta del usuario para continuar o no el programa'''
    while (seguir != "No" and seguir != "no" and seguir != "NO" and
           seguir != "Si" and seguir != "si" and seguir != "SI"):
        seguir = input('Error. La respuesta no es ni "Si" ni "No", Intente de nuevo: ')
    if seguir == "No" or seguir == "no" or seguir == "NO":
        seguir="No"
        return seguir
    else:
        seguir="Si"
        return seguir

def rellenarmatriz(matriz):
    '''Llena todas las casillas de una matriz con valores cero'''
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = 0

def imprimirmatriz(matriz):
    '''Muestra en pantalla la matriz de asientos con formato de columnas'''
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%6d" %matriz[f][c], end="")
        print()
        
def VerClientes(ListaClientes):
    '''Imprime en pantalla la lista de clientes registrados'''
    print()
    print("===== LISTA DE CLIENTES =====")
    for i in range(len(ListaClientes)):
        numero = str(i + 1)
        print(numero + "- [ " + ListaClientes[i] + " ]")
    if len(ListaClientes) == 0:
        print(" -No se encontraron clientes")
    print("=============================")
    print()

def VerificarValorMatriz(valor):
    '''Valida que el valor ingresado para fila o columna este entre 1 y 10'''
    while valor > 10 or valor < 1:
        valor=int(input("Error. Ingrese un valor correcto (entre 1 y 10)"))
    return valor
    
def validar_formato(formato):
    '''Verifica que un texto ingrese unicamente caracteres numericos y no este vacio'''
    if len(formato) == 0:
        return False
    digitos = "0123456789"
    for caracter in formato:
        if caracter not in digitos:
            return False

#Listas 
Clientes = []
ListaEspectaculosEspectaculos = [] 
FechasEspectaculos = []
ListaDeAsientos=[]
ListaDeCampo=[]

#Variables Globales
seguir = "Si"

#MAIN
while seguir != "No":
    Menu()
    Opcion = int(input("Ingresar una opcion: "))
    print("-----------------------------------------------------------------------")
    while Opcion > 6 or Opcion < 1:
        Menu()
        Opcion=int(input("Error. La opcion ingresada no existe, intente de nuevo: "))
    if Opcion == 1: 
        VerEspectaculos(ListaEspectaculosEspectaculos,FechasEspectaculos)
    if Opcion == 2:
        Espectaculo = input("Ingresar un espectaculo:")
        GuardarEspectaculo(Espectaculo,ListaEspectaculosEspectaculos)
        nuevamatriz = [[0 for c in range(10)] for f in range(10)]
        ListaDeAsientos.append(nuevamatriz)
        ListaDeCampo.append(0)
        print("A continuacion ingresar en formato D/M/A la fecha")
        Dia = int(input("Ingrese dia de 1 a 31: "))
        Mes = int(input("Ingrese mes del 1 al 12: "))
        Año = int(input("Ingrese año del 2026 en adelante: "))
        Dia, Mes, Año =VerificarFormatoFecha(Dia,Mes,Año)
        GuardarFechaEspectaculo(Dia,Mes,Año,FechasEspectaculos)
    if Opcion == 3:
        if len(ListaEspectaculosEspectaculos) == 0:
            print("  -No se ingresaron espectaculos")
            print("=====================================")
        else:
            print("Espectaculos disponibles:")
            for i in range(len(ListaEspectaculosEspectaculos)):
                print(i + 1, "-", ListaEspectaculosEspectaculos[i])
            num_esp = int(input("Seleccione el numero de espectaculo que desea ver: "))
            while num_esp < 1 or num_esp > len(ListaEspectaculosEspectaculos):
                num_esp = int(input("Error. Seleccione un numero valido de la lista: "))
            indiceespectaculo = num_esp - 1
            asientos = ListaDeAsientos[indiceespectaculo]
            print("¿Qué zona desea comprar?")
            print("1 - Platea / Asientos")
            print("2 - Campo (Pie)")
            tipo_zona = int(input("Seleccione una opción (1 o 2): "))
            while tipo_zona not in [1, 2]:
                tipo_zona = int(input("Opción inválida. Ingrese 1 para Asientos o 2 para Campo: "))
            if tipo_zona == 1:
                print("A continuacion se mostrara los asientos disponibles:")
                print("--------------------------------------------------------------")
                imprimirmatriz(asientos)
                print("--------------------------------------------------------------")
                deseacomprar = input("Desea comprar? (Responda Si o No): ")
                deseacomprar = ContinuarPrograma(deseacomprar)
                if deseacomprar == "Si":
                    filacomprar = int(input("¿En que fila desea comprar su asiento?: "))
                    filacomprar = VerificarValorMatriz(filacomprar)
                    columnacomprar = int(input("¿En que columna desea comprar su asiento?: "))
                    columnacomprar = VerificarValorMatriz(columnacomprar)
                    print("--------------------------------------------------------------------")
                    while asientos[filacomprar - 1][columnacomprar - 1] == 1:
                        print("Error. La entrada ya ha sido vendida, Pruebe con otra.")
                        filacomprar = int(input("¿En que fila desea comprar su asiento?: "))
                        filacomprar = VerificarValorMatriz(filacomprar)
                        columnacomprar = int(input("¿En que columna desea comprar su asiento?: "))
                        columnacomprar = VerificarValorMatriz(columnacomprar)
                        print("--------------------------------------------------------------------")  
                    precioentrada = 110000 - (filacomprar * 5000)
                    print(f"El precio de la entrada es de {precioentrada} pesos argentinos")
                    deseacomprar = input("Quiere realizar la compra? (Si para continuar, No para cancelar): ")
                    deseacomprar = ContinuarPrograma(deseacomprar)
                    if deseacomprar == "Si":
                        asientos[filacomprar - 1][columnacomprar - 1] = 1
                        print("Asiento reservado con exito")
            elif tipo_zona == 2:
                vendidos_actuales = ListaDeCampo[indiceespectaculo]
                if vendidos_actuales >= 50:
                    print("Lo sentimos, el Campo para este espectaculo esta agotado (50/50).")
                else:
                    precio_campo = 70000
                    print(f"Entradas de campo disponibles: {50 - vendidos_actuales}/50")
                    print(f"El precio de la entrada de Campo es de {precio_campo} pesos argentinos.")
                    deseacomprar = input("Quiere realizar la compra? (Si para continuar, No para cancelar): ")
                    deseacomprar = ContinuarPrograma(deseacomprar)
                    if deseacomprar == "Si":
                        ListaDeCampo[indiceespectaculo] += 1
                        print("Entrada de campo reservada con exito")
    if Opcion == 4:
        cliente = input("Ingrese su nombre y apellido:")
        IngresarClientes(cliente,Clientes)
    if Opcion == 5:
        print()
        VerClientes(Clientes)
    if Opcion == 6:
        seguir="No"
        print("Terminando programa...")
        print("=======================================")
    if Opcion != 6:
        seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir): ")
        seguir = ContinuarPrograma(seguir)
