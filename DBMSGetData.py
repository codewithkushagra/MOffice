import sqlite3

def getData(TABLE,ROW):
    
    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()

    cursor.execute(f"SELECT DISTINCT {ROW} FROM {TABLE}")
    result=cursor.fetchall()

    cursor.close()
    db.close()

    return result

def getWhereData(TABLE,ROW1,ROW2,ATTRIBUTENAME):
    
    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()
    cursor.execute(f"SELECT {ROW1} FROM {TABLE} WHERE {ROW2} = '{ATTRIBUTENAME}' ")
    result=cursor.fetchall()

    cursor.close()
    db.close()

    return result


def getOneVTwoP(TABLE,ROW1,ROW2,ROW3,ROW4,ATTRIBUTENAME1,ATTRIBUTENAME2):
    
    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()
    cursor.execute(f"SELECT {ROW1} , {ROW2} FROM {TABLE} WHERE {ROW3} = '{ATTRIBUTENAME1}' AND {ROW4}= '{ATTRIBUTENAME2}'  ")
    result=cursor.fetchone()
    
    cursor.close()
    db.close()

    return result
    

def getAllData(TABLE):

    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()
    
    cursor.execute(f"SELECT * FROM {TABLE} ")
    result=cursor.fetchall()
    
   
    
    cursor.close()
    db.close()
    return result


def getAllDataOfColumn(TABLE,COLUMN,PASSED):

    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()

    cursor.execute(f" SELECT * FROM {TABLE} WHERE {COLUMN}= '{PASSED}' ")
    result=cursor.fetchall()
    
    
    cursor.close()
    db.close()
    return result



def getAllDataByTwoColumn(TABLE,COLUMN1,COLUMN2,PASSED1,PASSED2):

    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()

    cursor.execute(f" SELECT * FROM {TABLE} WHERE {COLUMN1} = '{PASSED1}' AND {COLUMN2} = '{PASSED2}'")
    result=cursor.fetchall()
    
    
    cursor.close()
    db.close()
    return result




def getParty(PAN,TABLE):

    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()
    cursor.execute(f"SELECT PARTYNAME , GROUPNAME FROM {TABLE} WHERE PANNUMBER = '{PAN}'")
    result=cursor.fetchone()
  
    cursor.close()
    db.close()

    return result


def getOneForOne(TABLE,ROW1,COLUMN,PASSED):
    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()
    cursor.execute(f"SELECT {ROW1} FROM {TABLE} WHERE {COLUMN} = '{PASSED}'")
    result=cursor.fetchone()
    
    cursor.close()
    db.close()

    return result