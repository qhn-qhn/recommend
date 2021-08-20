from conn import startdb
def allschool():
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM school"
    cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    db.close()
    d = []
    for i in data:
        id = i[0]
        name = i[1]
        school_type = i[2]
        if school_type == 'nan':
            school_type = ''
        location = i[3]
        location_type = i[4]
        belong = i[5]
        yjsy = i[6]
        if yjsy == 'False':
            yjsy = ''
        if yjsy == 'True':
            yjsy = '√'
        self_line = i[7]
        if self_line == 'False':
            self_line = ''
        if self_line == 'True':
            self_line = '√'
        tmp = {'id': id, 'name': name, 'school_type': school_type, 'location': location, \
               'location_type': location_type, 'belong': belong, 'yjsy': yjsy, \
               'self_line': self_line, 'caozuo1': '修改', 'caozuo2': '删除'}
        d.append(tmp)
    return d