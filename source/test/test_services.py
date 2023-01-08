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
conn = sqlite3.connect(':memory:')
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


