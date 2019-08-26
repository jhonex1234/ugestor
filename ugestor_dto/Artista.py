from Empleado import Empleado


class Artista(Empleado):
      def __init__(self,nombreArtistico,generoMusical,tipoArtista):
         super().__init__(self,id, fechaIngreso, Cargo, Salario, id)
         self.__id = id
         self.nombreArtistico=nombreArtistico
         self.__generoMusical=generoMusical
         self.__tipoArtista=tipoArtista

         def  getnombreArtistico(self):
        	return self.__id

         def setnombreArtistico(self, id):
        	self.__id = id

         def  getnombreArtistico(self):
     		return self.__nombreArtistico

     	 def setnombreArtistico(self, nombreArtistico):
     		self.__nombreArtistico = nombreArtistico

         def  getgeneroMusical(self):
        	return self.__generoMusical

         def setgeneroMusical(self, generoMusical):
        	self.__generoMusical = generoMusical

         def  gettipoArtista(self):
           	return self._tipoArtista

         def settipoArtista(self, tipoArtista):
           	self.__tipoArtista = tipoArtista
