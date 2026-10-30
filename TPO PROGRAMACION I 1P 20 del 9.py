# Sistema de Venta de entradas para Espectaculos

def Menu():
    print()
    print("================= MENU =================")
    print("  1 - Ingresar Espectaculo")
    print("  2 - Eliminar Espectaculo")
    print("  3 - Modificar Espectaculo")
    print("  4 - Salir")
    print("========================================")


def MenuModificaciones():
    print("1 - Nombre")
    print("2 - Fecha")
    print("3 - Precio de entrada")
    print("4 - Stock")


def PedirEntero(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            return int(texto)
        except ValueError:
            print("Ingrese un numero entero.")


def PedirNombre(mensaje):
    while True:
        nombre = input(mensaje).strip().lower()
        if nombre != "":
            return nombre
        print("El nombre no puede estar vacio.")


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
    while True:
        dia = PedirEntero("Ingrese el dia del mes: ")
        mes = PedirEntero("Ingrese el mes: ")
        año = PedirEntero("Ingrese el año: ")
        if VerificarFormatoFecha(dia, mes, año):
            return Armar_Fecha_Completa(dia, mes, año)
        print("La fecha ingresada no es valida.")


def PedirPrecio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))
        except ValueError:
            print("Ingrese un precio numerico.")
            continue

        if precio > 0:
            return precio
        print("El precio debe ser mayor que cero.")


def AgregarEspectaculo(listae, listaf, listap, listadestock,nombre, fecha, precio, stock=1):
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


def ModificarNombre(listaEspec, lfecha, lprecios, listastock, viejo):
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


def ModificarEspectaculo(listaEspec, lfecha, lprecios, listastock):
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
        ModificarNombre(listaEspec, lfecha, lprecios, listastock, espectaculo)
    elif opcion == 2:
        ModificarFecha(lfecha, espectaculo)
    elif opcion == 3:
        ModificarPrecio(lprecios, espectaculo)
    else:
        ModificarStock(listastock, espectaculo)


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
                AgregarEspectaculo(listae, listaf, listap, listadestock,nombre, fecha, precio, stock)
    except FileNotFoundError:
        print("No existe el archivo, se inicia vacio.")


def Programa():
    listaEspectaculos = {}
    listaFechas = {}
    listaPrecios = {}
    listaStock = {}
    terminar = False

    CargarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
    while not terminar:
        Menu()
        opcion = PedirEntero("Ingresar alguna de las opciones disponibles: ")
        while opcion < 1 or opcion > 4:
            print("Opcion inexistente.")
            opcion = PedirEntero("Ingresar alguna de las opciones disponibles: ")

        if opcion == 1:
            IngresarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        elif opcion == 2:
            EliminarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        elif opcion == 3:
            ModificarEspectaculo(listaEspectaculos, listaFechas, listaPrecios, listaStock)
        else:
            print("Terminando programa...")
            terminar = True
        GuardarEspectaculos(listaEspectaculos, listaFechas, listaPrecios, listaStock)


try:
    Programa()
except (EOFError, KeyboardInterrupt):
    print("\nTerminando programa...")
