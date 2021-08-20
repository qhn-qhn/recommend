from conn import startdb
def showcomments():
    sql = "SELECT * FROM tieba"
    db = startdb()
    c = db.cursor()
    c.execute(sql)
    res = c.fetchall()
    tmp = []
    for i in res:
        id = i[1]
        content = i[2]
        time = i[3]
        tmp.insert(0, {'id': id, 'content': content, 'time': time})
    return tmp