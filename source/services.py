# code to create a data entry to database
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

# fetching inputted data from database
def getAllData(conn, tableName):

    # Displays columns
    print(f'\nColumns in {tableName} table:')
    cdata = conn.cursor().execute(f"""SELECT * FROM {tableName}""")
    for column in cdata.description:
        print(column[0])
    print(f'\nData in {tableName} table:')
    for row in cdata:
        print(row)
        return True
   

# cursor command to delete data from table
def deleteByid(conn, id):
    conn.cursor().execute(f"""
    DELETE FROM key_inv 
    WHERE key_id = {id};
    """)
    return True

# update key contained command
def updateByid(conn, ids, cont):
    conn.cursor().execute(f"""
    UPDATE key_inv
    SET contained = {cont}
    WHERE key_id = {ids};""")

# returns one line of information from database
def getOneRow(conn, ids):
    rowInfo = conn.cursor().execute(f"""
        SELECT * 
        FROM key_inv 
        WHERE key_id ={ids}""")
    listRow = rowInfo.fetchall()
    return listRow