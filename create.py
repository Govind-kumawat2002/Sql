import mysql.connector as mc


conn=mc.connect(user='govind' , host ='16.171.33.226' , password = 'govind12345',database='pdb')

try:
    conn=mc.connect(**conn)
    if(conn.is_connected()):
        print('connected')
except:
    print('unable to connect')
# connection has eastablished


query = 'CREATE table ineuronStudent(stuid INT not null  AUTO_INCREMENT PRIMARY KEY,name varchar(30),roll int,age int ,city varchar(30))'   # no need to specify semicolon
myc=conn.cursor()

try:
    myc.execute(query)
    conn.commit()
    print('your table has been created')
except:
    print('unable to create table')
    conn.rollback()
myc.close()
conn.close()
