#/usr/bin/python3

import sqlite3


conn = sqlite3.connect('./db.sqlite3', check_same_thread=False)

c = conn.cursor()

c.execute(f"SELECT *, DATE(created_at) as date FROM simple_app_newsurls ORDER BY date DESC")