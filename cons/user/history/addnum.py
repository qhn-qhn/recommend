from conn import startdb
def addnum(data):
    db = startdb()
    cursor = db.cursor()
    before=data[0][3]
    num = before+1
    print(data[0][1])
    sql = "UPDATE history SET num='%s' WHERE userid='%s' AND major='%s'"%(num,data[0][1],data[0][2])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        print('执行')
    except:
        db.close()