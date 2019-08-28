import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Modelo import Modelo


class ModeloDAO:
	"""docstring for ClassName"""
	def __init__(self):
		self.conn = DAO()
		self.sql = ""



	def Create(self, Modelo):
		self.sql = """insert into {0}.Modelo (idModelo,colorojosModelo,colorpielModelo,estaturaModelo ,cinturaModelo,bustoModelo,tallapiesModelo,pesoModelo,fechaHistoricoModelo) values ({6},{1}, '{2}','{3}','{4}','{5}','{7}','{8}','{9}')
		""".format(self.conn.getSCHEMA(), Modelo.getcolorOjos(), Modelo.getcolorPiel(), Modelo.getApellido(), Modelo.getestatura(), Modelo.getmedidaBusto(),
			Modelo.getId(), Modelo.getmedidaCintura(), Modelo.getPeso())
		try:
			cn = self.conn.getConnection()
			cur = cn.cursor()
			cur.execute(self.sql, )
			cur.close()
			cn.commit()
			self.msj = "Modelo Creado Exitosamente"
		except (Exception, psycopg2.DatabaseError) as error:
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
		finally:
			if cn is not None:
				cn.close()
		return self.msj

def Delete(self, Mo):
    self.sql = """delete from {0}.Modelo where idModelo={1}""".format(self.conn.getSCHEMA(), Modelo.getId())
    try:
        cn = self.conn.getConnection()
        cur = cn.cursor()
        cur.execute(self.sql, )
        cur.close()
        cn.commit()
        self.msj = "Modelo elimanado Exitosamente"
    except (Exception, psycopg2.DatabaseError) as error:
        self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
    finally:
        if cn is not None:
            cn.close()
    return self.msj

def Update(self, Modelo):
    self.sql = """update table {0}.Modelo set idModelo={1},colorojosModelo={2},colorpielModelo={3},estaturaModelo={4} ,cinturaModelo={5},bustoModelo={6},tallapiesModelo={8},pesoModelo={9},fechaHistoricoModelo={1}
    """.format(self.conn.getSCHEMA(), Modelo.getId(), Modelo.getNombre(), Modelo.getcolorOjos(), Modelo.getcolorPiel(), Modelo.getestatura(), Modelo.getmedidaBusto(), Modelo.getmedidaBusto(), Modelo.getmedidaCintura(),Modelo.getPeso())
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


	def Buscar(self, Modelo, column):
		self.sql = """select * from {0}.Modelo where {1}={2}""".format(self.conn.getSCHEMA(), column, Modelo)
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
