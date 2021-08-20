from conn import startdb
from cons.user.history.addhistory import addhistory
from cons.user.history.addnum import addnum


def history(userid, major):
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM history WHERE userid='%s' AND major='%s'" % (userid, major)

    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    db.commit()
    db.close()
    if len(data) == 0:
        addhistory(userid, major)
    else:
        addnum(data)
