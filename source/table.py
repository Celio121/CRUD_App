from setup import createConn, createTable

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

create_data = conn.cursor().execute(f"""INSERT INTO key_inv
VALUES(1, 5, '5', True);""")
conn.commit()

# Display the recently inputted data
data = conn.cursor().execute(f"""SELECT * 
FROM key_inv""")
listData = data.fetchall() # Converts object to usable data
print(listData)