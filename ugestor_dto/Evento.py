class Evento:
	def __init__(self, id, nombre, fechaInicio, fechaFin, idDiseñador):
		self.__id = id
		self.__nombre = nombre
		self.__fechaInicio = fechaInicio
		self.__fechaFin = fechaFin
		self._idDiseñador = idDiseñador


	def getId(self):
		return self.__id

	def setId(self, id):
		self.__id = id

	def getNombre(self):
		return self.__nombre

	def setNombre(self, nombre):
		self.__nombre = nombre

	def getFechaInicio(self):
		return self.__fechaInicio

	def setFechaInicio(self, fechaInicio):
		self.__fechaInicio = fechaInicio

	def getFechaFin(self):
		return self.__fechaFin

	def setFechaFin(self, fechaFin):
		self.__fechaFin = fechaFin	

	def setIdDiseñador(self, idDiseñador):
		self._idDiseñador = idDiseñador

	def getIdDiseñador(self):
		return self._idDiseñador