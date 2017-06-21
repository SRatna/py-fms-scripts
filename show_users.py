import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='krakra', db='test')
cur = conn.cursor()
while True:
    userInput = input('Enter\n1 to fetch a user\n2 to fetch all users\n')
    if userInput == '1':
        id = input('Please enter user id\n')
        cur.execute('select * from user where id = '+ str(id))
        print('User ID  User Name')
        if cur.rowcount == 0:
            print('No user of id '+str(id)+' found')
        for row in cur:
            print(str(row[0]) + '        ' + row[1])
        break
    if userInput == '2':
        cur.execute('select * from user')
        print('User ID  User Name')
        if cur.rowcount == 0:
            print('No users found')
        for row in cur:
            print(str(row[0])+'        '+row[1])
        break
    if userInput != '1' or userInput != '2':
        print('Please enter either 1 or 2\n')
        continue
cur.close()
conn.close()
