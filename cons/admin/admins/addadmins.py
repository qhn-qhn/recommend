from conn import startdb
def addadmins(data):
    db = startdb()
    cursor = db.cursor()
    sql = "INSERT INTO user values('%s','%s','%s','%s','%s',null,null,'1')" % (data['id'], data['username'], data['password'], data['phone'], data['email'])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        db.close()
        return 0