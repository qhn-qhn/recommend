import datetime
from flask import Flask, request, jsonify
from conn import startdb
# from new_data import getNew
from cons.user.news.new_data import getNew
from cons.user.userin.logins import logins
from cons.user.userin.regists import regists
from cons.user.userin.userinfos import userinfos
from cons.user.userin.changes import changes
from cons.user.school.selects import selects
from cons.user.major.getitems import getitems
from cons.user.major.showmajors import showmajors
from cons.user.news.getnew import getnew
from cons.user.comment.addcomments import addcomments
from cons.user.comment.showcomment import showcomments
from cons.user.history.history import history
from cons.user.rec.content.info import start
from cons.user.rec.cool.cool import starts
from cons.user.rec.recommend.searchrec import searchrec
from cons.user.rec.recommend.reco import recom

from cons.admin.user.allusers import allusers
from cons.admin.user.delusers import delusers
from cons.admin.school.allschool import allschool
from cons.admin.school.changeschools import changeschools
from cons.admin.school.addschools import addschools
from cons.admin.school.delschools import delschools
from cons.admin.admins.alladmins import alladmins
from cons.admin.admins.addadmins import addadmins
from cons.admin.admins.changeadmins import changeadmins
from cons.admin.major.allmajor import allmajors
from cons.admin.major.addmajors import addmajors
from cons.admin.major.changemajors import changesmajors
from cons.admin.major.delmajors import delmajors

# from werkzeug import SharedDataMiddleware

app = Flask(__name__)


