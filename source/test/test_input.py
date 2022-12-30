import sqlite3
from test_services import createRow
from test_setup import createConn
from test_CRUD import createRowConsole, test_createRowConsole
import pytest

# defining connection and cursor

conn = createConn('key_dbase.db')
cursor = conn.cursor()

def test_consoleInput():
    choice = 1
    if choice == "1":
        test_createRowConsole()
        result = test_createRowConsole
        assert result
