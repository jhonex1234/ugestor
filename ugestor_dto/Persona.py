

class Persona:
	"""docstring for ClassName"""
	def __init__(self, cedula, nombre, apellido, fechaNacimiento, sexo):
		self.__cedula = cedula
		self.__nombre = nombre 
		self.__apellido = apellido
		self.__fechaNacimiento = fechaNacimiento
		self.__sexo = sexo

	def  getCedula(self):
		return self.__cedula

	def setCedula(self, cedula):
		self.__cedula = cedula

	def setNombre(self, nombre):
		self.__nombre = nombre
	
	def getNombre(self):
		return self.__nombre

	def setApellido(self, apellido):
		self.__apellido = apellido
	
	def getApellido(self):
		return self.__apellido	

	def setFechaNacimiento(self, fechaNacimiento):
		self.__fechaNacimiento = fechaNacimiento
	
	def getFechaNacimiento(self):
		return self.__fechaNacimiento

	def setSexo(self, sexo):
		self.__sexo = sexo
	
	def getSexo(self):
		return self.__sexo
