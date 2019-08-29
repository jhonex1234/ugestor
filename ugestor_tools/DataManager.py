import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
sys.path.append("{0}/ugestor_persisten".format(pathRootFolder))
from PersonaDAO import PersonaDAO
from Persona import Persona

personadao = PersonaDAO()

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