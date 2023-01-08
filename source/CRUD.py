from services import createRow, deleteByid, getAllData, updateByid, getOneRow

# User definition to create new row

def createRowConsole(conn):
    key = input("Please enter key id: ")
    room = input("Please enter room location: ")
    rack = input("Please enter rack location: ")
    contained = input("Is the key in the safe(True/False): ")
    query = f"INSERT INTO key_inv VALUES({key}, {room},'{rack}',{contained});"

    createRow(conn, query)

# User input key id to delete row from table. Once deleted change is commited and data will be deleted.

def deleteOneConsole(conn):
    id = input("Please enter id of the key you would like to delete: ")
    deleteByid(conn, id)
    conn.commit()
    print("""
    Deletion is a success!
    
    Displaying change in database after deletion below:
    """)
    print(getAllData(conn, 'key_inv'))

def updateOneConsole(conn):
    print("\nBelow is all the keys registered.")
    print(getAllData(conn, 'key_inv'))
    ids = input("""\nPlease state which key is taken out of the safe by selecting the ID: """) # User input key id
    print(f"""\nYou have selected the following Key ID: """ + str(getOneRow(conn, ids)))  # displays the current key selected.
    cont = input("""\nUpdate whether key is in the safe or not(True False): """) # user input contained value
    updateByid(conn, ids, cont) # updating key contained value
    conn.commit()
    print(getOneRow(conn, ids))
