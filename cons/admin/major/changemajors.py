from conn import startdb
def changesmajors(data):
    db = startdb();
    cursor = db.cursor();
    sql = "UPDATE majorall SET type='%s',first='%s',second='%s',code='%s',school_list=null WHERE name='%s'"%(data['type'],data['first'],data['second'],data['code'],data['name'])
    print(data)
    try:
        cursor.execute(sql);
        db.commit();
        db.close();
        return 1;
    except:
        db.close();
        return 0