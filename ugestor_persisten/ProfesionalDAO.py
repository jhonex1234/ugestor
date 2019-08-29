
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Profesional import Profesional


class ProfesionalDAO:
    """docstring for ClassName"""

    def __init__(self):
        self.conn = DAO()
        self.sql = ""

    def Create(self, Profesional):
        self.sql = """insert into {0}.Profesional (idProfesional, EgresadoUniversidadProfesional, estudiosProfesional) values ({1}, '{2}','{3}')""".format(
            self.conn.getSCHEMA(), Profesional.getId(), Profesional.getEgresadoUniversidad(), Profesional.getestudios())
        try:
            cn = self.conn.getConnection()
            cur = cn.cursor()
            cur.execute(self.sql, )
            cur.close()
            cn.commit()
            self.msj = "Profesional Creado Exitosamente"
        except (Exception, psycopg2.DatabaseError) as error:
            self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
        finally:
            if cn is not None:
                cn.close()
        return self.msj


def Delete(self, Mo):
    self.sql = """delete from {0}.Profesional where idProfesional={1}""".format(
        self.conn.getSCHEMA(), Profesional.getId())
    try:
        cn = self.conn.getConnection()
        cur = cn.cursor()
        cur.execute(self.sql, )
        cur.close()
        cn.commit()
        self.msj = "Profesional elimanado Exitosamente"
    except (Exception, psycopg2.DatabaseError) as error:
        self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
    finally:
        if cn is not None:
            cn.close()
    return self.msj


def Update(self, Profesional):
    self.sql = """update table {0}.Profesional set idProfesional{1},pasaporteProfesional={1},paisOrigenDisenad={3}
    """.format(self.conn.getSCHEMA(),Profesional.getId(), Profesional.getEgresadoUniversidad(), Profesional.getestudios())
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

    def Buscar(self, Profesional, column):
        self.sql = """select * from {0}.Profesional where {1}={2}""".format(
            self.conn.getSCHEMA(), column, Profesional)
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
