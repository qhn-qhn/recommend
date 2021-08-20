from conn import startdb
def addschools(data):
    db = startdb()
    cursor  = db.cursor()
    sql = "INSERT INTO school values(null,'%s','%s','%s','%s','%s','%s','%s')" % (data['name'], data['schooltype'], data['location'], data['locationtype'], data['belong'], data['yjsy'], data['selfline'])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        db.close()
        return 0