from conn import startdb
def logins(id,password):
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE id='%s' and password='%s'" % (id, password)
    cursor.execute(sql)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data