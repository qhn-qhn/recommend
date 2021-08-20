from conn import startdb
def showmajors(lx,first,second):
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT DISTINCT(name),code from majorall WHERE type='%s' and first='%s' and second='%s'" % (
    lx, first, second)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    db.close()
    d = []
    if lx == 'zs':
        lx = '专业型硕士'
    else:
        lx = '学术型硕士'
    for i in data:
        name = i[0]
        code = i[1]
        tmp = {'lx': lx, 'first': first, 'second': second, 'name': name, 'code': code}
        d.append(tmp)
    return d