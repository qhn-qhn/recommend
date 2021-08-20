from cons.user.rec.content.count import count
from cons.user.rec.content.user import userinfo
from cons.user.rec.content.school import schoolinfo
from cons.user.rec.content.sm import schmaj
from operator import itemgetter
from cons.user.rec.content.sname import schoolname
from conn import startdb

def start(id):
    # print(id)
    # print()
    userdatas = []
    print('1userinfo')
    userdata = userinfo(id)
    # print(userdata)
    userdatas.append(id)
    for j in userdata:
        userdatas.append(j[3])  # 用户向量
    # print(userdatas)
    print('2schoolinfo')
    schooldata = schoolinfo()
    m = len(schooldata)
    schmajdatas = []
    print('3scmaj')
    for i in range(m):
        schmajdata = schmaj(schooldata[i][0], userdata)
        schmajdatas.append(schmajdata)  # 学校向量
    print('schmaj结束')
    print('4count')
    result = count(userdatas, schmajdatas)
    print(result)
    n = sorted(result, key=itemgetter(1), reverse=True)
    db = startdb()
    cursor = db.cursor()
    sql = "DELETE FROM rec1 WHERE userid='%s'" % (id)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()
    for abc in n:
        # print(abc)
        db = startdb()
        cursor = db.cursor()
        sql = "INSERT INTO rec1 VALUES (null,'%s','%s','%s')" % (id, abc[0],abc[1])
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()
    print('5schoolname')
    res = schoolname(n)
    # print(444)
    return(res)