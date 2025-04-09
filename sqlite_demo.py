import sqlite3
import time
from datetime import datetime


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

c.execute(f"INSERT INTO mainfile (file_name, content,id) VALUES (?, ?, ?)", ('org.py', content, id_In_Seconds))       

c.execute("SELECT * FROM mainfile WHERE content = 'shajhhashjsa shjasjsgadgjjgksajgkasjk'")

print(c.fetchone())

conn.commit()

conn.close()