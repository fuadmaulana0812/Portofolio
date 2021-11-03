#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import time
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


name=['Bayu','Fajar','Ilham','Wahyu','Rizki','Naufal','Tono','Bagus','Asep','Kartika','Ayu','Alma','Nabilah','Putri','Lia','Sari','Siti','Fitri']
nama=list(itertools.product(name, name, name))


# In[3]:


Nama=[]
Email=[]
for i in range(len(nama)):
    Nama.append(nama[i][0]+' '+nama[i][1]+' '+nama[i][2])
    Email.append(nama[i][0]+'_'+nama[i][1]+'_'+nama[i][2]+'@gmail.com')


# In[4]:


Jam_Login=[]
Durasi=[]
for i in range(len(nama)):
    jam=random.randint(25200,79200)
    durasi=random.randint(300,10800)
    Jam_Login.append(time.strftime('%H:%M:%S', time.gmtime(jam)))
    Durasi.append(time.strftime('%H:%M:%S', time.gmtime(durasi)))


# In[5]:


merk=['Vivo','Oppo','Samsung','Xiaomi','Realme','Iphone','Huawei','ASUS','Lenovo','Infinix']
Merk_HP=[]
for i in range(len(nama)):
    hp=random.choice(merk)
    Merk_HP.append(hp)


# In[6]:


No_Telp=[]
for i in range(len(nama)):
    nmr=random.randint(1200000000,9876543210)
    No_Telp.append('08'+str(nmr))


# In[7]:


place=['Kafe','Rumah Sakit','Restoran','Mall','Halte']
nama_tempat=['Permata','Tjantik','Larry','Rainbow','Jaguar','Star','Sunshine','Gemilang','Pesona','Specta','Domo','Gudetama','Sky','Rotello']
Nama_Tempat=list(itertools.product(nama_tempat,nama_tempat))
Location_Type=[]
Nama_Lokasi=[]
for i in range(len(nama)):
    lokasi=random.choice(place)
    Location_Type.append(lokasi)
    k=random.randint(0,len(Nama_Tempat)-1)
    if lokasi=='Rumah Sakit':
        Nama_Lokasi.append('RS '+Nama_Tempat[k][0]+' '+Nama_Tempat[k][1])
    else:
        Nama_Lokasi.append(lokasi+' '+Nama_Tempat[k][0]+' '+Nama_Tempat[k][1])


# In[8]:


interest=['Work Stuff','Sosial Media','Social Connection','Game','Hiburan']
Digital_Interest=[]
for i in range(len(nama)):
    intrs=random.choice(interest)
    Digital_Interest.append(intrs)


# In[9]:


Tahun_Lahir=[]
for i in range(len(nama)):
    tahun=random.randint(1970,2005)
    Tahun_Lahir.append(tahun)


# In[10]:


hari=['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
Hari=[]
for i in range(len(nama)):
    day=random.choice(hari)
    Hari.append(day)


# In[11]:


gender=['Laki-laki','Perempuan']
Jenis_Kelamin=[]
for i in range(len(nama)):
    gen=random.choice(gender)
    Jenis_Kelamin.append(gen)


# In[12]:


provider=['Telkomsel','Indosat','XL','Smartfren','3']
Provider_Seluler=[]
for i in range(len(nama)):
    seluler=random.choice(provider)
    Provider_Seluler.append(seluler)


# In[13]:


Data={'Nama Lokasi':Nama_Lokasi,
       'Hari':Hari,
       'Jam Login':Jam_Login,
       'Nama':Nama,
       'Jenis Kelamin':Jenis_Kelamin,
       'Email':Email,
       'No Telp':No_Telp,
       'Provider Seluler':Provider_Seluler,
       'Tahun Lahir':Tahun_Lahir,
       'Merek HP':Merk_HP,
       'Digital Interest':Digital_Interest,
       'Location Type':Location_Type,
       'Durasi':Durasi}
df=pd.DataFrame(data=Data)


# In[14]:


df.info()
df.head()


# In[15]:


df.to_csv('Data_HIGO.csv',index=False)


# In[ ]:




