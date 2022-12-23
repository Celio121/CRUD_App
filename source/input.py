from setup import createConn
from CRUD import createRowConsole

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
        """ 
        )
    choice = input("Please enter an option: ")
# Choice selection from user input
    if choice == "1":
        createRowConsole(conn)

consoleInput()