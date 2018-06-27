#!/usr/bin/python
# -*- coding UTF-8 -*-

import sqlite3

try:
    conn = sqlite3.connect("test.db")
    print("连上了")
except Exception:
    print("没连上")

c = conn.cursor()
sql = "select * from item"
c.execute(sql)
print(c.fetchall())
conn.commit()
conn.close()
