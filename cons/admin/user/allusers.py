from conn import startdb
def allusers():
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE tag=0"
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(data) > 0:
        return data
    else:
        return 0