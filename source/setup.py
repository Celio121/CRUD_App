import sqlite3

def createConn(dbName):
    # Returning a connection object creating a database of this name
    return sqlite3.connect(dbName)

# Cursor to execute the command and the create table string

def createTable(cursor, query):
    cursor.execute(query) # Creating table
    return True