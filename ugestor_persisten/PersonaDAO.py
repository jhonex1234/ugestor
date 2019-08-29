import os
import sys
import psycopg2

script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Persona import Persona


class PersonaDAO:
	"""docstring for ClassName"""
	def __init__(self):
		self.conn = DAO()
		self.sql = ""


	def Create(self, Persona):
		self.sql = """insert into {0}.persona (id ,cedula, nombre, apellido, fechanacimiento, sexo,tipoDocumento) values ({6},{1}, '{2}','{3}','{4}','{5}','{7}')
		""".format(self.conn.getSCHEMA(), Persona.getDocumento(), Persona.getNombre(), Persona.getApellido(), Persona.getFechaNacimiento(), Persona.getSexo(),
			Persona.getId(), Persona.gettipoDocumento())
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			cur.close()
			cn.commit()
			self.msj = "Finca  Creada Exitosamente"
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
				cn.close()
		return self.msj


	def Delete(self, Persona):
		self.sql = """delete from {0}.persona where id={1}""".format(self.conn.getSCHEMA(), Persona.getId())
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			cur.close()
			cn.commit()
			self.msj = "Finca  Creada Exitosamente"
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
				cn.close()
		return self.msj


	def Update(self, Persona):
		self.sql = """update table {0}.persona set cedula={1}, nombre='{2}', apellido='{3}', fechanacimiento='{4}', sexo='{5}', tipoDocumento='{7}' where id={6}
		""".format(self.conn.getSCHEMA(), Persona.getDocumento(), Persona.getNombre(), Persona.getApellido(), Persona.getFechaNacimiento(), Persona.getSexo(), Persona.getId(), Persona.gettipoDocumento())
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			cur.close()
			cn.commit()
			self.msj = "Finca  Creada Exitosamente"
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
				cn.close()
		return self.msj

	def Buscar(self, Persona, column):
		self.sql = """select * from {0}.persona where {1}={2}""".format(self.conn.getSCHEMA(), column, Persona)
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			result = cur.fetchall()
			cur.close()
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
			    cn.close()
		return result


	def Buscar(self, Persona, column):
		self.sql = """select * from {0}.persona where {1}={2}""".format(self.conn.getSCHEMA(), column, Persona)
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			result = cur.fetchall()
			cur.close()
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
			    cn.close()
		return result
