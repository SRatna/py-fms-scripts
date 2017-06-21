import paramiko
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
IP = '192.168.1.236'
username = 'alpha'
password = 'Server ko password.'
success = ssh.connect(IP,22, username, password)
# stdin, stdout, stderr = ssh.exec_command('ls')
# cur.execute('select * from user')
cur.execute('select * from user')
for row in cur:
    if row[1] == '':
        name = 'xxx'
    else:
        name = row[1]
    # stdin, stdout, stderr = ssh.exec_command('cd PycharmProjects/test ; python insert_record.py '+ str(row[0])+' '+str(row[1])+' "'+str(row[2])+'" '+str(row[3])+' '+str(row[4]))
    # stdin, stdout, stderr = ssh.exec_command('python insert_record.py '+ str(row[0])+' '+str(row[1])+' "'+str(row[2])+'" '+str(row[3])+' '+str(row[4]))
    stdin, stdout, stderr = ssh.exec_command('python insert_user.py '+ str(row[0])+' '+str(name))
    print(stdout.read())
    print(stderr.read())
cur.close()
conn.close()
# print(stdout.read())
ssh.close()