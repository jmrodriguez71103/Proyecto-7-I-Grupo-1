class usuario():

  def __init__ (self, NUsuario, DNI, Psw):
    self.Nusuario = NUsuario
    self.DNI = DNI
    self.Psw = Psw

  def cargarUsuario():
    Psw= input("Ingrese la contraseña: ")
    Usr= input("Ingrese el nombre del usuario: ")
    Dni= input("Ingrese el DNI del usuario: ")
    Usuarios.update({Dni:Psw})
    Usuario1= usuario(Usr, Dni, Psw)

  
  def ValidarUsuario (DNI, Psw):
    if DNI in Usuarios:
      x = Usuarios.pop(DNI)
      if x == Psw:
        Usuarios.update({DNI:Psw})
        print ("Login realizado exitosamente")
      else:
        Usuarios.update({DNI:Psw})
        print ("Contraseña incorrecta")
    else:
      print("DNI incorrecto")



usuario.cargarUsuario ()
usuario.ValidarUsuario ("45320127", "123")
