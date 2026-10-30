# Sistema de Venta de entradas para Espectaculos

def Menu():
    print()
    print("================= MENU =================")
    print("  1 - Ver Espectaculos")
    print("  2 - Ingresar Espectaculo")
    print("  3 - Eliminar Espectaculo")
    print("  4 - Modificar Espectaculo")
    print("  5 - Vender Entradas")
    print("  6 - Ver Clientes")
    print("  7 - Salir")
    print("========================================")

def MenuModificaciones():
    print("1-Nombre")
    print("- - - - ")
    print("2-Fecha")
    print("- - - - ")
    print("3-PrecioEntrada")
    print("- - - - - - - - -")
    print("4-Stock")

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
    texto = input(mensaje).strip()
    if validar_formato(texto):
        return int(texto)
    else:
        print("Ingrese un numero entero.")
        return PedirEntero(mensaje)
    
def PedirNombre(mensaje):
    nombre = input(mensaje).strip().lower()
    if nombre != "":
        return nombre
    else:
        print("El nombre no puede estar vacio.")
        return PedirNombre(mensaje)
    
def PedirPrecio(mensaje):
    try:
        precio = float(input(mensaje))
    except ValueError:
        print("Ingrese un precio numerico.")
        return PedirPrecio(mensaje)
    if precio > 0:
        return precio
    else:
        print("El precio debe ser mayor que cero.")
        return PedirPrecio(mensaje)
    
def VerificarFormatoFecha(dia, mes, año):
    if año < 2026 or mes < 1 or mes > 12:
        return False
    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
            max_dias = 29
        else:
            max_dias = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        max_dias = 30
    else:
        max_dias = 31
    if dia < 1 or dia > max_dias:
        return False
    return True

def Armar_Fecha_Completa(dia, mes, año):
    return str(dia) + "/" + str(mes) + "/" + str(año)

def PedirFecha():
    dia = PedirEntero("Ingrese el dia del mes: ")
    mes = PedirEntero("Ingrese el mes: ")
    año = PedirEntero("Ingrese el año: ")
    if VerificarFormatoFecha(dia, mes, año):
        return Armar_Fecha_Completa(dia, mes, año)
    else:
        print("La fecha ingresada no es valida.")
        return PedirFecha()
    
def VerEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock):
    '''Imprime la lista de espectaculos registrados con sus fechas, precios y stock'''
    print()
    print("============ ESPECTACULOS =============")
    numero = 1
    for espectaculo in listaEspectaculos:
        print("   " + str(numero) + "- [ " + espectaculo + " - " + listaFechas[espectaculo] + " - $" + str(listaPrecios[espectaculo]) + " - Stock: " + str(listaStock[espectaculo]) + " ]")
        numero = numero + 1
    if len(listaEspectaculos) == 0:
        print()
        print("No se ingresaron espectaculos")
        print()
    print("=======================================")
    print()

def AgregarEspectaculo(listaEspectaculos, listaFechas, listaPrecios, listaStock, nombre, fecha, precio, stock=1):
    listaEspectaculos[nombre] = nombre
    listaFechas[nombre] = fecha
    listaPrecios[nombre] = precio
    listaStock[nombre] = stock

def IngresarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock):
    espectaculo = PedirNombre("Ingrese el Espectaculo: ")
    if espectaculo in listaEspectaculos:
        print("Ya existe un espectaculo con ese nombre.")
        return
    fecha = PedirFecha()
    precio = PedirPrecio("Ingrese el precio de la entrada para el espectaculo: ")
    AgregarEspectaculo(listaEspectaculos, listaFechas, listaPrecios, listaStock, espectaculo, fecha, precio)
    print("Espectaculo ingresado.")

def EliminarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock):
    espectaculo = PedirNombre("Ingrese el espectaculo que desea eliminar: ")
    if espectaculo not in listaEspectaculos:
        print("No se encontro el espectaculo.")
        return
    del listaEspectaculos[espectaculo]
    del listaFechas[espectaculo]
    del listaPrecios[espectaculo]
    del listaStock[espectaculo]
    print("Espectaculo eliminado.")

