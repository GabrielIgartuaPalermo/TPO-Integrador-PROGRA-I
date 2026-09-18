#Sistema de Venta de entradas para Espectaculos

#FUNCIONES
def Menu ():
    '''Muestra el menu principal de opciones en pantalla'''
    print()
    print("================= MENU =================")
    print("  1 - Ver espectaculos")
    print("  2 - Ingresar Espectaculo")
    print("  3 - Comprar tickets de entrada")
    print("  4 - Ingresar Cliente")
    print("  5 - Ver Clientes")
    print("  6 - Salir")
    print("========================================")

def VerEspectaculos(espectaculos,fechaespectaculos):
    '''Imprime la lista de espectaculos registrados con sus fechas'''
    print()
    print("============ ESPECTACULOS =============")
    for i in range(len(espectaculos)):
        numero = str(i + 1)
        print("   ", numero + "- [ " + espectaculos[i] + " - " + fechaespectaculos[i] + " ]")
    if len(espectaculos) == 0:
        print()
        print("                  No se ingresaron espectaculos")
        print()
    print("=======================================")
    print()

def validar_formato(formato):
    '''Verifica que un texto ingrese unicamente caracteres numericos y no este vacio'''
    if len(formato) == 0:
        return False
    digitos = "0123456789"
    for caracter in formato:
        if caracter not in digitos:
            return False
    return True

def PedirEntero(mensaje):
    '''Usa validar_formato para pedir un input hasta que sea solo numerico y lo convierte a int'''
    texto = input(mensaje)
    while validar_formato(texto) == False:
        texto = input("Error. Ingrese unicamente numeros validos: ")
    return int(texto)

def VerificarFormatoFecha(diad,mesm,añoa):
    '''Valida que el dia, mes y año sean valores correctos y devuelve la fecha valida'''
    while añoa < 2026:
        añoa = PedirEntero("Error. Ingresar un año que sea 2026 o en adelante: ")
    while mesm < 1 or mesm > 12:
        mesm = PedirEntero("Mes invalido, ingresar nuevamente el mes (1-12): ")
    if mesm == 2:
        if (añoa % 4 == 0 and añoa % 100 != 0) or (añoa % 400 == 0):
            max_dias = 29
        else:
            max_dias = 28
    elif mesm == 4 or mesm == 6 or mesm == 9 or mesm == 11:
        max_dias = 30
    else:
        max_dias = 31
    while diad < 1 or diad > max_dias:
        diad = PedirEntero("Dia invalido, ingresar un dia entre 1 y " + str(max_dias) + ": ")
    return diad, mesm, añoa

def Armar_Fecha_Completa(d, m, a):
    '''Convierte dia mes y año en un texto en formato dia mes año con separadores'''
    return "/".join(map(str, (d, m, a)))

def GuardarFechaEspectaculo (diad,mesm,añoa,espectaculos):
    '''Genera la fecha formateada y la guarda en la lista de fechas'''
    fecha = Armar_Fecha_Completa(diad, mesm, añoa)
    espectaculos.append(fecha)

def ContinuarPrograma(seguir):
    '''Valida y normaliza la respuesta del usuario para continuar o no el programa'''
    while seguir.lower() != "si" and seguir.lower() != "no":
        seguir = input('Error. La respuesta no es ni "Si" ni "No", Intente de nuevo: ')
    if seguir.lower() == "no":
        seguir="No"
        return seguir
    else:
        seguir="Si"
        return seguir

def imprimirmatriz(matriz):
    '''Muestra en pantalla la matriz de asientos con formato de columnas'''
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%6d" %matriz[f][c], end="")
        print()

def VerClientes(listaclientes):
    '''Imprime en pantalla la lista de clientes registrados'''
    print()
    print("===== LISTA DE CLIENTES =====")
    for i in range(len(listaclientes)):
        numero = str(i + 1)
        print(numero + "- [ " + listaclientes[i] + " ]")
    if len(listaclientes) == 0:
        print(" -No se encontraron clientes")
    print("=============================")
    print()

