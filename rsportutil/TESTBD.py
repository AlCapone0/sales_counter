import sqlite3


conn = sqlite3.connect('..\db.sqlite3')


cur = conn.cursor()

cur.execute('SELECT * FROM counter_rsportcouter')
print (cur.fetchall())


cur.execute('insert into counter_rsportcouter (id, PortID, DataCreated, ProxyKey) VALUES(NULL, "1", "01.01", "fffffffffff")')
conn.commit()




conn.close()




