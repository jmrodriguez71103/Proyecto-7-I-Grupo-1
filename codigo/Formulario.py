#import mysql.connector
class SIC():
  d

class usuario(SIC):
  def cargarUsuario():
    Psw= input("Ingrese la contraseña:")
    Usr= input("Ingrese el nombre del usuario")
    Dni= input("Ingrese el DNI del usuario")

class cliente(SIC):
  def cargarUsuario():
    ID_Cliente= int(input("Ingrese el ID del cliente"))
    Nombre= input("Ingrese elnombre del cliente")
    Apellido= input("Ingrese el apellido del cliente")
    DNI= input("Ingrese el documento del cliente")
    Direccion= input("Ingrese la direccion del cliente")
    Mail= input("Ingrese el Mail del cliente")
    Telefono= input("Ingrese el telefono del cliente")
    ID_Caso= int(input("Ingrese la ID del caso"))

    


class caso(SIC):
  def cargarCaso ():
    ID_caso= int(input("Ingrese el ID del caso"))
    ID_cliente= int(input("Ingrese el ID del cliente"))
    tipo= input("Ingrese el tipo de caso")
    fecha_inicio= input("Ingrese la fecha de inicio del caso")
    fecha_fin= input("ingrese la fecha del fin del caso")
    ID_etapa= int(input("Ingrese el ID de la etapa"))
    motivo= input("Ingrese el motivo del caso")

class etapas_dos(SIC):
  def cargarEtapados():
    ID_etapa= int(input("Ingrese la ID de la etapa"))
    ID_caso= int(input("Ingrese el ID del caso"))
    firma= input("Ingrese la firma")
    fecha_firma= int(input("Ingrese la fecha de la firma"))
    lugar_firma= input("Ingrese el lugar de la firma")

class etapa_tres(SIC):
  def cargareEtapatres():
    ID_etapa=
    fecha_inicio_E3= int(input("Ingrese fecha de inicio"))
    fecha_cierre_E3= int(input("Ingrese fecha de cierre"))
    fecha_comision= int(input("Ingrese fecha de comision"))
    presenta_despacho= input("Presenetó el documento de pronto despacho?")
    fecha_dictamen=int(input("Ingrese fecha de dictamen"))
    fecha_conciliacion=int(input("Ingrese fecha de conciliacion"))


class etapa_cuatro(SIC):
  def cargarEtapacuatro():
    ID_etapa=
    etapa_inicio= input("Ha iniciado la etapa inicio?")
    etapa_intermedia= input("Ha iniciado la etapa intermedia?")
    etapa_final= input("Ha iniciado la etapa final?")
    fecha_inicio= int(input("Ingrese la fecha de incio de la etapa inical"))
    fecha_intermedia= int(input("Ingrese la fecha de incio de la etapa intermedia"))
    fecha_final= int(input("Ingrese la fecha de incio de la etapa final"))
    
