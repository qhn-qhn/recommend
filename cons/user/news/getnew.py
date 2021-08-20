from conn import startdb
def getnew():
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM news"
    cursor.execute(sql)
    data = cursor.fetchall()
    res = []
    for i in data:
        title = i[1]
        href = i[2]
        time = i[3]
        tmp = {}
        tmp['title'] = title
        tmp['href'] = href
        tmp['time'] = time
        res.append(tmp)
    return res