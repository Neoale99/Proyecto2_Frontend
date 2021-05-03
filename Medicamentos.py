class Medicamentos:
    def __init__(self,nombre,precio,descripcion,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad

    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio    

    def getDescripcion(self):
        return self.descripcion
    
    def getCantidad(self):
        return self.cantidad

    def setNombre(self,nombre):
        self.nombre = nombre

    def setEdad(self,precio):
        self.precio = precio
    
    def setApellido(self,descripcion):
        self.descripcion = descripcion

    def setFn(self,cantidad):
        self.cantidad = cantidad 