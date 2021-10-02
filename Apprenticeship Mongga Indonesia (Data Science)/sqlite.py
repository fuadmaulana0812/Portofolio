#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect("D:\\db.db")
c = conn.cursor()
#execute untuk mengeksekusi cursor
c.execute("DROP TABLE IF EXISTS tab")
c.execute("""CREATE TABLE tab
        (nama text,
        usia INT(255),
        email text)
""")  
#c.execute("INSERT INTO tab VALUES ('Fuad', 21, 'stevenderson0@gmail.com')")
listdata=[
    ('nana',23,'nini@gigimail'),
    ('hahah', 31, 'hahah@gigimail'),
    ('steven', 22, 'steven@gigimail'),
    ('humam', 32, 'human@gigimail'),
    ('fawwaz', 31, 'fawwaz@gigimail')
]

c.executemany("INSERT INTO tab VALUES (?,?,?)", listdata)
#c.executescript("""INSERT INTO tab VALUES ('Fuad', 21, 'gokil')""")

#c.execute("SELECT rowid,* FROM tab ORDER BY nama ASC") #order ASC dan DESC
#c.execute("SELECT rowid, * FROM tab WHERE usia>22 ORDER BY nama")
c.execute("UPDATE tab SET nama='namabaru', usia=32 WHERE usia==31")
c.execute("SELECT rowid,* FROM tab")

items=c.fetchall()
for f in items:
    print(f)
    
#for f in items:
 #   print(f[1])
print(items[0][0])

#c.commit()  #commit menjalankan semua execute
print("bikin data berhasil")
c.close


# In[ ]:




