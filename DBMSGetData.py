import sqlite3

def getData(TABLE,ROW):
    
    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()

    cursor.execute(f"SELECT {ROW} FROM {TABLE}")
    result=cursor.fetchall()

    cursor.close()
    db.close()

    return result