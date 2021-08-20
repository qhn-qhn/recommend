from conn import startdb
def schmaj(schoolname,majname):
    data=[]
    data.append(schoolname)
    k = len(majname)
    for i in range(k):
        db = startdb()
        cursor = db.cursor()
        sql = "SELECT * FROM schmaj WHERE school='%s' AND major='%s'"%(schoolname,majname[i][2])
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result):
            data.append(1)
        else:
            data.append(0)
        db.commit()
        db.close()
    return data