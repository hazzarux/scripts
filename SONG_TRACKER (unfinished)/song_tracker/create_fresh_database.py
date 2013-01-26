import sqlite3

DATABASE = 'song_tracker.db'

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
cur.execute("create table %s (%s integer primary key, %s text, %s text, %s text, %s text, %s text)" % ('songs','id', 'artist','song','date_added','link','visible'))
conn.commit()
cur.close()
