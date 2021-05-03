class Persona:

    def __init__(self,nombre,apellido,edad,fn,sexo,usuario,contra,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fn = fn
        self.sexo = sexo
        self.usuario = usuario
        self.contra = contra
        self.telefono = telefono

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad
    
    def getApellido(self):
        return self.apellido

    def getfn(self):
        return self.fn

    def getusuario(self):
        return self.usuario
    
    def getSexo(self):
        return self.sexo    

    def getTelefono(self):
        return self.telefono
    
    def getContra(self):
        return self.contra

    def setNombre(self,nombre):
        self.nombre = nombre

    def setEdad(self,edad):
        self.edad = edad
    
    def setApellido(self,apellido):
        self.apellido = apellido

    def setFn(self,fn):
        self.fn = fn

    def setSexo(self,sexo):
        self.sexo = sexo
    
    def setUsuario(self,usuario):
        self.usuario = usuario

    def setContra(self,contra):
        self.contra = contra
    
    def setTelefono(self,telefono):
        self.telefono = telefono
        