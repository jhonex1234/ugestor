import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
sys.path.append("{0}/ugestor_persisten".format(pathRootFolder))
from PersonaDAO import PersonaDAO
from Persona import Persona
from ArtistaDAO import ArtistaDAO
from Artista import Artista
from DisenadorDAO import DisenadorDAO
from Disenador import Disenador
from EmpleadoDAO import EmpleadoDAO
from Empleado import Empleado
from EmpleadorazoDAO import EmpleadorazoDAO
from Empleadorazo import Empleadorazo
from ModeloDAO import ModeloDAO
from Modelo import Modelo
from ProfesionalDAO import ProfesionalDAO
from Profesional import Profesional

personadao = PersonaDAO()
Disenadordao = DisenadorDAO()
Artistadao = ArtistaDAO()
Empleado = EmpleadoDAO()
Empleadorazo = EmpleadorazoDAO()
Modelo = ModeloDAO()
Profesional = ProfesionalDAO()

class DataManager:

	def createPerson(self, Persona):
		return personadao.Create(Persona)

	def deletePerson(self,Persona):
		return personadao.Delete(Persona)

	def updatePerson(self, Persona):
		return personadao.Update(Persona)

	def buscarPerson(self, Persona, column):
		return personadao.Buscar(Persona, column)

	def obtenerPersonas(self):
		return personadao.VerTodos()

	def v(self,Persona):
		personadao.validate(Persona)

	def createAgencia(self, Agencia):
		return AgenciaDAO.Create(Agencia)

	def deleteAgencia(self,Agencia):
		return AgenciaDAO.Delete(Agencia)

	def updateAgencia(self, Agencia):
		return AgenciaDAO.Update(Agencia)

	def buscarAgencia(self, Agencia, column):
		return AgenciaDAO.Buscar(Agencia, column)

	def createArtistas(self, Artistas):
		return ArtistaDAO.Create(Artista)

	def deleteArtistas(self,Artistas):
		return ArtistaDAO.Delete(Artista)

	def updateArtistas(self, Artistas):
		return ArtistaDAO.Update(Artista)

	def buscarArtistas(self, Artistas, column):
		return ArtistaDAO.Buscar(Artistas, column)

	def obtenerArtistas(self):
		return ArtistaDAO.VerTodos()

		"""Disenador"""
	def createDisenador(self, Disenador):
		return DisenadorDAO.Create(Disenador)

	def deleteDisenador(self,Disenador):
		return DisenadorDAO.Delete(Disenador)

	def updateDisenador(self, Disenador):
		return DisenadorDAO.Update(Disenador)

	def buscarDisenador(self, Disenador, column):
		return DisenadorDAO.Buscar(Disenador, column)

	def obtenerDisenador(self):
		return DisenadorDAO.VerTodos()
	"""Empleado"""

	def createEmpleado(self, Empleado):
		return EmpleadoDAO.Create(Empleado)

	def deleteEmpleado(self,Empleado):
		return EmpleadoDAO.Delete(Empleado)

	def updateEmpleado(self, Empleado):
		return EmpleadoDAO.Update(Empleado)

	def buscarEmpleado(self, Empleado, column):
		return EmpleadoDAO.Buscar(Empleado, column)

	def obtenerEmpleado(self):
		return EmpleadoDAO.VerTodos()
	"""Empleadorazo"""

	def createEmpleadorazo(self, Empleadorazo):
		return EmpleadorazoDAO.Create(Empleadorazo)

	def deleteEmpleadorazo(self,Empleadorazo):
		return EmpleadorazoDAO.Delete(Empleadorazo)

	def updateEmpleadorazo(self, Empleadorazo):
		return EmpleadorazoDAO.Update(Empleadorazo)
	"""Modelo"""

	def createModelo(self, Modelo):
		return ModeloDAO.Create(Modelo)

	def deleteModelo(self,Modelo):
		return ModeloDAO.Delete(Modelo)

	def updateModelo(self, Modelo):
		return ModeloDAO.Update(Modelo)

	def buscarModelo(self, Modelo, column):
		return ModeloDAO.Buscar(Modelo, column)

	def obtenerModelo(self):
		return ModeloDAO.VerTodos()
	"""Profesional"""
	def createProfesional(self, Profesional):
		return ProfesionalDAO.Create(Profesional)

	def deleteProfesional(self,Profesional):
		return ProfesionalDAO.Delete(Profesional)

	def updateProfesional(self, Profesional):
		return ProfesionalDAO.Update(Profesional)

	def buscarProfesional(self, Profesional, column):
		return ProfesionalDAO.Buscar(Profesional, column)

	def obtenerProfesional(self):
		return ProfesionalDAO.VerTodos()
