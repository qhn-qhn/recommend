from conn import startdb
def userinfos(id):
    db = startdb()
    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE id='%s'" % (id)
    cursor.execute(sql)
    data = cursor.fetchone()
    # print(data)
    if len(data) > 0:
        return data
        # return jsonify({'response_status': True,'response_body': [{"data":data}]})
    else:
        return 0