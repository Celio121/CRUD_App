from setup import createConn, createTable
from services import getAllData

# defining connection and cursor
conn = createConn('key_dbase.db')
cursor = conn.cursor()

# create key table
create_keytable = """CREATE TABLE IF NOT EXISTS key_inv
(key_id INTERGER NOT NULL UNIQUE, 
room_id int(5) NOT NULL, 
rack varchar(5) NOT NULL, 
contained bool NOT NULL, 
PRIMARY KEY(key_id)
);"""
createTable(conn, create_keytable)

# Display the recently inputted data
print(getAllData(conn, "key_inv"))