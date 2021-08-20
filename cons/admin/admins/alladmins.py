from conn import startdb
def alladmins():
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE tag=1"
    cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    db.close()
    if len(data) > 0:
        return data