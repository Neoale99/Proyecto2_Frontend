class Admin:
    nombre = "Abner"
    apellido = "Cardona"
    usuario = "admin"
    contra = "1234"
    def __init__(self,nombre,apellido,usuario,contra):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contra = contra
  

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getusuario(self):
        return self.usuario
    
    def getContra(self):
        return self.contra

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setApellido(self,apellido):
        self.apellido = apellido

    def setUsuario(self,usuario):
        self.usuario = usuario

    def setContra(self,contra):
        self.contra = contra

        