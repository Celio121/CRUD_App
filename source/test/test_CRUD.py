from test_services import createRow, deleteByid, getAllData, updateByid, getOneRow
import sqlite3
import pytest

# User definition to create new row

def createRowConsole(conn):
    key = input("Please enter key id: ")
    room = input("Please enter room location: ")
    rack = input("Please enter rack location: ")
    contained = input("Is the key in the safe(True/False): ")
    query = f"INSERT INTO key_inv VALUES({key}, {room},'{rack}',{contained});"

    createRow(conn, query)

    
def test_createRowConsole():
    # Set up
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS test_table
    (key_id INTERGER NOT NULL UNIQUE, 
    room_id int(5) NOT NULL, 
    rack varchar(5) NOT NULL, 
    contained bool NOT NULL, 
    PRIMARY KEY(key_id)
    );""")

    #test code
    key = 1
    room = 2
    rack = 3
    contained = True
    query = f"INSERT INTO test_table VALUES({key}, {room},'{rack}',{contained});"

    createRow(conn, query)

    #show results
    result = cursor.execute("""SELECT * FROM test_table""").fetchone()
    assert result == (1, 2, '3', True)

def deleteOneConsole(conn):
    id = input("Please enter id of the key you would like to delete: ")
    deleteByid(conn, id)
    conn.commit()
    print("""
    Deletion is a success!
    
    Displaying change in database after deletion below:
    """)
    print(getAllData(conn, 'key_inv'))

def test_deleteOneConsole():
    # Creation
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS test2
    (id INTERGER NOT NULL UNIQUE,
    cont bool NOT NULL
    );""")
    data_ins = createRow(conn, f"INSERT INTO test2 VALUES(2, True);")
    data_ins2 = createRow(conn, f"INSERT INTO test2 VALUES(3, False);")
    input = 2
    delete_data = cursor.execute(f"""DELETE FROM test2 
    WHERE id = {input};
    """)
    # Result
    result = cursor.execute(f"""SELECT * FROM test2""").fetchone()
    # Assert
    assert result == (3, False)

def updateOneConsole(conn):
    print("\nBelow is all the keys registered.")
    print(getAllData(conn, 'key_inv'))
    ids = input("""\nPlease state which key is taken out of the safe by selecting the ID: """) # User input key id
    print(f"""\nYou have selected the following Key ID: """ + str(getOneRow(conn, ids)))  # displays the current key selected.
    cont = input("""\nUpdate whether key is in the safe or not(True False): """) # user input contained value
    updateByid(conn, ids, cont) # updating key contained value
    conn.commit()
    print(getOneRow(conn, ids))

def test_updateOneConsole():
    # Creation
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS test2
    (id INTERGER NOT NULL UNIQUE,
    cont bool NOT NULL
    );""")
    data_ins = createRow(conn, f"INSERT INTO test2 VALUES(2, True);")
    id_inp = 2
    cont_inp = False
    conn.cursor().execute(f"""
    UPDATE test2
    SET cont = {cont_inp}
    WHERE id = {id_inp};""")
    # Result
    result = cursor.execute("SELECT * FROM test2").fetchone()
    # Assert
    assert result == (2, False)
