from conn import startdb
def delschools(name):
    db = startdb()
    cursor = db.cursor()
    sql = "DELETE FROM school  WHERE name='%s'" % (name)
    try:
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()
        return 1
    except:
        db.close()
        return 0