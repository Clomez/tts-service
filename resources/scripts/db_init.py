import sqlite3

conn = sqlite3.connect('audio_data.db')

conn.execute('''CREATE TABLE AUDIO
         (ID INT PRIMARY KEY NOT NULL,
         NAME           TEXT,
         THEME          TEXT,
         TITLE          TEXT,
         LANGUAGE       text,
         DATE           TEXT,
         USER           TEXT);''')

conn.close()