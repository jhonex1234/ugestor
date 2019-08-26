class Agencia:
	"""docstring for ClassName"""
	def __init__(self, id, nombre, anocreacion, sedeproncipal, idPersona, correoElectronico, relacionesOtrasAgencias, CodAgencia):
		self.__id = id
		self.__nombre = nombre
		self.__anoCreacion = anocreacion 
		self.__sedePrincipal = sedeproncipal
		self.__idPersona = idPersona
		self.__correoElectronico = correoElectronico 
		self.__relacionesOtrasAgencias = relacionesOtrasAgencias 
		self.__CodAgencia = CodAgencia

	def getId(self):
		return self.__

	def setId(self,id):
		self.__id = id
		
	def getNombre(self):
		return self.__nombre

	def setNombre(self, nombre):
		self.__nombre = nombre

		
	def getAnocreacion(self):
		return self.__anoCreacion

	def setsAnocreacion(self, anocreacion):
		self.__anoCreacion = anocreacion

		
	def getsedeproncipal(self):
		return self.__sedePrincipal

	def setsedeproncipal(self, sedePrincipal):
		self.__sedePrincipal =  sedePrincipal

		
	def getidPersona(self):
		return self.__idPersona

	def setidPersona(self, idPersona):
		self.__idPersona = idPersona

		
	def getcorreoElectronico(self):
		return self.__correoElectronico

	def setcorreoElectronico(self, correoElectronico):
		self.__correoElectronico = correoElectronico

		
	def getrelacionesOtrasAgencias(self):
		return self.__relacionesOtrasAgencias

	def setrelacionesOtrasAgencias(self,relacionesOtrasAgencias):
		self.__relacionesOtrasAgencias

	def getCodAgencia(self):
		return self.__CodAgencia

	def setCodAgencia(self, CodAgencia):
		self.__CodAgencia = CodAgencia
