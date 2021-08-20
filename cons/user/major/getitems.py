from conn import startdb
def getitems(lx,first):
    # lx = request.values.get("lx")
    if lx == '学术型硕士':
        lx = 'xs'
    if lx == '专业型硕士':
        lx = 'zs'
    # first = request.values.get("first")
    print(lx, first)
    sql = "SELECT DISTINCT(second) from majorall WHERE type='%s' and  first='%s'" % (lx, first)
    db = startdb()
    c = db.cursor()
    c.execute(sql)
    res = c.fetchall()
    tmp = []
    id = 1
    for i in res:
        tmp.append({'title': i[0], 'id': id})
        id += 1
    print(tmp)
    return tmp