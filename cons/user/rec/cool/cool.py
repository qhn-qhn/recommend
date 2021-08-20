# from user import userinfo
from conn import startdb
from operator import itemgetter


def userinfo(id):
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM user where id='%s'"%(id)
    cursor.execute(sql)
    userdata = cursor.fetchall()
    db.commit()
    db.close()
    return userdata

def schoolnum(schooldata,s):
    results =[]
    print(s)
    for i in schooldata:
        result = []
        result.append(i[1])
        if (i[4] == s[1]):
            result.append(1)
        else:
            result.append(0)
        if (i[2]==s[2]):
            result.append(1)
        else:
            result.append(0)
        print(result)
        results.append(result)

    datas = []
    for j in results:
        data=[]
        data.append(j[0])
        num = (j[1]+j[2])/2
        data.append(num)
        datas.append(data)
        # print(datas)
    return datas



def starts(id):
    # print(id)
    # userdatas=[]
    userdata = userinfo(id)
    s=[]
    s.append(userdata[0][0])
    s.append(userdata[0][5])
    # print(s)
    if (userdata[0][6]=='985'):
        s.append('985&211')
        # print(222)
    elif(userdata[0][6]=='普通院校'):
        s.append('nan')
    else:
        s.append('211')
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM school where location_type='%s' OR school_type='%s'" % (s[1],s[2])
    cursor.execute(sql)
    schooldata = cursor.fetchall()
    db.commit()
    db.close()
    results=schoolnum(schooldata,s)
    results = sorted(results, key=itemgetter(1), reverse=True)
    # print(results)

    for i in results:
        print(i)
        db = startdb()
        cursor = db.cursor()
        sql = "INSERT INTO rec2 VALUES (null,'%s','%s','%s')" % (id, i[0],i[1])
        cursor.execute(sql)
        db.commit()
        db.close()
