from codecs import register
import re
import mysql.connector

data = []

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_demo")
        return connection

    def insert_db(self, nombre_farmacia,ubicacion,telefono_farmcia,correo):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_registros_farmacia(NOMBRE_FARMACIA,UBICACION,TELEFONO_FARMCIA,CORREO) VALUES (%s,%s,%s,%s)"
        data = (nombre_farmacia,ubicacion,telefono_farmcia,correo)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

    def read_db(self):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT * FROM TBL_REGISTROS_FARMACIA WHERE ID_USUARIO = 1"
        cursor.execute(query)  
        registro = 0
        for fila in cursor:
            data.append(fila)
            print('RESULTADO - BackEnd: ' + str(registro) +" - "+ str(data[registro]))
            registro = registro + 1

        my_connection.close() 
