from Persona import Persona


class Empleado(Persona):
	"""docstring for ClassName"""
	def __init__(self, fechaIngreso, cargo, salario, id):
		super().__init__(self, id, cedula, nombre, apellido, fechaNacimiento, sexo)
		self.__fechaIngreso = fechaIngreso
		self.__cargo = cargo
		self.__salario = salario
		self.__id = id

		def getId(self):
			return self.__id

		def setId(self, id):
			self.__id = id

		def getfechaIngreso(self):
			return self.__fechaIngreso

		def setfechaIngreso(self, fechaIngreso):
			self.__cargo = cargo

		def getsalario(self):
			return self.__salario

		def setsalario(self, salario):
			self. __salario = salario
