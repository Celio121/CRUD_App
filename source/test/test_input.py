import sqlite3
from test_services import test_getAllData
from test_setup import createConn
from test_CRUD import createRowConsole, test_createRowConsole, test_deleteOneConsole, test_updateOneConsole
import pytest

# defining connection and cursor

conn = createConn('key_dbase.db')
cursor = conn.cursor()

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

def test_consoleInput():
    choice = 3 # Setup
    if choice == "1": # Setup 
        test_createRowConsole()
        result = test_createRowConsole() # Result
        assert result # Assert
    elif choice == "2":
        test_getAllData()
        result2 = test_getAllData() #Result
        assert result2 # Assert
    elif choice == "3": # Setup
        test_updateOneConsole()
        result3 = test_updateOneConsole() # Result
        assert result3 # Assert
    elif choice == "4": # Setup
        test_deleteOneConsole() 
        result4 = test_deleteOneConsole() # Result
        assert result4 # Assert

