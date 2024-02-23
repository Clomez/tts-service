import sqlite3

conn = sqlite3.connect('audio_data.db')


conn.execute("INSERT INTO AUDIO (ID,NAME,THEME,DATE,USER) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

conn.commit()
conn.close()