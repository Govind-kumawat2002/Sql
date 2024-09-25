import mysql.connector as mc 
### first method connection
# try:
# config={'user':'root','password':'Jigar@975919','host':'localhost','port':3306}
conn=mc.connect(user='govind' , host ='16.171.33.226' , password = 'govind12345')
if(conn.is_connected()):
    print('jai ho mata Rani')
else:
    print('unable to connect')
sql='CREATE database pdb'
myc=conn.cursor()
try:
    myc.execute(sql)
except:
    print('unable to create database')
myc.close()
conn.close()