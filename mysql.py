import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()
cur.execute("SELECT * FROM user")
for row in cur:
    print(row[0],row[1])

cur.close()
conn.close()