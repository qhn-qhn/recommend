from conn import startdb
def schoolinfo():
    print("3school")
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT name FROM school"
    cursor.execute(sql)
    schooldata = cursor.fetchall()
    db.commit()
    db.close()
    return schooldata