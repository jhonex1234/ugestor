
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Empleadorazo import Empleadorazo


class EmpleadorazoDAO:
    """docstring for ClassName"""

    def __init__(self):
        self.conn = DAO()
        self.sql = ""

    def Create(self, Empleadorazo):
        self.sql = """insert into {0}.Empleadorazo (idEmpleadorazo) values ({1})""".format(
            self.conn.getSCHEMA(), Empleadorazo.getId())
        try:
            cn = self.conn.getConnection()
            cur = cn.cursor()
            cur.execute(self.sql, )
            cur.close()
            cn.commit()
            self.msj = "Empleadorazo Creado Exitosamente"
        except (Exception, psycopg2.DatabaseError) as error:
            self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
        finally:
            if cn is not None:
                cn.close()
        return self.msj


def Delete(self, Mo):
    self.sql = """delete from {0}.Empleadorazo where idEmpleadorazo={1}""".format(
        self.conn.getSCHEMA(), Empleadorazo.getId())
    try:
        cn = self.conn.getConnection()
        cur = cn.cursor()
        cur.execute(self.sql, )
        cur.close()
        cn.commit()
        self.msj = "Empleadorazo elimanado Exitosamente"
    except (Exception, psycopg2.DatabaseError) as error:
        self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
    finally:
        if cn is not None:
            cn.close()
    return self.msj




    def Buscar(self, Empleadorazo, column):
        self.sql = """select * from {0}.Empleadorazo where {1}={2}""".format(
            self.conn.getSCHEMA(), column, Empleadorazo)
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