def ActualizarNombreEnCompras(listaCompras, viejo, nuevo, inicio=0):
    '''Reemplaza el nombre viejo por el nuevo en las compras ya realizadas'''
    if inicio < len(listaCompras):
        if listaCompras[inicio] == viejo:
            listaCompras[inicio] = nuevo
        ActualizarNombreEnCompras(listaCompras, viejo, nuevo, inicio + 1)

def ModificarNombre(listaEspectaculos, listaFechas, listaPrecios, listaStock, listaCompras, viejo):
    nuevo = PedirNombre("Ingrese el nombre nuevo del espectaculo: ")
    if nuevo != viejo and nuevo in listaEspectaculos:
        print("Ya existe un espectaculo con ese nombre.")
        return
    if nuevo != viejo:
        listaEspectaculos[nuevo] = nuevo
        listaFechas[nuevo] = listaFechas[viejo]
        listaPrecios[nuevo] = listaPrecios[viejo]
        listaStock[nuevo] = listaStock[viejo]
        del listaEspectaculos[viejo]
        del listaFechas[viejo]
        del listaPrecios[viejo]
        del listaStock[viejo]
        # Se actualiza el nombre en las compras ya realizadas
        ActualizarNombreEnCompras(listaCompras, viejo, nuevo)
    print("Nombre modificado.")

def ModificarFecha(listaFechas, espectaculo):
    print("A continuacion ingrese nuevamente la fecha:")
    listaFechas[espectaculo] = PedirFecha()

def ModificarPrecio(listaPrecios, espectaculo):
    print("Ingrese a continuacion el nuevo precio:")
    listaPrecios[espectaculo] = PedirPrecio("Ingresar precio: ")

def ModificarStock(listaStock, espectaculo):
    subopcion = PedirEntero("Ingrese 1 para cambiar el stock o 2 para sumar stock: ")
    while subopcion != 1 and subopcion != 2:
        print("Opcion inexistente.")
        subopcion = PedirEntero("Ingrese 1 para cambiar el stock o 2 para sumar stock: ")
    cantidad = PedirEntero("Ingrese la cantidad de entradas: ")
    while cantidad < 1:
        print("El stock debe ser como minimo 1.")
        cantidad = PedirEntero("Ingrese la cantidad de entradas: ")
    if subopcion == 1:
        listaStock[espectaculo] = cantidad
    else:
        listaStock[espectaculo] = listaStock[espectaculo] + cantidad

def ModificarEspectaculo(listaEspectaculos, listaFechas, listaPrecios, listaStock, listaCompras):
    espectaculo = PedirNombre("¿Que espectaculo desea modificar?: ")
    if espectaculo not in listaEspectaculos:
        print("No se encontro el espectaculo.")
        return
    MenuModificaciones()
    opcion = PedirEntero("Ingrese una opcion: ")
    while opcion < 1 or opcion > 4:
        print("Opcion inexistente.")
        opcion = PedirEntero("Ingrese una opcion: ")
    if opcion == 1:
        ModificarNombre(listaEspectaculos, listaFechas, listaPrecios, listaStock, listaCompras, espectaculo)
    elif opcion == 2:
        ModificarFecha(listaFechas, espectaculo)
    elif opcion == 3:
        ModificarPrecio(listaPrecios, espectaculo)
    else:
        ModificarStock(listaStock, espectaculo)

def VenderEntradas(listaEspectaculos, listaPrecios, listaStock, listaClientes, listaCompras, listaCantidades):
    '''Registra la venta de entradas a un cliente y descuenta el stock'''
    espectaculo = PedirNombre("Ingrese el espectaculo del que desea comprar entradas: ")
    if espectaculo not in listaEspectaculos:
        print("No se encontro el espectaculo.")
        return
    if listaStock[espectaculo] == 0:
        print("No quedan entradas disponibles para este espectaculo.")
        return
    cliente = PedirNombre("Ingrese el nombre del cliente: ")
    cantidad = PedirEntero("Ingrese la cantidad de entradas: ")
    while cantidad < 1 or cantidad > listaStock[espectaculo]:
        print("La cantidad debe ser de al menos 1 y no puede superar el stock (" + str(listaStock[espectaculo]) + ").")
        cantidad = PedirEntero("Ingrese la cantidad de entradas: ")
    listaStock[espectaculo] = listaStock[espectaculo] - cantidad
    listaClientes.append(cliente)
    listaCompras.append(espectaculo)
    listaCantidades.append(cantidad)
    total = listaPrecios[espectaculo] * cantidad
    print("Venta realizada. Total a pagar: $" + str(total))

