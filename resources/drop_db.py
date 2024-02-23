import sqlite3

conn = sqlite3.connect('test.db')

conn.execute("DROP TABLE AUDIO")

conn.close()