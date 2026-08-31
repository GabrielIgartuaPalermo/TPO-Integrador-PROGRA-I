#Modulos
from datetime import datetime
#Sistema de Venta de entradas para Espectaculos
#FUNCIONES
def GuardarPrecioEntrada (Precio,Precios=[]):
    Precios.append(Precio)
    return Precios
def Menu ():
    print("1-Ver espectaculos")
    print("2-Comprar tickets")
    print("3-Ver clientes")
    
    return
#Profesor esta hecho con IA esta funcion
def VerificarFormatoFecha(FechaE):
    es_valida = False
    while not es_valida:
        FechaE = input("Ingresar fecha que cumpla el formato(D/M/A):")
        try:
            fecha_obj = datetime.strptime(FechaE, "%d/%m/%Y")
            es_valida = True  
            print("La fecha respeta el formato D/M/A y es válida.")
        except ValueError:
            print("Formato o fecha inválida. Intentá de nuevo.\n")
    
    return FechaE
def GuardarFechaEspectaculo (FechaE,Espectaculos=[]):
    Espectaculos.append(FechaE)
    return 
#Listas 
Clientes = []
ListadePreciosdeEntradas = [] 
Lista_EspectaculosEspectaculos = [] 
Fechas_Espectaculos = [] 
#MAIN
seguir = "Si"
while seguir != "No":
    Menu() 
    precioEntrada = float(input("Ingresar precio: "))
    Fecha = input("Ingresar fecha segun formato (D/M/A (Respetar / cuando escribes la fecha) ): ")
    Opcion = int(input("Ingresar una opcion"))
    GuardarPrecioEntrada(precioEntrada,ListadePreciosdeEntradas)
    GuardarFechaEspectaculo(Fecha,Fechas_Espectaculos)
    VerificarFormatoFecha(Fecha)
    seguir = input("Deseas seguir? (Ingrese Si para seguir o No para no seguir:")
    if seguir == "Si":
        print("Continuamos")
    else:
        print("Terminando programa...")
        seguir = "No"