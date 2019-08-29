

class Persona:
	"""docstring for ClassName"""
	def __init__(self, id, documento, nombre, tipoDocumento, apellido, paisOrigen, fechaNacimiento, sexo):
		self.__id = id
		self.__documento = documento
		self.__nombre = nombre
		self.__tipoDocumento =  tipoDocumento
		self.__apellido = apellido
		self.__paisOrigen = paisOrigen
		self.__fechaNacimiento = fechaNacimiento
		self.__sexo = sexo
		
	def getId(self):
		return self.__id

	def setId(self, id):
		self.__id = id

	def getDocumento(self):
		return self.__documento

	def setDocumento(self, documento):
		self.__documento = documento

	def setNombre(self, nombre):
		self.__nombre = nombre
	
	def getNombre(self):
		return self.__nombre

	def gettipoDocumento(self):
		return self.__tipoDocumento

	def settipoDocumento(self, tipoDocumento):
		self.__tipoDocumento = tipoDocumento

	def setApellido(self, apellido):
		self.__apellido = apellido
	
	def getApellido(self):
		return self.__apellido	

	def getPaisOrigen(self):
		return self.__paisOrigen

	def setPaisOrigen(self, paisOrigen):
		self.__paisOrigen = paisOrigen

	def setFechaNacimiento(self, fechaNacimiento):
		self.__fechaNacimiento = fechaNacimiento
	
	def getFechaNacimiento(self):
		return self.__fechaNacimiento

	def setSexo(self, sexo):
		self.__sexo = sexo
	
	def getSexo(self):
		return self.__sexo
