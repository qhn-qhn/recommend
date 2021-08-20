from conn import startdb
def userinfo(id):
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM history where userid='%s'"%(id)
    cursor.execute(sql)
    userdata = cursor.fetchall()
    db.commit()
    db.close()
    return userdata