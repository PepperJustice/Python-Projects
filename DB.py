
import sqlite3

conn = sqlite3.connect('new.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name STRING\
        )")
    conn.commit()
conn.close()

