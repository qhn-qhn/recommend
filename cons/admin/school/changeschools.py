from conn import startdb
def changeschools(data):
    db = startdb()
    cursor = db.cursor()
    sql = "UPDATE school SET school_type='%s',location='%s',location_type='%s',belong='%s',yjsy='%s',self_line='%s' WHERE name='%s'" % (data['school_type'], data['location'], data['location_type'], data['belong'], data['yjsy'], data['self_line'], data['name'])
    try:
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()
        return 1
    except:
        db.close()
        return 0