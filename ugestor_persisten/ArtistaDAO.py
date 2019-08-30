import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pathRootFolder = script_dir.split(script_dir.split(os.sep)[-1])[0]
sys.path.append("{0}/ugestor_dto".format(pathRootFolder))
from DAO import DAO
from Artista import Artista


class ArtistaDAO:
    """docstring for ClassName"""

    def __init__(self):
        self.conn = DAO()
        self.sql = ""

        def Create(self, Artista):
            nameSecuen = ""
            if(self.conn.validateSequence(Persona.__class__.__name__)):
                self.conn.reconnect()
                nameSecuen = self.conn.createSequence(Persona.__class__.__name__)
            else:
                nameSecuen = "seq_{0}".format(Persona.__class__.__name__)
                self.conn.reconnect()
                self.sql = """insert into {0}.Artista (idArtista , nombreArtistico, generoMusical, tipoArtista,  idperdsona) values ({1},{2}, '{3}','{4}')""".format( self.conn.getSCHEMA(), Artista.getnombreArtistico(),Artista.getnombreArtistico(),Artista.getgeneroMusical(),
                                                                                                                                                                     nameSecuen,Artista.gettipoArtista())
                try:
                    cn = self.conn.getConnection()
                    cur = cn.cursor()
                    cur.execute(self.sql, )
                    cur.close()
                    cn.commit()
                    self.msj = "Artista Creado Exitosamente"
                except (Exception, psycopg2.DatabaseError) as error:
                    self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
                finally:
                    if cn is not None:
                        cn.close()
                        return self.msj


                    def Delete(self, Artista):
                        self.conn.reconnect()
                        self.sql = """delete from {0}.Artista where idArtista={1}""".format(self.conn.getSCHEMA(), Artista.getId())
                        try:
                            cn = self.conn.getConnection()
                            cur = cn.cursor()
                            cur.execute(self.sql, )
                            cur.close()
                            cn.commit()
                            self.msj = "Artista elimanado Exitosamente"
                        except (Exception, psycopg2.DatabaseError) as error:
                            self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
                        finally:
                            if cn is not None:
                                cn.close()
                                return self.msj


                            def Update(self, Artista):
                                self.conn.reconnect()
                                self.sql = """update table {0}.Artista set idArtista={1},nombreArtistico={2}, generoMusical={3},tipoArtista ={4}
                                """.format(self.conn.getSCHEMA(), Disenador.getid(), Disenador.getpasaporte(), Disenador.getpasaporte())
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

                                    def Buscar(self, Artista, column):
                                        self.conn.reconnect()
                                        self.sql = """select * from {0}.Artista where {1}={2}""".format(
                                            self.conn.getSCHEMA(), column, Artista)
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
                                            
