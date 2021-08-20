from conn import startdb
def addhistory(userid,major):
    db = startdb()
    cursor = db.cursor()
    sql = "INSERT INTO history value (null,'%s','%s','%s')"%(userid,major,1)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        db.close()