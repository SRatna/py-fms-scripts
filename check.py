import paramiko
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
IP = '192.168.1.73'
username = 'john'
password = 'itahari45'
success = ssh.connect(IP,22, username, password)
# print('cool')
# ssh.exec_command('mysql -uroot -p123')
# cmds = ['cd Documents','ls']
# stdin, stdout, stderr = ssh.exec_command('python3 print.py')
# stdin, stdout, stderr = ssh.exec_command(' ; '.join(cmds))
# ssh.exec_command('create database ram;')
# stdin, stdout, stderr = ssh.exec_command('ls')
# print(stdout.read())
# cur.execute('select * from user')
# for row in cur:
#     ssh.exec_command('python insert_user.py '+ str(row[0]) + ' ' + str(row[1]))
cur.execute('select * from punch_record')
for row in cur:
    stdin, stdout, stderr = ssh.exec_command('python insert_record.py '+ str(row[0])+' '+str(row[1])+' "'+str(row[2])+'" '+str(row[3])+' '+str(row[4]))
    print(stdout.read())
    print(stderr.read())
cur.close()
conn.close()
ssh.close()