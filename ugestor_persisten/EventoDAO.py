import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Evento import Evento


class EventoDAO:
	"""docstring for ClassName"""
	def __init__(self):
		self.conn = DAO()
		self.sql = ""


	def Create(self, Evento):
		nameSecuen = ""
	    if(self.conn.validateSequence(Persona.__class__.__name__)):
	        self.conn.reconnect()
	        nameSecuen = self.conn.createSequence(Persona.__class__.__name__)
	    else:
			nameSecuen = "seq_{0}".format(Persona.__class__.__name__)
		self.conn.reconnect()
		self.sql = """insert into {0}.evento (id, nombre, fechainicio, fechafin, iddisenador) values ({1}, '{2}','{3}','{4}', {5})
		""".format(self.conn.getSCHEMA(), Evento.getId(), Evento.getNombre(), Evento.getFechaInicio(), Evento.getFechaFin(), Evento.getIdDiseñador())
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			cur.close()
			cn.commit()
			self.msj = "Finca Creada Exitosamente"
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
				cn.close()
		return self.msj


	def Delete(self, Evento):
		self.sql = """delete from {0}.evento where id={1}""".format(self.conn.getSCHEMA(), Evento.getId())
		self.conn.reconnect()
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			cur.close()
			cn.commit()
			self.msj = "Finca Creada Exitosamente"
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
				cn.close()
		return self.msj


	def Update(self, Evento):
		self.conn.reconnect()
		self.sql = """update {0}.evento set id={1}, nombre='{2}', fechainicio='{3}', fechafin='{4}', iddisenador={5} where id={1}
		""".format(self.conn.getSCHEMA(), Evento.getId(), Evento.getNombre(), Evento.getFechaInicio(), Evento.getFechaFin(), Evento.getIdDiseñador())
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

	def Buscar(self, Evento, column):
		self.conn.reconnect()
		self.sql = """select * from{0}.evento where {1}={2}""".format(self.conn.getSCHEMA(), column, Evento)
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
