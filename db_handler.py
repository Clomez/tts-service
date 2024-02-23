import sqlite3
from datetime import date

fields = "(ID,NAME,THEME,TITLE,LANGUAGE,DATE,USER) "
insert = "INSERT INTO AUDIO "

def commit_to_audio(data):
    conn = sqlite3.connect('audio_data.db')
    conn.execute(f"{insert}"
                    f"{fields}"
                    f"VALUES ('{data['id']}', '{data['filename']}', '{data['title']}', '{data['theme']}', " 
                    f"'{data['language']}', '{str(date.today())}', '{data['user']}' )")

    conn.commit()
    conn.close()

def read_all_from_audio():
    conn = sqlite3.connect('audio_data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM AUDIO")
    return cur.fetchall()