
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Empleado import Empleado


class EmpleadoDAO:
    """docstring for ClassName"""

    def __init__(self):
        self.conn = DAO()
        self.sql = ""

    def Create(self, Empleado):
        self.sql = """insert into {0}.Empleado (idEmpleado,fechaIngresoEmpleado, cargoEmpleado, salarioEmpleado) values ({1},{2}, '{3}','{4}')""".format(
            self.conn.getSCHEMA(),Empleado.getId(),Empleado.getnombrefechaIngreso(),Empleado.getcargo(),Empleado.getsalario())
            self.conn.reconnect()
        try:
            cn = self.conn.getConnection()
            cur = cn.cursor()
            cur.execute(self.sql, )
            cur.close()
            cn.commit()
            self.msj = "Empleado Creado Exitosamente"
        except (Exception, psycopg2.DatabaseError) as error:
            self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
        finally:
            if cn is not None:
                cn.close()
        return self.msj


def Delete(self, Mo):
    self.conn.reconnect()
    self.sql = """delete from {0}.Empleado where idEmpleado={1}""".format(
        self.conn.getSCHEMA(), Empleado.getId())
    try:
        cn = self.conn.getConnection()
        cur = cn.cursor()
        cur.execute(self.sql, )
        cur.close()
        cn.commit()
        self.msj = "Empleado elimanado Exitosamente"
    except (Exception, psycopg2.DatabaseError) as error:
        self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
    finally:
        if cn is not None:
            cn.close()
    return self.msj


def Update(self, Empleado):
    nameSecuen = ""
    if(self.conn.validateSequence(Persona.__class__.__name__)):
        self.conn.reconnect()
        nameSecuen = self.conn.createSequence(Persona.__class__.__name__)
    else:
		nameSecuen = "seq_{0}".format(Persona.__class__.__name__)
    self.conn.reconnect()
    self.sql = """update table {0}.Empleado set idEmpleado={1},fechaIngresoEmpleado={2}, cargoEmpleado={3}, salarioEmpleado={4}
    """.format(self.conn.getSCHEMA(), Empleado.getId(),Empleado.getnombrefechaIngreso(),Empleado.getcargo(),Empleado.getsalario())
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

    def Buscar(self, Empleado, column):
        self.conn.reconnect()
        self.sql = """select * from {0}.Empleado where {1}={2}""".format(
            self.conn.getSCHEMA(), column, Empleado)
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
