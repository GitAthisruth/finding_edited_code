import sqlite3
import time
from datetime import datetime
import os


content = "shajhhashjsa shjasjsgadgjjgksajgkasjk"

conn  = sqlite3.connect('file_tracker.db')

c = conn.cursor()#conn for connect and cursor for start running sql command using execute method(The execute method in SQL is used to run a SQL query or command in a database).

# c.execute("""CREATE TABLE mainfile (
#           file_name text,
#           content text,
#           id TEXT UNIQUE 
#           )""")

current_time = time.strftime('%Y-%m-%d %H:%M:%S')
dt = datetime.today()  
id_In_Seconds = dt.timestamp()
# print(id_In_Seconds)
id = "2025"

originalFilePath = r"C:\Users\LENOVO\Desktop\prizmora\finding_edited_code\org.py"
backupFilePath = "backup_file.py"
original_Basename = os.path.basename(originalFilePath)
backup_Basename = os.path.basename(backupFilePath)
if os.path.exists(originalFilePath):
    with open(originalFilePath,"r") as f:
        original_Content = f.read()
        # print(original_Content)
        # c.execute(f"INSERT INTO mainfile (file_name, content,id) VALUES (?, ?, ?)", ('org.py', original_Content, id))       
c.execute("SELECT * FROM mainfile WHERE id = '2025'")

original_Content_Db = c.fetchone()

print(original_Content_Db)

conn.commit()

conn.close()