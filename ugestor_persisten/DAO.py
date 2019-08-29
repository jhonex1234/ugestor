import psycopg2

class DAO:
	"""docstring for ClassName"""
	def __init__(self): 
		
		self.msj = ""

		self.dbname = "ugestor"
		self.user = "postgres"
		self.password = "1234"
		self.host = 'localhost'
		
		self.conn = ""
		
		self.SCHEMA = ""
		self.port = 5432



		self.setSCHEMA("ugestorapp")
		self.connnection()
	
	def setSCHEMA(self, name):
		self.SCHEMA = name

	def getSCHEMA(self):
		return self.SCHEMA

	def getmsj(self):
		return self.msj
	
	def getConnection(self):
		return self.conn

	def reconnect(self):
		self.connnection()



	def connnection(self): 
		try: 
			self.conn = psycopg2.connect("host='{0}' dbname='{1}' user='{2}' password='{3}'  port={4}".format(self.host, self.dbname, 
				self.user, self.password, self.port ))
			self.msj = "Conecion ok"
			return self.conn
		except (Exception, psycopg2.DatabaseError) as error: 
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
			return self.conn

	def createSequence(self,name):
		self.sql = """create sequence {0}.seq_{1} INCREMENT 1
				  MINVALUE 1
				  MAXVALUE 9223372036854775807
				  START 1
				  CACHE 1; """.format(self.SCHEMA, name)
		try:
			cn = self.conn
			cur = cn.cursor()
			cur.execute(self.sql, )
			cur.close()
			cn.commit()
			return """{0}.{1};""".format(self.SCHEMA, name)
		except (Exception, psycopg2.DatabaseError) as error:
			print("Lamentamos informar:  {0}".format(error))
			return None
		finally:
			if cn is not None:
				cn.close()

	def validateSequence(self,name):
		self.sql = """SELECT *FROM information_schema.sequences where sequence_name = '{0}.seq_{1}'""".format(self.SCHEMA,name)
		retsul = []
		boll = True
		try:
			cn = self.conn
			cur = cn.cursor()
			cur.execute(self.sql, )
			result = cur.fetchall()
			cur.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print("Lamentamos informar le que a ocurrido un error:  {0}".format(error))
			return None
		finally:
			if cn is not None:
				cn.close()
		
		if(result != ()):
			boll = False
		return boll	