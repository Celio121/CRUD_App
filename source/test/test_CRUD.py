from test_services import createRow
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
