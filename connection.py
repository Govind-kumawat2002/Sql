# import mysql.connector as conn
# try:
#     mydb =conn.connect(host='localhost',user = 'devs',passwd = '1234',use_pure =True)
#     query='SHOW DATABASES'
#     cursor=mydb.cursor()
#     cursor.execute(query)
#     print(cursor.fetchall())
# except Exception as e:
#     mydb.close()
#     print(str(e))
import mysql.connector as mc 
### first method connection
# try:
# config={'user':'root','password':'Jigar@975919','host':'localhost','port':3306}
conn=mc.connect(user='govind' , host ='13.53.168.160' , password = 'govind12345')
if(conn.is_connected()):
    print('jai ho mata Rani')
else:
    print('unable to connect')


# cur = conn.cursor()
# query = "create database ineuron;"
# cur.execute(query)myq