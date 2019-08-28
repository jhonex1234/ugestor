from Persona import Persona


class Modelo:
	def __init__(self, id, colorOjos, colorPiel, estatura, medidaCintura,medidaBusto, tallaZapatos, peso, particularidades):
		super().__init__(self, id, cedula, cedula, apellido, fechaNacimiento, sexo)
		self.__id = id
		self.__colorOjos = colorOjos
		self.__colorPiel = colorPiel
		self.__estatura = estatura
		self.__medidaCintura = medidaCintura
		self.__medidaBusto = medidaBusto
		self.__medidaCintura = medidaCintura
		self.__tallaZapatos = tallaZapatos
		self.__particularidades = particularidades
		self.__peso = peso
	def getId(self):
		return self.__id

	def setIdid(self, id):
		self.__id = id

	def getcolorOjos(self):
		return self.__colorOjos

	def setcolorOjos(self, colorOjos):
		self.__colorOjos = colorOjos

	def getcolorPiel(self):
		return self.colorPiel

	def setcolorPiel(self, colorPiel):
		self.__colorPiel = colorPiel

	def getestatura(self):
		return self.__estaturmedidaBustoa

	def setestatura(self, estatura):
		self.__estatura = estatura

	def getmedidaBusto(self):
		return self.__medidaBusto

	def setmedidaBusto(self, medidaBusto):
		self.__medidaBusto = medidaBusto

	def getmedidaCintura(self):
		return self.__medidaCintura

	def setmedidaCintura(self, medidaCintura):
		self.__medidaCintura = medidaCintura

	def getPeso(self):
		return self.__medidaCintura

	def setPeso(self, peso):
		self.__peso = peso
