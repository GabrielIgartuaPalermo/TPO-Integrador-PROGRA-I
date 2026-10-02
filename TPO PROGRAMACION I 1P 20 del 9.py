#Sistema de Venta de entradas para Espectaculos

#FUNCIONES
def Menu ():
    '''Muestra el menu principal de opciones en pantalla'''
    print()
    print("================= MENU =================")
    print("  1 - Ver espectaculos")
    print("  2 - Ingresar Espectaculo")
    print("  3 - Eliminar Espectaculo")
    print("  4 - Modificar Espectaculo")
    print("  5 - Ver Clientes")
    print("  6 - Salir")
    print("========================================")

def IngresarEspectaculos(lista):
    espectaculo = input("Ingrese el Espectaculo: ").strip().lower()
    lista.append(espectaculo)
    D = int(input("Ingrese el dia del mes:"))
    M = int(input("Ingrese el mes:"))
    A = int(input("Ingrese el año:"))
    VerificarFormatoFecha(D,M,A)
    Armar_Fecha_Completa(D,M,A)
    return lista

def EliminarEspectaculos(lista):
    espectaculo = input("Ingrese el espectaculo que desea eliminar: ").strip().lower()
    if espectaculo in lista:
        lista.remove(espectaculo)
        print("Espectaculo eliminado")
    else:
        print("No se ha encontrado el espectaculo")
"""
def VerEspectaculos(LISTAESPECTACULOS):
    '''Imprime la lista de espectaculos registrados con sus fechas'''
    print()
    print("============ ESPECTACULOS =============")
    for i in range(len(LISTAESPECTACULOS)):
        numero = str(i + 1)
        print("   ", numero + "- [ " + LISTAESPECTACULOS[i] + " - " + LISTAESPECTACULOS[i] + " ]")
    if len(LISTAESPECTACULOS) == 0:
        print()
        print("No se ingresaron espectaculos")
        print()
    print("=======================================")
    print()
"""
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
        diad = PedirEntero(f"Dia invalido, ingresar un dia entre 1 y {max_dias}: ")
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
        seguir = "No"
        return seguir
    else:
        seguir = "Si"
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
    print("====== LISTA DE CLIENTES ======")
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
        valor = PedirEntero("Error. Ingrese un valor correcto (entre 1 y 10): ")
    return valor

#FUNCIONMAIN/PROGRAMAPRINCIPAL
def Programa():
    #ContadorPrincipal
    seguir = "Si"
    #VAR
    ListaEspec = []
    while seguir != "No":
        Menu()
        opcion = PedirEntero("Ingresar una opcion: ")
        print("-----------------------------------------------------------------------")
        while opcion > 6 or opcion < 1:
            Menu()
            opcion = PedirEntero("Error. La opcion ingresada no existe, intente de nuevo: ")
        """ if opcion == 1:
            VerEspectaculos(ListaEspec)"""
        if opcion == 2:
            IngresarEspectaculos(ListaEspec)
        if opcion == 3:
            EliminarEspectaculos(ListaEspec)
        """if opcion == 4:
            cliente = input("Ingrese su nombre y apellido:")
            while cliente.strip() == "":
                cliente = input("Error. El nombre no puede estar vacío, ingrese su nombre y apellido de nuevo:")
            cliente = cliente.title()
            Clientes.append(cliente)
        if opcion == 5:
            VerClientes(Clientes)
        if opcion == 6:
            seguir = "No"
            print("Terminando programa...")
            print("=======================================")
        if opcion != 6:
            seguir = ContinuarPrograma(input("Deseas seguir? (Ingrese Si para seguir o No para no seguir): "))
"""

Programa()
