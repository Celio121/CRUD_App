import sqlite3
import pytest

conn = sqlite3.connect('test_table.db')

# Testing table creation definition
def test_create_table():
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS key_inv
(key_id INTERGER NOT NULL UNIQUE, 
room_id int(5) NOT NULL, 
rack varchar(5) NOT NULL, 
contained bool NOT NULL, 
PRIMARY KEY(key_id)
);""")
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert ('key_inv',) in tables
    
    cursor.execute("DROP TABLE key_inv;")

#create database again since it was droppped
# Testing data creation definition
def test_create_data():
    # Setup
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS key_inv
(key_id INTERGER NOT NULL UNIQUE, 
room_id int(5) NOT NULL, 
rack varchar(5) NOT NULL, 
contained bool NOT NULL, 
PRIMARY KEY(key_id)
);""")
    # Insert Values
    create_data = cursor.execute(f"""INSERT INTO key_inv VALUES(1,5,'5',True);""")
    conn.commit()
    # Show results
    result = cursor.execute("""SELECT * FROM key_inv""").fetchone()
    # Assert
    assert result == (1, 5, '5', True)

# Testing retrieving data from database definition
def test_get_data():
    # Setup
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO key_inv VALUES(2,3,'3',False);""") # Create more data
    conn.commit
    # Show results
    data = cursor.execute(f"""SELECT * FROM key_inv""")
    listData = data.fetchall()

    # Assert
    assert listData == [(1, 5, '5', True), (2, 3 ,'3', False)]

    cursor.execute("DROP TABLE key_inv;")