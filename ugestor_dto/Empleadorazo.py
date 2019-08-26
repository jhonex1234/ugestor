from Empleado import Empleado


class Empleadorazo(Empleado):
  def __init__(self, id):
  super().__init__(self, id, fechaIngreso, Cargo, Salario, id)
  self.__id = id

  def getid(self):
      return self.__id

  def setid(self, id):
      self.__id = id
