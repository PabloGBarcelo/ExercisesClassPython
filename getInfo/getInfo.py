import pyodbc
reference = input("Ingresa una referencia")
#storeNum = input("Ingresa una tienda")

def connectToPower520(): # conecta al server y devuelve la conexion
	return pyodbc.connect('DSN=DB520;UID=PABLO5;PWD=BARCELO5')
	#return pyodbc.connect('DSN=DB232;UID=PABLO8;PWD=BARCELO8') #AQUI

def sendQuery(query):
	con = connectToPower520()
	cursor = con.cursor()
	cursor.execute(query)
	return cursor

def associateColumnNamesWithDict(cursor):
	results = []
	columns = [column[0] for column in cursor.description]

	for row in cursor.fetchall():
		results.append(dict(zip(columns, row)))

	return results  # Crea un diccionario con los resultados

def getInfo(codbar):
    
    # query = "SELECT  FROM EGFITJOY.REFJOYBAR AS BAR WHERE CODBAR = '" + str(reference) + "'" 
    #query = "SELECT * FROM EGFITJOY.REFJOYBAR AS BAR WHERE CODBAR = '{0}'".format(str(reference))
	query = "SELECT EGFITJOY.EXISTENCIA.MAGAT,EGFITJOY.EXISTENCIA.EXSACT,EGFITJOY.REFJOYBAR.CODALT,EGFITJOY.REFJOYBAR.CODBAR FROM ((EGFITJOY.REFJOYBAR INNER JOIN EGFITJOY.REFJOYALT ON (EGFITJOY.REFJOYBAR.CODALT = EGFITJOY.REFJOYALT.CODALT)\
					 AND (EGFITJOY.REFJOYBAR.CODIRE = EGFITJOY.REFJOYALT.CODIRE)) INNER JOIN EGFITJOY.RELREFART ON EGFITJOY.REFJOYBAR.CODIRE = EGFITJOY.RELREFART.CODIRE) INNER JOIN EGFITJOY.EXISTENCIA ON (EGFITJOY.REFJOYBAR.CODIRE = EGFITJOY.EXISTENCIA.CODIRE)\
					 AND (EGFITJOY.REFJOYBAR.CODBAR = EGFITJOY.EXISTENCIA.LOT)\
					 WHERE EGFITJOY.REFJOYBAR.CODBAR = '" + str(codbar) + "'\
					 AND EGFITJOY.EXISTENCIA.EXSACT>=1"
	info = associateColumnNamesWithDict(sendQuery(query))
	for item in info:
		print(item)    		
	return
getInfo(reference)


