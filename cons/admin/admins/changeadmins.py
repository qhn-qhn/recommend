from conn import startdb
def changeadmins(data):
    db = startdb()
    cursor = db.cursor()
    sql = "UPDATE user SET username='%s',password='%s',phone='%s',email='%s',schoolname=null,schoolmajor=null WHERE id='%s'" % (data['username'], data['password'], data['phone'], data['email'], data['id'])
    # sql = "INSERT INTO user values('%s','%s','%s','%s','%s','%s','%s')" % (
    # id, username, password, phone, email, schoolname, schoolmajor)
    try:
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()
        return 1
    except:
        db.close()
        return 0