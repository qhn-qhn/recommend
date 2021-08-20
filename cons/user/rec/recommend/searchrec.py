from conn import startdb
from cons.user.rec.recommend.reco import recom
def searchrec(id):
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT school,num FROM rec1 WHERE userid='%s'" % (id)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    # 关闭数据库连接
    db.close()
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT school,num FROM rec2 WHERE userid='%s'" % (id)
    cursor.execute(sql)
    datas = cursor.fetchall()
    db.commit()
    # 关闭数据库连接
    db.close()
    if (len(data) == 0):
        s = []
        for i in datas:
            s.append(i[0])
        return s
    else:
        s = recom(data, datas)
        return s