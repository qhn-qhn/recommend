from conn import startdb
def addcomments(id,content,ctime):
    db = startdb()
    cursor = db.cursor()
    sql = "INSERT INTO tieba values(null,'%s','%s','%s')" % (id, content, ctime)
    try:
        cursor.execute(sql)
        db.commit()
        db.commit()
        # 关闭数据库连接
        db.close()
        return 1
    except:
        db.close()
        return 0