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