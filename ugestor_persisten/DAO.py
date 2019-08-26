#!/usr/bin/python2.7
#
# Small script to show Postgreself.sql and Pyscopg together
#
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


	def connnection(self): 
		try: 
			self.conn = psycopg2.connect("host='{0}' dbname='{1}' user='{2}' password='{3}'  port={4}".format(self.host, self.dbname, 
				self.user, self.password, self.port ))
			self.msj = "Conecion ok"
			return self.conn
		except (Exception, psycopg2.DatabaseError) as error: 
			self.msj = "Lamentamos informar le que a ocurrido un error:  {0}".format(error)
			return self.conn

	