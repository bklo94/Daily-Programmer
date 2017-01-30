import sqlite3

sqlite_file = '/Users/brand/Desktop/Novel/novel.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('''CREATE TABLE ONLINE_NOVELS
    (ID INT PRIMARY KEY    NOT NULL,
    NOVEL_NAME      TEXT   NOT NULL,
    NOVEL_CURRENT   INT    NOT NULL,
    NOVEL_LATEST    INT    NOT NULL,
    NOVEL_LANG      CHAR(3)   NOT NULL,
    WEBSITE         TEXT   NOT NULL);''')

print "Table ONLINE_NOVELS created"

c.execute('''CREATE TABLE REAL_NOVELS
    (ID INT PRIMARY KEY    NOT NULL,
    NOVEL_NAME      TEXT   NOT NULL,
    NOVEL_CURRENT   INT    NOT NULL,
    NOVEL_LATEST    INT    NOT NULL,
    NOVEL_LANG      CHAR(3)   NOT NULL);''')

print "Table REAL_NOVELS created"

conn.commit()
conn.close()