def ImprimirClientes(listaClientes, listaCompras, listaCantidades, inicio=0):
    '''Imprime un cliente por linea, recorriendo la lista de forma recursiva'''
    if inicio < len(listaClientes):
        numero = str(inicio + 1)
        print("   " + numero + "- [ " + listaClientes[inicio] + " - " + listaCompras[inicio] + " - Entradas: " + str(listaCantidades[inicio]) + " ]")
        ImprimirClientes(listaClientes, listaCompras, listaCantidades, inicio + 1)

def VerClientes(listaClientes, listaCompras, listaCantidades):
    '''Imprime la lista de clientes con el espectaculo y la cantidad de entradas compradas'''
    print()
    print("============== CLIENTES ===============")
    ImprimirClientes(listaClientes, listaCompras, listaCantidades)
    if len(listaClientes) == 0:
        print()
        print("No se registraron clientes")
        print()
    print("=======================================")
    print()

def GuardarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock):
    with open("espectaculos.txt", "w", encoding="utf-8") as archivo:
        for espectaculo in listaEspectaculos:
            archivo.write(espectaculo + "\n")
            archivo.write(listaFechas[espectaculo] + "\n")
            archivo.write(str(listaPrecios[espectaculo]) + "\n")
            archivo.write(str(listaStock[espectaculo]) + "\n")

def CargarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock):
    try:
        with open("espectaculos.txt", "r", encoding="utf-8") as archivo:
            while True:
                nombre = archivo.readline().strip()
                if nombre == "":
                    break
                fecha = archivo.readline().strip()
                precio = float(archivo.readline())
                stock = int(archivo.readline())
                AgregarEspectaculo(listaEspectaculos, listaFechas, listaPrecios, listaStock, nombre, fecha, precio, stock)
    except FileNotFoundError:
        print("No existe el archivo, se inicia vacio.")

def GuardarClientes(listaClientes, listaCompras, listaCantidades):
    with open("clientes.txt", "w", encoding="utf-8") as archivo:
        for i in range(len(listaClientes)):
            archivo.write(listaClientes[i] + "\n")
            archivo.write(listaCompras[i] + "\n")
            archivo.write(str(listaCantidades[i]) + "\n")

def CargarClientes(listaClientes, listaCompras, listaCantidades):
    try:
        with open("clientes.txt", "r", encoding="utf-8") as archivo:
            while True:
                cliente = archivo.readline().strip()
                if cliente == "":
                    break
                espectaculo = archivo.readline().strip()
                cantidad = int(archivo.readline())
                listaClientes.append(cliente)
                listaCompras.append(espectaculo)
                listaCantidades.append(cantidad)
    except FileNotFoundError:
        print("No existe el archivo de clientes, se inicia vacio.")
        
def Programa():
    listaEspectaculos = {}
    listaFechas = {}
    listaPrecios = {}
    listaStock = {}
    listaClientes = []
    listaCompras = []
    listaCantidades = []
    terminar = False
    CargarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
    CargarClientes(listaClientes, listaCompras, listaCantidades)
    while not terminar:
        Menu()
        opcion = PedirEntero("Ingresar una opcion: ")
        print("-----------------------------------------------------------------------")
        while opcion > 7 or opcion < 1:
            Menu()
            opcion = PedirEntero("Error. La opcion ingresada no existe, intente de nuevo: ")
        if opcion == 1:
            VerEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        elif opcion == 2:
            IngresarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        elif opcion == 3:
            EliminarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        elif opcion == 4:
            ModificarEspectaculo(listaEspectaculos, listaFechas, listaPrecios, listaStock, listaCompras)
        elif opcion == 5:
            VenderEntradas(listaEspectaculos, listaPrecios, listaStock, listaClientes, listaCompras, listaCantidades)
        elif opcion == 6:
            VerClientes(listaClientes, listaCompras, listaCantidades)
        else:
            print("Terminando programa...")
            terminar = True
        GuardarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        GuardarClientes(listaClientes, listaCompras, listaCantidades)
try:
    Programa()
except (EOFError, KeyboardInterrupt):
    print("\nTerminando programa...")