import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Agencia import Agencia


class AgenciaDAO:
	"""docstring for ClassName"""
	def __init__(self):
		self.conn = DAO()
		self.sql = ""


	def Create(self, Agencia):
		self.sqlPerson = """insert into {0}.Agencia (idAgencia, nombreAgencia, anocreacionAgencia, sedeproncipalAgencia, idPersonaAgencia, correoElectronicoAgencia, relacionesOtrasAgencia, CodAgenciaAgencia) values ({1}, '{2}','{3}','{4}', {5}, '{6}', '{7}', '{8}')
		""".format(self.conn.getSCHEMA(), Agencia.getId(), Agencia.getNombre(), Agencia.getAnocreacion(), Agencia.getsedeproncipal(), Agencia.getidPersona(), Agencia.getcorreoElectronico(), Agencia.getrelacionesOtrasAgencias(), Agencia.getCodAgencia())
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


	def Delete(self, Agencia):
		self.sql = """delete from {0}.agencia where id={1}""".format(self.conn.getSCHEMA(), Agencia.getId())
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


	def Update(self, Agencia):
		self.sql = """update {0}.agencia set id={1}, nombre='{2}', anocreacion='{3}', sedeproncipal='{4}', idPersona={5}, correoElectronico='{6}', relacionesOtrasAgencias='{7}', CodAgencia='{8}' where id={1}
		""".format(self.conn.getSCHEMA(),  Agencia.getId(), Agencia.getNombre(), Agencia.getAnocreacion(), Agencia.getsedeproncipal(), Agencia.getidPersona(), Agencia.getcorreoElectronico(), Agencia.getrelacionesOtrasAgencias(), Agencia.getCodAgencia())
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

	def Buscar(self, Agencia, column):
		self.sql = """select * from{0}.agencia where {1}={2}""".format(self.conn.getSCHEMA(), column, Agencia)
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
