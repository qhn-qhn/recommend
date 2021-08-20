from conn import startdb
def changes(data):
    db = startdb()
    cursor = db.cursor()
    sql = "UPDATE user SET username='%s',password='%s',phone='%s',email='%s',schoolname='%s',schoolmajor='%s' WHERE id='%s'" % (data['username'], data['password'], data['phone'], data['email'], data['schoolname'], data['schoolmajor'],data['id'])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        db.close()
        return 0