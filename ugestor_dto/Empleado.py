from Persona import Persona


class Empleado(Persona):
	"""docstring for ClassName"""
	def __init__(self, fechaIngreso, Cargo, Salario, id):
		super().__init__(self, id, cedula, nombre, apellido, fechaNacimiento, sexo)
		self.__fechaIngreso = fechaIngreso
		self.__Cargo = Cargo
		self.__Salario = Salario
		self.__id = id
