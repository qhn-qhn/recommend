from conn import startdb
def delmajors(name):
    db = startdb()
    cursor = db.cursor()
    sql = "DELETE FROM majorall WHERE name = '%s'"%(name)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        return 0