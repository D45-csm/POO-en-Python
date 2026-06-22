class Usuario:
    def __init__(self,IDe, nombre, rol, correo, contraseña, activo):
        self._IDe= IDe
        self.nombre=nombre
        self._activo=activo
        self.rol=rol
        self.correo= correo
        self.__contraseña=contraseña

    def get_activo(self):
         return self._activo
         
    def iniciar_sesion(self, nom, contra):
        if self.nombre== nom and self.__contraseña==contra:
            self._activo= True 
            print("Inicio de Sesion exitoso ✅")
            return self._activo
        else:
            self._activo= False 
            print("📛 datos incorrectos, no se ha logrado iniciar sesion")
            return self._activo

    def cerrar_sesion(self):
            self._activo= False 
            print("sesion cerrada correctamente ✅")
            return self._activo

usuario1= Usuario(1,"Daniel", "supervisor","acos@gmail.com", "12345", False)

nombre= input("introduce tu nombre: ")
contraseña= input("introduce tu contraseña: ")

usuario1.iniciar_sesion(nombre, contraseña)


if usuario1.get_activo():
    decision=input("desea cerrar sesion?: ")
    if decision=="si":
        usuario1.cerrar_sesion()

