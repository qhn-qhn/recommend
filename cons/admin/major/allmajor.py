from conn import startdb
def allmajors():
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM majorall"
    cursor.execute(sql)
    data = cursor.fetchall()
    d = []
    db.commit()
    db.close()
    for i in data:
        if i[1] == 'xs':
            type = '学术型硕士'
        else:
            type = '专业型硕士'
        first = i[2]
        second = i[3]
        name = i[4]
        code = i[5]
        tmp = {'type': type, 'first': first, 'second': second, 'name': name, \
               'code': code, 'caozuo1': '修改', 'caozuo2': '删除'}
        d.append(tmp)
    return d
