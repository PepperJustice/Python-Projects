# Step 222 python assignment database
# Author Carla Justice


import sqlite3

#connecting to testwork database and creating table accessing cursor object as cur
conn = sqlite3.connect('testwork.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filename TEXT)")
    conn.commit()

conn = sqlite3.connect('testwork.db')

# tuple of files
file_tuple = ('information.docx', 'Hello.txt', 'myImage.png', \
              'mymovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in the tuple to find the files with txt extension
for x in file_tuple:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (x,))
            print(x)

conn.close()



