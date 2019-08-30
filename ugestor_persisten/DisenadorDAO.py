
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Disenador import Disenador


class DisenadorDAO:
    """docstring for ClassName"""

    def __init__(self):
        self.conn = DAO()
        self.sql = ""

    def Create(self, Disenador):
        self.conn.reconnect()
        self.sql = """insert into {0}.Disenador ( idDisenador,paisOrigen, pasaporte) values ({1}, '{2}','{3}')""".format(
            self.conn.getSCHEMA(), Disenador.getId(), Disenador.getpasaporte(), Disenador.getpaisOrigen())
        try:
            cn = self.conn.getConnection()
            cur = cn.cursor()
            cur.execute(self.sql, )
            cur.close()
            cn.commit()
            self.msj = "Disenador Creado Exitosamente"
        except (Exception, psycopg2.DatabaseError) as error:
            self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
        finally:
            if cn is not None:
                cn.close()
        return self.msj


def Delete(self, Mo):
    self.conn.reconnect()
    self.sql = """delete from {0}.Disenador where idDisenador={1}""".format(
        self.conn.getSCHEMA(), Disenador.getId())
    try:
        cn = self.conn.getConnection()
        cur = cn.cursor()
        cur.execute(self.sql, )
        cur.close()
        cn.commit()
        self.msj = "Disenador elimanado Exitosamente"
    except (Exception, psycopg2.DatabaseError) as error:
        self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
    finally:
        if cn is not None:
            cn.close()
    return self.msj


def Update(self, Disenador):


    self.conn.reconnect()
    self.sql = """update table {0}.Disenador set idDisenador{1},pasaporteDisenador={1},paisOrigenDisenad={3}
    """.format(self.conn.getSCHEMA(),Disenador.getId(), Disenador.getpasaporte(), Disenador.getpaisOrigen())
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

    def Buscar(self, Disenador, column):
        self.conn.reconnect()
        self.sql = """select * from {0}.Disenador where {1}={2}""".format(
            self.conn.getSCHEMA(), column, Disenador)
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
