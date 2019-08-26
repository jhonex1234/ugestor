from Empleado import Empleado


class profesionales(Empleado):
      def __init__(self,id,EgresadoUniversidad,estudios):
      super().__init__(self,id, fechaIngreso, Cargo, Salario, id)
      self.__id=id
      self.__EgresadoUniversidad=EgresadoUniversidad
      self.__estudios=estudios

      def  getid(self):
      	return self.__id

      def setid(self, id):
      	self.__id = id

      def getEgresadoUniversidad(self):
    	return self.__EgresadoUniversidad

      def setEgresadoUniversidad(self, EgresadoUniversidad):
        self.__EgresadoUniversidad = EgresadoUniversidad

      def  getestudios(self):
      	return self.__estudios

      def setid(self, estudios):
      	self.__estudios = estudios
