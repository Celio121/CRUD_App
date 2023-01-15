import sqlite3
import pytest

def createConn(dbName):
    return sqlite3.connect(dbName)

def test_create_conn():
    # Setup
    db_name = 'test.db'

    # Execute the code being tested
    conn = createConn(db_name)

    # Assert
    assert isinstance(conn, sqlite3.Connection)
    assert conn.total_changes == 0

def createTable(cursor, query):
    cursor.execute(query)
    return True

def test_create_table():
    # Setup
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    query = 'CREATE TABLE test (id INTEGER, name TEXT)'

    # Execute the code being tested
    result = createTable(cursor, query)
    conn.commit()

    # Assert
    assert result == True
    assert 'test' in cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''').fetchone()