def VerificarValorMatriz(valor):
    '''Valida que el valor ingresado para fila o columna este entre 1 y 10'''
    while valor > 10 or valor < 1:
        valor=PedirEntero("Error. Ingrese un valor correcto (entre 1 y 10): ")
    return valor

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
    opcion = PedirEntero("Ingresar una opcion: ")
    print("-----------------------------------------------------------------------")
    while opcion > 6 or opcion < 1:
        Menu()
        opcion=PedirEntero("Error. La opcion ingresada no existe, intente de nuevo: ")
    if opcion == 1: 
        VerEspectaculos(ListaEspectaculosEspectaculos,FechasEspectaculos)
    if opcion == 2:
        espectaculo = input("Ingresar un espectaculo:")
        while espectaculo.strip() == "": 
            espectaculo = input("Error. El nombre no puede estar vacío, ingresa un espectaculo de nuevo:")
        ListaEspectaculosEspectaculos.append(espectaculo)
        nuevamatriz = [[0 for c in range(10)] for f in range(10)]
        ListaDeAsientos.append(nuevamatriz)
        ListaDeCampo.append(0)
        print("A continuacion ingresar en formato D/M/A la fecha")
        dia = PedirEntero("Ingrese dia de 1 a 31: ")
        mes = PedirEntero("Ingrese mes del 1 al 12: ")
        año = PedirEntero("Ingrese año del 2026 en adelante: ")
        dia, mes, año = VerificarFormatoFecha(dia,mes,año)
        GuardarFechaEspectaculo(dia,mes,año,FechasEspectaculos)
    if opcion == 3:
        if len(ListaEspectaculosEspectaculos) == 0:
            print("  -No se ingresaron espectaculos")
            print("=====================================")
        else:
            print("Espectaculos disponibles:")
            for i in range(len(ListaEspectaculosEspectaculos)):
                print(i + 1, "-", ListaEspectaculosEspectaculos[i])
            num_esp = PedirEntero("Seleccione el numero de espectaculo que desea ver: ")
            while num_esp < 1 or num_esp > len(ListaEspectaculosEspectaculos):
                num_esp = PedirEntero("Error. Seleccione un numero valido de la lista: ")
            indiceespectaculo = num_esp - 1
            asientos = ListaDeAsientos[indiceespectaculo]
            print("¿Qué zona desea comprar?")
            print("1 - Platea / Asientos")
            print("2 - Campo (Pie)")
            tipozona = PedirEntero("Seleccione una opción (1 o 2): ")
            while tipozona not in [1, 2]:
                tipozona = PedirEntero("Opción inválida. Ingrese 1 para Asientos o 2 para Campo: ")
            if tipozona == 1:
                print("A continuacion se mostrara los asientos disponibles:")
                print("--------------------------------------------------------------")
                imprimirmatriz(asientos)
                print("--------------------------------------------------------------")
                deseacomprar = input("Desea comprar? (Responda Si o No): ")
                deseacomprar = ContinuarPrograma(deseacomprar)
                if deseacomprar == "Si":
                    filacomprar = PedirEntero("¿En que fila desea comprar su asiento?: ")
                    filacomprar = VerificarValorMatriz(filacomprar)
                    columnacomprar = PedirEntero("¿En que columna desea comprar su asiento?: ")
                    columnacomprar = VerificarValorMatriz(columnacomprar)
                    print("--------------------------------------------------------------------")
                    while asientos[filacomprar - 1][columnacomprar - 1] == 1:
                        print("Error. La entrada ya ha sido vendida, Pruebe con otra.")
                        filacomprar = PedirEntero("¿En que fila desea comprar su asiento?: ")
                        filacomprar = VerificarValorMatriz(filacomprar)
                        columnacomprar = PedirEntero("¿En que columna desea comprar su asiento?: ")
                        columnacomprar = VerificarValorMatriz(columnacomprar)
                        print("--------------------------------------------------------------------")  
                    precioentrada = 110000 - (filacomprar * 5000)
                    print("El precio de la entrada es de " + str(precioentrada) + " pesos argentinos")
                    deseacomprar = input("Quiere realizar la compra? (Si para continuar, No para cancelar): ")
                    deseacomprar = ContinuarPrograma(deseacomprar)
                    if deseacomprar == "Si":
                        asientos[filacomprar - 1][columnacomprar - 1] = 1
                        print("Asiento reservado con exito")
            elif tipozona == 2:
                vendidosactuales = ListaDeCampo[indiceespectaculo]
                if vendidosactuales >= 50:
                    print("Lo sentimos, el Campo para este espectaculo esta agotado (50/50).")
                else:
                    preciocampo = 75000
                    print("Entradas de campo disponibles: " + str(50 - vendidosactuales) + "/50")
                    print("El precio de la entrada de Campo es de " + str(preciocampo) + " pesos argentinos.")
                    deseacomprar = input("Quiere realizar la compra? (Si para continuar, No para cancelar): ")
                    deseacomprar = ContinuarPrograma(deseacomprar)
                    if deseacomprar == "Si":
                        ListaDeCampo[indiceespectaculo] += 1
                        print("Entrada de campo reservada con exito")
    if opcion == 4:
        cliente = input("Ingrese su nombre y apellido:")
        while cliente.strip() == "": 
            cliente = input("Error. El nombre no puede estar vacío, ingrese su nombre y apellido de nuevo:")
        Clientes.append(cliente)
    if opcion == 5:
        print()
        VerClientes(Clientes)
    if opcion == 6:
        seguir="No"
        print("Terminando programa...")
        print("=======================================")
    if opcion != 6:
        seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir): ")
        seguir = ContinuarPrograma(seguir)
