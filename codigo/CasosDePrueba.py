class Test ():

def T1ValidarDNIyPsw (self):
	app= app()
	app.ValidarUsuario(45320127, "AA@@21")

def T2ValidarDNIyPsw (self):
	app=app()
	app.ValidarUsuario(45320127, "a")

def T3ValidarDNIyPsw (self):
	app=app()
	app.ValidarUsuario(1, "AA@@21")


def T4ValidarDNIyPsw (self):
	app=app()
	app.ValidarUsuario()




#Nombre, Apellido, DNI, Dirección, Teléfono, Mail.

def T1NuevoCliente (self):
	app=app()#Todo bien
	app.NuevoCliente("Juan", "Rodriguez", 45320127, "Calle 1 N°1", 1224324234, "aaa@gmail.com")

def T2NuevoCliente (self):
	app=app()#Sin Nombre
	app.NuevoCliente("Rodriguez", 45320127, "Calle 1 N°1", 1224324234, "aaa@gmail.com")

def T3NuevoCliente (self):
	app=app()#Mal Nombre
	app.NuevoCliente(1, "Rodriguez", 45320127, "Calle 1 N°1", 1224324234, "aaa@gmail.com")

def T4NuevoCliente (self):
	app=app()#Sin Apellido
	app.NuevoCliente("Juan", 45320127, "Calle 1 N°1", 1224324234, "aaa@gmail.com")

def T5NuevoCliente (self):
	app=app()#Mal Apellido
	app.NuevoCliente("Juan", 2, 45320127, "Calle 1 N°1", 1224324234, "aaa@gmail.com")

def T6NuevoCliente (self):
	app=app()#Sin DNI
	app.NuevoCliente("Juan", "Rodriguez", "Calle 1 N°1", 1224324234, "aaa@gmail.com"")

def T7NuevoCliente (self):
	app=app()#Mal DNI
	app.NuevoCliente("Juan", "Rodriguez", *12133422, "Calle 1 N°1", 1224324234, "aaa@gmail.com")

def T8NuevoCliente (self):
	app=app()#Sin Dirección
	app.NuevoCliente("Juan", "Rodriguez", 45320127, 1224324234, "aaa@gmail.com")

def T9NuevoCliente (self):
	app=app()#Sin Teléfono
	app.NuevoCliente("Juan", "Rodriguez", 45320127, "Calle 1 N°1", "aaa@gmail.com")

def T10NuevoCliente (self):
	app=app()#Mal Teléfono
	app.NuevoCliente("Juan", "Rodriguez", 45320127, "Calle 1 N°1", *1224324234, "aaa@gmail.com")

def T11NuevoCliente (self):
	app=app()#Sin Mail
	app.NuevoCliente("Juan", "Rodriguez", 45320127, "Calle 1 N°1", 1224324234)

#Tipo, Fecha-Inicio, Fecha-Fin, Motivo

def T1NuevoCaso (self):
	app=app()#Todo bien
	app.NuevoCaso("Divorcio", 2022-06-10, "Discrepancia")

def T2NuevoCaso (self):
	app=app()#Sin Tipo
	app.NuevoCaso(2022-06-10, "Discrepancia")

def T3NuevoCaso (self):
	app=app()#Mal Tipo
	app.NuevoCaso(*2312, 2022-06-10, "Discrepancia")

def T4NuevoCaso (self):
	app=app()#Sin Fecha
	app.NuevoCaso("Divorcio", "Discrepancia")

def T5NuevoCaso (self):
	app=app()#Mal Fecha
	app.NuevoCaso("Divorcio", 20222-06-10, "Discrepancia")

def T6NuevoCaso (self):
	app=app()#Sin Motivo
	app.NuevoCaso("Divorcio", 2022-06-10)

def T7NuevoCaso (self):
	app=app()#Mal Motivo
	app.NuevoCaso("Divorcio", 2022-06-10, *332)


