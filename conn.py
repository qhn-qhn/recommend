import pymysql

def startdb():
    db = pymysql.connect(host="localhost", user="root", password="1234", database="kaoyan")
    return db