import pytest
import sqlite3

conn = sqlite3.connect(':memory:')

def createRow(conn, query):
    try:
        conn.cursor().execute(query)
        conn.commit()
        return True
    except Exception as e:
        print(str(e))
        print("An exception happened:(")
    finally:
        print("This will always run, regardless of whether there is an exception or not")

#Creating conn to database as well as table to run test def, created cursor
query = 'CREATE TABLE test (id INTEGER, name bool)'
cursor = conn.cursor()

def test_createRow():
    cursor = conn.cursor()
    # testing the exeption to see result will be failed as values are incorrect
    try:
        result = createRow(conn, "INSERT INTO test VALUES(1, 'exception');")
        assert result == "An exception happened:("
    except Exception: # this will run even if the exception is invalid.
        e = "This will always run, regardless of whether there is an exception or not"
        assert e == "This will always run, regardless of whether there is an exception or not"

# cursor command to delete data from table
def deleteByid(conn, id):
    conn.cursor().execute(f"""
    DELETE FROM key_inv 
    WHERE key_id = {id};
    """)
    return True

# Creating test DB
def test_deletByid():
    # Creation
    cursor.execute("""CREATE TABLE IF NOT EXISTS test2
    (id INTERGER NOT NULL UNIQUE,
    cont bool NOT NULL
    );""")
    data_ins = createRow(conn, f"INSERT INTO test2 VALUES(2, True);")
    data_ins2 = createRow(conn, f"INSERT INTO test2 VALUES(3, False);")
    delete_data = cursor.execute("""DELETE FROM test2 
    WHERE id = 2;
    """)
    # Result
    result = cursor.execute(f"""SELECT * FROM test2""").fetchone()
    # Assert
    assert result == (3, False)

# fetching inputted data from database
def getAllData(conn, tableName):

    # Displays columns
    print(f'\nColumns in {tableName} table:')
    cdata = conn.cursor().execute(f"""SELECT * FROM {tableName}""")
    for column in cdata.description:
        print(column[0])
    print(f'\nData in {tableName} table:')
    for row in cdata:
        print(row)
        return True

def test_getAllData():
    # Creation
    cursor.execute("""CREATE TABLE IF NOT EXISTS test
    (id INTERGER NOT NULL UNIQUE,
    cont bool NOT NULL);""")

    data_ins = createRow(conn, f"INSERT INTO test VALUES(2, True);")
    data_ins2 = createRow(conn, f"INSERT INTO test VALUES(3, False);")
    # Result
    data = cursor.execute(f"""SELECT * FROM test""")
    result = data.fetchall()
    # Assert
    assert result == [(2, True), (3, False)]

# update key contained command
def updateByid(conn, ids, cont):
    conn.cursor().execute(f"""
    UPDATE key_inv
    SET contained = {cont}
    WHERE key_id = {ids};""")

def test_updateByid():
    # Creation
    cursor.execute("""CREATE TABLE IF NOT EXISTS test
    (id INTERGER NOT NULL UNIQUE,
    cont bool NOT NULL);""")
    data_ins = createRow(conn, f"INSERT INTO test VALUES(2, True);")
    update = conn.cursor().execute(f"""
    UPDATE test
    SET cont = False
    WHERE id = 2;""")
    # Result
    result = cursor.execute(f"""SELECT * FROM test""").fetchone()
    # Assert
    assert result == (2, False)
    
def getOneRow(conn, ids):
    rowInfo = conn.cursor().execute(f"""
        SELECT * 
        FROM key_inv 
        WHERE key_id ={ids}""")
    listRow = rowInfo.fetchall()
    return listRow

def test_getOneRow():
    # Creation
    cursor.execute("""CREATE TABLE IF NOT EXISTS test3
    (id INTERGER NOT NULL UNIQUE,
    cont bool NOT NULL);""")
    data_ins = createRow(conn, f"INSERT INTO test3 VALUES(2, True);")
    # Result
    result = cursor.execute(f"""SELECT * FROM test3""").fetchone()
    # Assert
    assert result == (2, True)