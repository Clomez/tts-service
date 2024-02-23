import sqlite3

conn = sqlite3.connect('audio_data.db')

conn.execute("DROP TABLE AUDIO")

conn.close()