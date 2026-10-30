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


def VerEspectaculos(listae, listaf, listap, listadestock):
    '''Imprime la lista de espectaculos registrados con sus fechas, precios y stock'''
    print()
    print("============ ESPECTACULOS =============")
    numero = 1
    for espectaculo in listae:
        print("   " + str(numero) + "- [ " + espectaculo + " - " + listaf[espectaculo] + " - $" + str(listap[espectaculo]) + " - Stock: " + str(listadestock[espectaculo]) + " ]")
        numero = numero + 1
    if len(listae) == 0:
        print()
        print("No se ingresaron espectaculos")
        print()
    print("=======================================")
    print()


def AgregarEspectaculo(listae, listaf, listap, listadestock, nombre, fecha, precio, stock=1):
    listae[nombre] = nombre
    listaf[nombre] = fecha
    listap[nombre] = precio
    listadestock[nombre] = stock


def IngresarEspectaculos(listae, listaf, listap, listadestock):
    espectaculo = PedirNombre("Ingrese el Espectaculo: ")
    if espectaculo in listae:
        print("Ya existe un espectaculo con ese nombre.")
        return

    fecha = PedirFecha()
    precio = PedirPrecio("Ingrese el precio de la entrada para el espectaculo: ")
    AgregarEspectaculo(listae, listaf, listap, listadestock, espectaculo, fecha, precio)
    print("Espectaculo ingresado.")


def EliminarEspectaculos(listae, listaf, listap, listadestock):
    espectaculo = PedirNombre("Ingrese el espectaculo que desea eliminar: ")
    if espectaculo not in listae:
        print("No se encontro el espectaculo.")
        return

    del listae[espectaculo]
    del listaf[espectaculo]
    del listap[espectaculo]
    del listadestock[espectaculo]
    print("Espectaculo eliminado.")


def ActualizarNombreEnCompras(listacompras, viejo, nuevo, inicio=0):
    '''Reemplaza el nombre viejo por el nuevo en las compras ya realizadas'''
    if inicio < len(listacompras):
        if listacompras[inicio] == viejo:
            listacompras[inicio] = nuevo
        ActualizarNombreEnCompras(listacompras, viejo, nuevo, inicio + 1)


def ModificarNombre(listaEspec, lfecha, lprecios, listastock, listacompras, viejo):
    nuevo = PedirNombre("Ingrese el nombre nuevo del espectaculo: ")
    if nuevo != viejo and nuevo in listaEspec:
        print("Ya existe un espectaculo con ese nombre.")
        return

    if nuevo != viejo:
        listaEspec[nuevo] = nuevo
        lfecha[nuevo] = lfecha[viejo]
        lprecios[nuevo] = lprecios[viejo]
        listastock[nuevo] = listastock[viejo]
        del listaEspec[viejo]
        del lfecha[viejo]
        del lprecios[viejo]
        del listastock[viejo]
        # Se actualiza el nombre en las compras ya realizadas
        ActualizarNombreEnCompras(listacompras, viejo, nuevo)
    print("Nombre modificado.")


def ModificarFecha(lfecha, espectaculo):
    print("A continuacion ingrese nuevamente la fecha:")
    lfecha[espectaculo] = PedirFecha()


def ModificarPrecio(lprecios, espectaculo):
    print("Ingrese a continuacion el nuevo precio:")
    lprecios[espectaculo] = PedirPrecio("Ingresar precio: ")


def ModificarStock(listastock, espectaculo):
    subopcion = PedirEntero("Ingrese 1 para cambiar el stock o 2 para sumar stock: ")
    while subopcion != 1 and subopcion != 2:
        print("Opcion inexistente.")
        subopcion = PedirEntero("Ingrese 1 para cambiar el stock o 2 para sumar stock: ")

    cantidad = PedirEntero("Ingrese la cantidad de entradas: ")
    while cantidad < 1:
        print("El stock debe ser como minimo 1.")
        cantidad = PedirEntero("Ingrese la cantidad de entradas: ")

    if subopcion == 1:
        listastock[espectaculo] = cantidad
    else:
        listastock[espectaculo] = listastock[espectaculo] + cantidad


def ModificarEspectaculo(listaEspec, lfecha, lprecios, listastock, listacompras):
    espectaculo = PedirNombre("¿Que espectaculo desea modificar?: ")
    if espectaculo not in listaEspec:
        print("No se encontro el espectaculo.")
        return

    MenuModificaciones()
    opcion = PedirEntero("Ingrese una opcion: ")
    while opcion < 1 or opcion > 4:
        print("Opcion inexistente.")
        opcion = PedirEntero("Ingrese una opcion: ")

    if opcion == 1:
        ModificarNombre(listaEspec, lfecha, lprecios, listastock, listacompras, espectaculo)
    elif opcion == 2:
        ModificarFecha(lfecha, espectaculo)
    elif opcion == 3:
        ModificarPrecio(lprecios, espectaculo)
    else:
        ModificarStock(listastock, espectaculo)


