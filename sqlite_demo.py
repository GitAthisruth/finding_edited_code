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

originalFilePath = r"C:\Users\LENOVO\Desktop\prizmora\finding_edited_code\org.py"
backupFilePath = "backup_file.py"
original_Basename = os.path.basename(originalFilePath)
backup_Basename = os.path.basename(backupFilePath)
if os.path.exists(originalFilePath):
    with open(originalFilePath,"r") as f:
        original_Content = f.read()
        # print(original_Content)
        c.execute("SELECT * FROM mainfile WHERE id = 1")
        if c.fetchone():
            c.execute("""UPDATE mainfile SET file_name = ?, content = ? WHERE id = ? """, (original_Basename, original_Content, "1"))
        else:
            c.execute(f"INSERT INTO mainfile (file_name, content,id) VALUES (?, ?, ?)", ('org.py', original_Content, "1"))   
        conn.commit()
        print("Database updated successfully.")
    if os.path.exists(backupFilePath):
            with open(backupFilePath,"r") as g:
                backup_File_Content = g.read() 
                # c.execute(f"INSERT INTO mainfile (file_name, content,id) VALUES (?, ?, ?)", ('bkfile.py', backup_File_Content,"2"))   
    else:
        with open(backupFilePath, "w") as g:
            g.write(original_Content)
            print(f"Backup file created: {backupFilePath}")   
original_File_Db = c.execute("SELECT * FROM mainfile WHERE id = 1")
original_Content_Db = c.fetchone()
backup_File_Db = c.execute("SELECT * FROM mainfile WHERE id = 2")
backup_Content_Db = c.fetchone()
conn.commit()
conn.close()
# print(original_Content_Db)
# print(backup_Content_Db)

original_Content_Lines = original_Content_Db[1].splitlines()
backup_Content_Lines = backup_Content_Db[1].splitlines()
# print(original_Content_Lines)
if original_Content_Lines != backup_Content_Lines:
                print(f"editing file is modified..")
                for index in range(len(original_Content_Lines)):
                    print(index)
                    if original_Content_Lines[index]!=backup_Content_Lines[index]:
                        print(f"line :{index+1} of {original_Basename} is changed from {backup_File_Content[index].strip()} to {original_Content_Lines[index].strip()} in backupfile: {backup_Basename}")
else:
    print("no code changes")


