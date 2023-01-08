from setup import createConn
from services import getAllData
from CRUD import createRowConsole, deleteOneConsole, updateOneConsole

# defining connection and cursor

conn = createConn('key_dbase.db')
cursor = conn.cursor()

# User input output
def consoleInput():
    print(
        """
        Welcome to the Key Inventory!
        Please select an option by entering the number.
        1. Create a new entry
        2. Get all data on DB
        3. Update a row in the database
        4. Delete a row from the database
        """
        )
    choice = input("Please enter an option: ")
# Choice selection from user input
    if choice == "1":
        createRowConsole(conn)
    elif choice == "2":
        print(getAllData(conn, 'key_inv'))
    elif choice == "3":
        updateOneConsole(conn)
    elif choice == "4":
        deleteOneConsole(conn)

consoleInput()