def VenderEntradas(listae, listap, listadestock, listaclientes, listacompras, listacantidades):
    '''Registra la venta de entradas a un cliente y descuenta el stock'''
    espectaculo = PedirNombre("Ingrese el espectaculo del que desea comprar entradas: ")
    if espectaculo not in listae:
        print("No se encontro el espectaculo.")
        return

    if listadestock[espectaculo] == 0:
        print("No quedan entradas disponibles para este espectaculo.")
        return

    cliente = PedirNombre("Ingrese el nombre del cliente: ")
    cantidad = PedirEntero("Ingrese la cantidad de entradas: ")
    while cantidad < 1 or cantidad > listadestock[espectaculo]:
        print("La cantidad debe ser de al menos 1 y no puede superar el stock (" + str(listadestock[espectaculo]) + ").")
        cantidad = PedirEntero("Ingrese la cantidad de entradas: ")

    listadestock[espectaculo] = listadestock[espectaculo] - cantidad
    listaclientes.append(cliente)
    listacompras.append(espectaculo)
    listacantidades.append(cantidad)
    total = listap[espectaculo] * cantidad
    print("Venta realizada. Total a pagar: $" + str(total))


def ImprimirClientes(listaclientes, listacompras, listacantidades, inicio=0):
    '''Imprime un cliente por linea, recorriendo la lista de forma recursiva'''
    if inicio < len(listaclientes):
        numero = str(inicio + 1)
        print("   " + numero + "- [ " + listaclientes[inicio] + " - " + listacompras[inicio] + " - Entradas: " + str(listacantidades[inicio]) + " ]")
        ImprimirClientes(listaclientes, listacompras, listacantidades, inicio + 1)


def VerClientes(listaclientes, listacompras, listacantidades):
    '''Imprime la lista de clientes con el espectaculo y la cantidad de entradas compradas'''
    print()
    print("============== CLIENTES ===============")
    ImprimirClientes(listaclientes, listacompras, listacantidades)
    if len(listaclientes) == 0:
        print()
        print("No se registraron clientes")
        print()
    print("=======================================")
    print()


def GuardarEspectaculos(listae, listaf, listap, listadestock):
    with open("espectaculos.txt", "w", encoding="utf-8") as archivo:
        for espectaculo in listae:
            archivo.write(espectaculo + "\n")
            archivo.write(listaf[espectaculo] + "\n")
            archivo.write(str(listap[espectaculo]) + "\n")
            archivo.write(str(listadestock[espectaculo]) + "\n")


def CargarEspectaculos(listae, listaf, listap, listadestock):
    try:
        with open("espectaculos.txt", "r", encoding="utf-8") as archivo:
            while True:
                nombre = archivo.readline().strip()
                if nombre == "":
                    break

                fecha = archivo.readline().strip()
                precio = float(archivo.readline())
                stock = int(archivo.readline())
                AgregarEspectaculo(listae, listaf, listap, listadestock, nombre, fecha, precio, stock)
    except FileNotFoundError:
        print("No existe el archivo, se inicia vacio.")


def GuardarClientes(listaclientes, listacompras, listacantidades):
    with open("clientes.txt", "w", encoding="utf-8") as archivo:
        for i in range(len(listaclientes)):
            archivo.write(listaclientes[i] + "\n")
            archivo.write(listacompras[i] + "\n")
            archivo.write(str(listacantidades[i]) + "\n")


def CargarClientes(listaclientes, listacompras, listacantidades):
    try:
        with open("clientes.txt", "r", encoding="utf-8") as archivo:
            while True:
                cliente = archivo.readline().strip()
                if cliente == "":
                    break

                espectaculo = archivo.readline().strip()
                cantidad = int(archivo.readline())
                listaclientes.append(cliente)
                listacompras.append(espectaculo)
                listacantidades.append(cantidad)
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
        if opcion == 2:
            IngresarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        if opcion == 3:
            EliminarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        if opcion == 4:
            ModificarEspectaculo(listaEspectaculos, listaFechas, listaPrecios, listaStock, listaCompras)
        if opcion == 5:
            VenderEntradas(listaEspectaculos, listaPrecios, listaStock, listaClientes, listaCompras, listaCantidades)
        if opcion == 6:
            VerClientes(listaClientes, listaCompras, listaCantidades)
        if opcion == 7:
            print("Terminando programa...")
            terminar = True
        GuardarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        GuardarClientes(listaClientes, listaCompras, listaCantidades)


try:
    Programa()
except (EOFError, KeyboardInterrupt):
    print("\nTerminando programa...")