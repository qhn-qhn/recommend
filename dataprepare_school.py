import pandas as pd
from conn import startdb
df = pd.read_excel('./document/院校库.xls',header=0)
db = startdb()
for index, row in df.iterrows():
    name = row[2]
    school_type = row[0]
    location = row[3]
    location_type = row[1]
    belong = row[4]
    yjsy = row[5]
    self_line = row[6]
    sql = "insert into school(id,name,school_type,location,location_type,belong,yjsy,self_line) values "+\
        "(null,'%s','%s','%s','%s','%s','%s','%s')"%(name, school_type, location, location_type, belong, yjsy, self_line)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()