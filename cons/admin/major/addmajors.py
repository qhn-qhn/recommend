from conn import startdb
def addmajors(data):
    db = startdb();
    cursor = db.cursor()
    sql = "INSERT INTO majorall value (null,'%s','%s','%s','%s','%s',null)"%(data['type'],data['first'],data['second'],data['name'],data['code'])
    try:
        cursor.execute(sql);
        db.commit();
        db.close();
        return 1
    except:
        db.close()
        return 0