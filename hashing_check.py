from bcrypt import hashpw, checkpw, gensalt
import pyodbc

server = 'DESKTOP-F3QE491\IBAD' 
database = 'Final_Final_Project'  
use_windows_authentication = True 

connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
cursor = connection.cursor()

cursor.execute("select UserID,Password from Users")

lst = []
salt = gensalt(rounds=7)
for i in cursor.fetchall():
    new = [i[0],hashpw(i[1].encode('utf8'), salt).decode('utf8')]

    lst.append(new)

# print(lst)

for j in lst:
    cursor.execute(f"update Users set Password = '{j[1]}' where UserID = {j[0]}")


cursor.execute("select UserID,Password from Users")

for i in cursor.fetchall():

    # print(i)
    # print(i[1].encode('utf-8'))
    # print('1234'.encode('utf-8'))

    print(checkpw('4321'.encode('utf-8'),i[1].encode('utf-8')))

# connection.commit()

# actual_pass = '1234'
# hashed_pass = hashpw(actual_pass.encode(), salt)

# print(checkpw(actual_pass.encode(),hashed_pass))