# Connecting to the mySql data base
import mysql.connector

__cnx = None

def getSqlConnection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='8090',
                                host='127.0.0.1',
                                database='gs')
    return __cnx