# login
@app.route('/login', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def login():
    # username = request.values.get("username")
    id = request.values.get("id")
    password = request.values.get("password")
    data = logins(id, password)
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM user WHERE id='%s' and password='%s'"%(id, password)
    # cursor.execute(sql)
    # data = cursor.fetchone()
    # print(data)
    if len(data) > 0:
        # a=jsonify({'response_status': True,'response_body': [{"username":data[1]}]})
        # print(a.response);
        return jsonify({'response_status': True, 'response_body': [{"data": data}]})
        # return jsonify({'response_status': True,'response_body': [{"data":data}]})
    else:
        return jsonify({'response_status': False, 'response_body': []})


# regist
@app.route('/regist', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def regist():
    id = request.values.get("id")
    username = request.values.get("username")
    password = request.values.get("password")
    phone = request.values.get("phone")
    email = request.values.get("email")
    schoolname = request.values.get("schoolname")
    schoolmajor = request.values.get("schoolmajor")
    data = {'id': id, 'username': username, 'password': password, 'phone': phone, 'email': email,
            'schoolname': schoolname, 'schoolmajor': schoolmajor}
    result = regists(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql="DELETE FROM rec2 WHERE userid='%s'"%(id)
    # cursor.execute(sql)
    # db.commit()
    # db.close()
    # db = startdb()
    # cursor = db.cursor()
    # if (schoolmajor == '985&211'):
    #     schoolmajor = '985'
    # if (schoolmajor=='nan'):
    #     schoolmajor='普通院校'
    # sql = "INSERT INTO user values('%s','%s','%s','%s','%s','%s','%s','0')"%(id,username, password,phone,email,schoolname,schoolmajor)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # 关闭数据库连接
    #     db.close()
    #     return jsonify({'response_status': True, 'response_body': []})
    # except:
    #     db.close()
    #     return jsonify({'response_status': False, 'response_body': []})


# 用户信息
@app.route("/userinfo", methods=['POST'])
def userinfo():
    id = request.values.get("useri")
    data = userinfos(id)
    if data != 0:
        return jsonify({'response_status': True, 'response_body': [{"data": data}]})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM user WHERE id='%s'" % (id)
    # cursor.execute(sql)
    # data = cursor.fetchone()
    # # print(data)
    # if len(data) > 0:
    #     a = jsonify({'response_status': True, 'response_body': [{"data": data}]})
    #     # print(a.response);
    #     return jsonify({'response_status': True, 'response_body': [{"data": data}]})
    #     # return jsonify({'response_status': True,'response_body': [{"data":data}]})
    # else:
    #     return jsonify({'response_status': False, 'response_body': []})


# 修改用户信息
@app.route("/change", methods=['POST'])
def change():
    id = request.values.get("id")
    username = request.values.get("username")
    password = request.values.get("password")
    phone = request.values.get("phone")
    email = request.values.get("email")
    schoolname = request.values.get("schoolname")
    schoolmajor = request.values.get("schoolmajor")
    data = {'id': id, 'username': username, 'password': password, 'phone': phone, 'email': email,
            'schoolname': schoolname, 'schoolmajor': schoolmajor}
    result = changes(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "UPDATE user SET username='%s',password='%s',phone='%s',email='%s',schoolname='%s',schoolmajor='%s' WHERE id='%s'"%(username, password,phone,email,schoolname,schoolmajor,id)
    # # sql = "INSERT INTO user values('%s','%s','%s','%s','%s','%s','%s')" % (
    # # id, username, password, phone, email, schoolname, schoolmajor)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # 关闭数据库连接
    #     db.close()
    #     return jsonify({'response_status': True, 'response_body': []})
    # except:
    #     db.close()
    #     return jsonify({'response_status': False, 'response_body': []})


# 院校信息
@app.route('/showschool', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def select():
    d = selects()
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM school"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # d = []
    # for i in data:
    #     id = i[0]
    #     name = i[1]
    #     school_type = i[2]
    #     if school_type=='nan':
    #         school_type = ''
    #     location = i[3]
    #     location_type = i[4]
    #     belong = i[5]
    #     yjsy = i[6]
    #     if yjsy=='False':
    #         yjsy = ''
    #     if yjsy=='True':
    #         yjsy = '√'
    #     self_line = i[7]
    #     if self_line=='False':
    #         self_line = ''
    #     if self_line=='True':
    #         self_line = '√'
    #     tmp = {'id':id, 'name':name,'school_type': school_type, 'location':location,\
    #            'location_type': location_type, 'belong': belong, 'yjsy': yjsy,\
    #            'self_line': self_line}
    #     d.append(tmp)
    # print(len(data))
    # print(len(d))
    return jsonify({
        "code": 0,
        "msg": "",
        "count": len(d),
        "data": d
    })


# 专业查询
@app.route('/getitem', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def getitem():
    lx = request.values.get("lx")
    if lx == '学术型硕士':
        lx = 'xs'
    if lx == '专业型硕士':
        lx = 'zs'
    first = request.values.get("first")
    tmp = getitems(lx, first)
    # print(lx, first)
    # sql = "SELECT DISTINCT(second) from majorall WHERE type='%s' and  first='%s'"%(lx, first)
    # db = startdb()
    # c = db.cursor()
    # c.execute(sql)
    # res = c.fetchall()
    # tmp = []
    # id = 1
    # for i in res:
    #     tmp.append({'title':i[0],'id':id})
    #     id += 1
    return jsonify({'response_status': True, 'response_body': tmp})


# 专业信息
@app.route('/showmajor', methods=['GET'])  # 关于route（）里面可以写url，提交的方式
def showmajor():
    lx = request.values.get("lx")
    if lx == '学术型硕士':
        lx = 'xs'
    if lx == '专业型硕士':
        lx = 'zs'
    first = request.values.get("first")
    second = request.values.get("second")
    d = showmajors(lx, first, second)
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT DISTINCT(name),code from majorall WHERE type='%s' and first='%s' and second='%s'"%(lx, first, second)
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # d = []
    # if lx == 'zs':
    #     lx = '专业型硕士'
    # else:
    #     lx = '学术型硕士'
    # for i in data:
    #     name = i[0]
    #     code = i[1]
    #     tmp = {'lx':lx,  'first': first, 'second':second, 'name':name, 'code':code }
    #     d.append(tmp)
    return jsonify({
        "code": 0,
        "msg": "",
        "count": len(d),
        "data": d
    })


# 国家政策信息
@app.route('/getnews', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def getnews():
    res = getnew()
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM news"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # res = []
    # for i in data:
    #     title = i[1]
    #     href = i[2]
    #     time = i[3]
    #     tmp = {}
    #     tmp['title'] = title
    #     tmp['href'] = href
    #     tmp['time'] = time
    #     res.append(tmp)
    return jsonify({'response_status': True, 'response_body': res})


# refreashnews
@app.route('/refreashnews', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def refreashnews():
    try:
        getNew()
        return jsonify({'response_status': True, 'response_body': []})
    except:
        return jsonify({'response_status': False, 'response_body': []})


# addcommment
@app.route('/addcomment', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def addcomment():
    id = request.values.get('useri')
    content = request.values.get("content")
    d = datetime.datetime.now()
    ctime = f"{d:%B %d %Y}"
    result = addcomments(id, content, ctime)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "INSERT INTO tieba values(null,'%s','%s','%s')" % (id,content, ctime)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     db.commit()
    #     # 关闭数据库连接
    #     db.close()
    #     return jsonify({'response_status': True, 'response_body': []})
    # except:
    #     db.close()


# showcommment
@app.route('/showcomment', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def showcomment():
    tmp = showcomments()
    # sql = "SELECT * FROM tieba"
    # db = startdb()
    # c = db.cursor()
    # c.execute(sql)
    # res = c.fetchall()
    # tmp = []
    # for i in res:
    #     id = i[1]
    #     content = i[2]
    #     time = i[3]
    #     tmp.insert(0, {'id':id, 'content':content, 'time':time})
    return jsonify({'response_status': True, 'response_body': tmp})


# 没有迁移
# 搜索
@app.route('/search', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def search():
    # 地区
    r1 = request.values.get("r1")
    r1 = r1[:1]

    # xs or zs
    r2 = request.values.get("r2")
    type = ''
    if r2 == "学术型硕士":
        type = 'xs'
    if r2 == "专业型硕士":
        type = 'zs'
    # 专业名称或代码
    name = ''
    code = ''
    r3 = request.values.get("r3")
    id = request.values.get("id")
    print(1111111)
    history(id, r3)

    # print(r1,r2,r3)
    def check_contain_chinese(check_str):
        for ch in check_str.encode('utf-8').decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def getLocation(school_name):
        sql = "SELECT location_type FROM school WHERE name='%s' " % (school_name)
        db = startdb()
        c = db.cursor()
        c.execute(sql)
        r = c.fetchone()
        return r[0][0]

    # r = getLocation('兰州大学')
    s = ''
    if (check_contain_chinese(r3)) == True:
        name = r3
        s = "SELECT school_list FROM majorall WHERE type='%s' and name='%s' " % (type, name)
    else:
        code = r3
        s = "SELECT school_list FROM majorall WHERE type='%s' and code='%s' " % (type, code)
    d = startdb()
    cu = d.cursor()
    cu.execute(s)
    r = cu.fetchone()
    tmp = []
    if r != None:
        school_list = r[0]
        ll = str(school_list).split('-')
        for i in ll:
            if getLocation(i) != r1:
                continue
            else:
                tmp.append({'school': i})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    return jsonify({'response_status': True, 'response_body': tmp})


# 基于内容
@app.route('/yxtj', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def yxtj():
    # print('1start')
    id = request.values.get("id")
    result = start(id)
    print('结束')
    return jsonify({'response_status': True, 'response_body': [{'data': id}]})


# 基于标签
@app.route('/initrec', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def initrec():
    id = request.values.get("id")
    starts(id)
    return jsonify({'response_status': True, 'response_body': []})


# 推荐院校信息
@app.route('/yxcx', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def yxcx():
    id = request.values.get("useri")
    s = searchrec(id)
    # print('123')
    # print(s)
    return jsonify({'response_status': True, 'response_body': [{'data': s}]})
    # print(id)
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT school,num FROM rec1 WHERE userid='%s'"%(id)
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # db.commit()
    # # 关闭数据库连接
    # db.close()
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT school,num FROM rec2 WHERE userid='%s'" % (id)
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # db.commit()
    # # 关闭数据库连接
    # db.close()
    # if (len(data)==0):
    #     s=[]
    #     for i in datas:
    #         s.append(i[0])
    #     return jsonify({'response_status': True, 'response_body': [{'data':s}]})
    # else:
    #     s=recom(data,datas)
    #     print(s)
    #     return jsonify({'response_status': True, 'response_body': [{'data':s}]})


# 所有用户信息
@app.route('/alluser', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def alluser():
    data = allusers()
    if data != 0:
        return jsonify({'response_status': True, 'response_body': [{"data": data}]})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM user WHERE tag=0"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # if len(data) > 0:
    #     return jsonify({'response_status': True, 'response_body': [{"data": data}]})


# 删除用户信息
@app.route('/deluser', methods=['POST'])
def deluser():
    id = request.values.get("id")
    # print(id)
    data = delusers(id)
    # db = startdb()
    # cursor = db.cursor()
    # # sql = "DELETE FROM user WHERE id='%s'"%(id)
    # sql = "DELETE FROM user WHERE id='%s'" % (id)
    # data=cursor.execute(sql)
    # db.commit()
    # db.close()
    # print(data)
    return jsonify({'response_status': True, 'response_body': [{"data": data}]})


# 所有管理员信息
@app.route("/alladmin", methods=['POST'])
def alladmin():
    data = alladmins()
    print(data)
    return jsonify({'response_status': True, 'response_body': [{"data": data}]})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM user WHERE tag=1"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # if len(data) > 0:
    #     return jsonify({'response_status': True, 'response_body': [{"data": data}]})


# 添加管理员信息
@app.route('/addadmin', methods=['POST'])
def addadmin():
    id = request.values.get("id")
    username = request.values.get("username")
    password = request.values.get("password")
    phone = request.values.get("phone")
    email = request.values.get("email")
    data = {'id': id, 'username': username, 'password': password, 'phone': phone, 'email': email}
    result = addadmins(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "INSERT INTO user values('%s','%s','%s','%s','%s',null,null,'1')"%(id,username, password,phone,email)
    # try:
    #     cursor.execute(sql)
    #     print(22222)
    #     db.commit()
    #     # 关闭数据库连接
    #     db.close()
    #     return jsonify({'response_status': True, 'response_body': []})
    # except:
    #     db.close()
    #     return jsonify({'response_status': False, 'response_body': []})


# 修改管理员信息
@app.route("/changeadmin", methods=['POST'])
def changeadmin():
    id = request.values.get("id")
    username = request.values.get("username")
    password = request.values.get("password")
    phone = request.values.get("phone")
    email = request.values.get("email")
    data = {'id': id, 'username': username, 'password': password, 'phone': phone, 'email': email}
    result = changeadmins(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "UPDATE user SET username='%s',password='%s',phone='%s',email='%s',schoolname=null,schoolmajor=null WHERE id='%s'"%(username, password,phone,email,id)
    # # sql = "INSERT INTO user values('%s','%s','%s','%s','%s','%s','%s')" % (
    # # id, username, password, phone, email, schoolname, schoolmajor)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # 关闭数据库连接
    #     db.close()
    #     return jsonify({'response_status': True, 'response_body': []})
    # except:
    #     db.close()
    #     return jsonify({'response_status': False, 'response_body': []})


# 所有学校信息
@app.route('/manageschool', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def manageschool():
    d = allschool()
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM school"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # d = []
    # for i in data:
    #     id = i[0]
    #     name = i[1]
    #     school_type = i[2]
    #     if school_type=='nan':
    #         school_type = ''
    #     location = i[3]
    #     location_type = i[4]
    #     belong = i[5]
    #     yjsy = i[6]
    #     if yjsy=='False':
    #         yjsy = ''
    #     if yjsy=='True':
    #         yjsy = '√'
    #     self_line = i[7]
    #     if self_line=='False':
    #         self_line = ''
    #     if self_line=='True':
    #         self_line = '√'
    #     tmp = {'id':id, 'name':name,'school_type': school_type, 'location':location,\
    #            'location_type': location_type, 'belong': belong, 'yjsy': yjsy,\
    #            'self_line': self_line,'caozuo1':'修改','caozuo2':'删除'}
    #     d.append(tmp)
    return jsonify({
        "code": 0,
        "msg": "",
        "count": len(d),
        "data": d,
    })


# 添加学校信息
@app.route("/addschool", methods=['post'])
def addschool():
    name = request.values.get("name")
    schooltype = request.values.get("schooltype")
    location = request.values.get("location")
    locationtype = request.values.get("locationtype")
    belong = request.values.get("belong")
    yjsy = request.values.get("yjsy")
    selfline = request.values.get("selfline")
    data = {'name': name, 'schooltype': schooltype, 'location': location, 'locationtype': locationtype,
            'belong': belong, 'yjsy': yjsy, 'selfline': selfline};
    result = addschools(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_statue': False, 'response_body': []})


# 修改学校信息
@app.route("/changeschool", methods=['POST'])
def changeschool():
    name = request.values.get("name")
    school_type = request.values.get("school_type")
    location = request.values.get("location")
    location_type = request.values.get("location_type")
    belong = request.values.get("belong")
    yjsy = request.values.get("yjsy")
    self_line = request.values.get("self_line")
    # print(self_line)
    if (self_line == '√'):
        self_line = True
    else:
        self_line = False
    if (yjsy == '√'):
        yjsy = True
    else:
        yjsy = False
    data = {'name': name, 'school_type': school_type, 'location': location, 'location_type': location_type,
            'belong': belong, 'yjsy': yjsy, 'self_line': self_line}
    result = changeschools(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "UPDATE school SET school_type='%s',location='%s',location_type='%s',belong='%s',yjsy='%s',self_line='%s' WHERE name='%s'"%(school_type, location,location_type,belong,yjsy,self_line,name)
    # # sql = "INSERT INTO user values('%s','%s','%s','%s','%s','%s','%s')" % (
    # # id, username, password, phone, email, schoolname, schoolmajor)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # 关闭数据库连接
    #     db.close()
    #     return jsonify({'response_status': True, 'response_body': []})
    # except:
    #     db.close()
    #     return jsonify({'response_status': False, 'response_body': []})


# 删除学校信息
@app.route("/delschool", methods=['POST'])
def delschool():
    name = request.values.get("name")
    result = delschools(name)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})
    # db = startdb()
    # cursor = db.cursor()
    # sql = "DELETE FROM school  WHERE name='%s'"%(name)
    # # sql = "INSERT INTO user values('%s','%s','%s','%s','%s','%s','%s')" % (
    # # id, username, password, phone, email, schoolname, schoolmajor)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # 关闭数据库连接
    #     db.close()
    #     return jsonify({'response_status': True, 'response_body': []})
    # except:
    #     db.close()
    #     return jsonify({'response_status': False, 'response_body': []})


# 所有专业信息
@app.route('/managemajor', methods=['POST'])  # 关于route（）里面可以写url，提交的方式
def managemajor():
    d = allmajors()
    # db = startdb()
    # cursor = db.cursor()
    # sql = "SELECT * FROM majorall"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # d = []
    # db.commit()
    # db.close()
    # print(data)
    # for i in data:
    #     if i[1]=='xs':
    #         type='学术型硕士'
    #     else:
    #         type='专业型硕士'
    #     first = i[2]
    #     second = i[3]
    #     name = i[4]
    #     code = i[5]
    #     tmp = {'type':type, 'first':first,'second': second, 'name':name,\
    #            'code': code,'caozuo1':'修改','caozuo2':'删除'}
    #     d.append(tmp)
    return jsonify({
        "code": 0,
        "msg": "",
        "count": len(d),
        "data": d,
    })


# 添加专业信息
@app.route('/addmajor', methods=['post'])
def addmajor():
    type = request.values.get('type');
    first = request.values.get('first');
    second = request.values.get('second');
    name = request.values.get('name');
    code = request.values.get('code');
    data = {
        'type': type,
        'first': first,
        'second': second,
        'name': name,
        'code': code,
    };
    result = addmajors(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'reponse_body': []})


# 修改专业信息
@app.route('/changemajor', methods=['post'])
def changemajor():
    type = request.values.get('type')
    if type == '学术型硕士':
        type = 'xs'
    else:
        type = 'zs'
    first = request.values.get('first')
    second = request.values.get('second')
    name = request.values.get('name')
    code = request.values.get('code')
    data = {'type': type, 'first': first, 'second': second, 'name': name, 'code': code}
    result = changesmajors(data)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})


# 删除专业
@app.route('/delmajor', methods=['post'])
def delmajor():
    name = request.values.get('name')
    result = delmajors(name)
    if result == 1:
        return jsonify({'response_status': True, 'response_body': []})
    else:
        return jsonify({'response_status': False, 'response_body': []})


if __name__ == '__main__':
    app.debug = True


    # 跨域支持
    def after_request(resp):
        # resp = make_response(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return resp
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        # return resp


    app.after_request(after_request)
    app.run(host='0.0.0.0', port=1005)
