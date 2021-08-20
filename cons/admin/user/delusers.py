from conn import startdb
def delusers(id):
    db = startdb()
    cursor = db.cursor()
    sql = "DELETE FROM user WHERE id='%s'" % (id)
    data = cursor.execute(sql)
    db.commit()
    db.close()
    return data