from conn import startdb
def regists(data):
    db = startdb()
    print(1)
    print(data)
    print(2)
    cursor = db.cursor()
    sql = "DELETE FROM rec2 WHERE userid='%s'" % (data['id'])
    cursor.execute(sql)
    db.commit()
    db.close()
    db = startdb()
    cursor = db.cursor()
    if (data['schoolmajor'] == '985&211'):
        schoolmajor = '985'
    if (data['schoolmajor'] == 'nan'):
        schoolmajor = '普通院校'
    sql = "INSERT INTO user values('%s','%s','%s','%s','%s','%s','%s','0')" % (data['id'], data['username'], data['password'], data['phone'], data['email'], data['schoolname'], data['schoolmajor'])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        db.close()
        return 0