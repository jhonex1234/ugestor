from Persona import Persona


class Disenador(Persona):
	def __init__(self, paisOrigen,pasaporte,id):
		super().__init__(self, id, cedula, nombre, apellido, fechaNacimiento, sexo)
		self.__id = id
		self.__pasaporte = pasaporte
		self.__paisOrigen = paisOrigen

  	def  getid(id):
    	return self.id

    def setid(self, id):
     	self.__id = id

    def  getpasaporte(pasaporte):
    	return self.pasaporte

    def setpasaporte(self, pasaporte):
     	self.__pasaporte = pasaporte

    def  getpasaporte(pasaporte):
       return self.pasaporte

    def setpasaporte(self, pasaporte):
    	self.__pasaporte = pasaporte
        
