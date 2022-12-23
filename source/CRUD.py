from services import createRow

# User definition to create new row

def createRowConsole(conn):
    key = input("Please enter key id: ")
    room = input("Please enter room location: ")
    rack = input("Please enter rack location: ")
    contained = input("Is the key in the safe(True/False): ")
    query = f"INSERT INTO key_inv VALUES({key}, {room},'{rack}',{contained});"

    createRow(conn, query)

