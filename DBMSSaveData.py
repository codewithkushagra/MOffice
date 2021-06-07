import sqlite3





def createTables():

    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()

    cursor.execute("DROP TABLE IF EXISTS TEAMREGISTER")
    cursor.execute("DROP TABLE IF EXISTS RECEIVEDWORK")
    cursor.execute("DROP TABLE IF EXISTS GENERALUPDATE")
    cursor.execute("DROP TABLE IF EXISTS GROUPANDPARTYDETAILS")
    db.commit()
    cursor.execute("CREATE TABLE GROUPANDPARTYDETAILS(GROUPNAME TEXT,PARTYNAME TEXT,PANNUMBER TEXT,PARTYADDRESS TEXT)")
    cursor.execute("CREATE TABLE RECEIVEDWORK(WORKID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,PANNUMBER TEXT,DEPARTMENT TEXT,TYPE TEXT,TYPEC TEXT,AY TEXT,DATEOFRECEIVING TEXT,ESTIMATEDATE TEXT,PRIORITY TEXT,NATUREOFWORK TEXT,FY TEXT,WORKSTATUS TEXT,ALLOTED TEXT,COMPELETIONDATE TEXT)")
    cursor.execute("CREATE TABLE TEAMREGISTER(ID TEXT,NAME TEXT,PHONE INTEGER,AGE INTEGER,GENDER TEXT,ADDRESS TEXT,HIREDATE TEXT,PASSWORD TEXT);")
    cursor.execute("CREATE TABLE GENERALUPDATE(PRIME INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,WORKID INTEGER ,UPDATEOFWORK TEXT,Date TEXT)")

    cursor.close()
    db.close()

    return

def saveGroupParty(groupname,partyname,pannumber,address):
    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()
    
    cursor.execute("INSERT INTO GROUPANDPARTYDETAILS(GROUPNAME,PARTYNAME,PANNUMBER,PARTYADDRESS)VALUES(?,?,?,?)",(groupname,partyname,pannumber,address))
    db.commit()

    cursor.close()
    db.close()
    return 

def insertWorkRecord(departmenttype,departmenttypec,pannumber,departmentnameselected,recievedate,financialyear,assessmentyear,workstatus):
    db=sqlite3.connect('mybd.db')
    cursor=db.cursor()
    none="None"
    cursor.execute("INSERT INTO RECEIVEDWORK(PANNUMBER,DEPARTMENT,TYPE,TYPEC,AY,DATEOFRECEIVING,ESTIMATEDATE,PRIORITY,NATUREOFWORK,FY,WORKSTATUS,ALLOTED,COMPELETIONDATE)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(pannumber,departmentnameselected,departmenttype,departmenttypec,assessmentyear,recievedate,none,none,none,financialyear,workstatus,none,none))
    db.commit()

    cursor.close()
    db.close()
    return



# createTables()