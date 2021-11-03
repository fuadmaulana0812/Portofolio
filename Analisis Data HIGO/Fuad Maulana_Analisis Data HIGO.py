#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("D:/Karir/HIGO - Data Scientist/Data_HIGO.csv",converters={'No Telp': lambda x: str(x)})
df.info()
df.head()


# In[3]:


#Top 9 Nama Tempat dengan Pengguna Terbanyak
Place1=df['Nama Lokasi'].value_counts()
Place1=Place1[:9]

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(Place1.index, Place1, align='center', color='brown')
ax.set_yticklabels(Place1.index)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Nama Tempat Lokasi')
ax.set_title('Jumlah Pengguna Berdasarkan Tempat Lokasi', size=16)

rects=ax.patches

labels=[f"{i}" for i in Place1]

#Make Labels
for rect,label in zip(rects,labels):
    width=rect.get_width()
    ax.text(width,rect.get_y()+rect.get_height()/2,label,ha='left',va='center')

plt.show()


# In[4]:


#Jumlah Pengguna Berdasarkan Hari
D=df['Hari'].value_counts()
day=['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
Day=D[day]

plt.rcdefaults()
fig, ax = plt.subplots()

ax.bar(day, Day, align='center')
ax.set_xticklabels(day)
#ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Jumlah Pengguna')
ax.set_title('Jumlah Pengguna Berdasarkan Hari', size=16)

rects=ax.patches

labels=[f"{i}" for i in Day]

#Make Labels
for rect,label in zip(rects,labels):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha='center',va='bottom')

plt.show()


# In[8]:


#Membuat Confidence Interval untuk populasi rata - rata pengguna per hari
#n=7 => Cofidence Interval menggunakan distribusi t
CI1=st.t.interval(alpha=0.95,df=len(Day)-1,loc=np.mean(Day),scale=st.sem(Day))
CI1


# In[9]:


print('Jumlah pengguna yang menggunakan Wifi HIGOspot paling banyak di hari',D.index[0],'dengan jumlah',max(Day),'pengguna')
print('Jumlah pengguna yang menggunakan Wifi HIGOspot paling sedikit di hari',D.index[-1],'dengan jumlah',min(Day),'pengguna')
print('Rata - rata pengguna per hari adalah',Day.sum()/len(Day.index))
print('Confidence Interval rata - rata jumlah pengguna per hari adalah',CI1[0],'-',CI1[1])


# In[10]:


#Jumlah Pengguna Berdasarkan Jenis Kelamin
gender=df['Jenis Kelamin'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(gender,labels=gender.index,autopct='%1.2f%%')
plt.title('Presentase Jenis Kelamin Pengguna', size=16)
plt.show()


# In[11]:


print('Pengguna',gender.index[0],'lebih banyak daripada pengguna',gender.index[1],'dengan jumlah',gender[0],'pengguna',gender.index[0])


# In[12]:


#Jumlah Pengguna Berdasarkan Kelompok Usia
tahun=df['Tahun Lahir'].value_counts()
now_year=2021
umur=[now_year-i for i in df['Tahun Lahir']]

#Membuat kelompok interval umur
gol_16_22=0
gol_23_29=0
gol_30_36=0
gol_37_43=0
gol_44_51=0
for i in umur:
    if i in range(16,23):
        gol_16_22+=1
    elif i in range(23,30):
        gol_23_29+=1
    elif i in range(30,37):
        gol_30_36+=1
    elif i in range(37,44):
        gol_37_43+=1
    elif i in range(44,52):
        gol_44_51+=1
Umur=pd.Series(data={'16-22':gol_16_22,'23-29':gol_23_29,'30-36':gol_30_36,'37-43':gol_37_43,'44-51':gol_44_51})

#make pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(Umur,labels='Usia '+Umur.index+' Tahun',autopct='%1.2f%%')
plt.title('Presentase Jumlah Pengguna Berdasarkan Kelompok Usia', size=16)
plt.show()


# In[13]:


#Membuat Confidence Interval untuk populasi rata - rata umur pengguna
#n=5832 => Cofidence Interval menggunakan distribusi z (normal)
CI2=st.norm.interval(alpha=0.95,loc=np.mean(umur),scale=st.sem(umur))
CI2


# In[16]:


Umur=Umur.sort_values()
print('Jumlah pengguna terbanyak adalah pengguna dengan usia',Umur.index[-1],'Tahun, dengan jumlah',Umur.max(),'pengguna')
print('Jumlah pengguna terkecil adalah pengguna dengan usia',Umur.index[0],'dan usia',Umur.index[1],'Tahun, dengan jumlah',Umur.min(),'pengguna')
print('Rata-rata usia pengguna adalah',np.mean(umur),'Tahun')
print('Confidence Interval rata - rata usia pengguna adalah',CI2[0],'-',CI2[1])


# In[17]:


#Jumlah Pengguna Berdasarkan Provider Seluler
provider=df['Provider Seluler'].value_counts(sort=False)

plt.rcdefaults()
fig, ax = plt.subplots()

ax.bar(provider.index, provider, align='center',color='gray')
ax.set_xticklabels(provider.index, rotation=45)
ax.set_ylabel('Jumlah Pengguna')
ax.set_title('Jumlah Pengguna Berdasarkan Provider Seluler', size=16)

rects=ax.patches

labels=[f"{i}" for i in provider]

#Make Labels
for rect,label in zip(rects,labels):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha='center',va='bottom')

plt.show()


# In[18]:


print('Provider dengan jumlah pengguna terbanyak adalah',provider.idxmax(),'dengan total',provider.max(),'pengguna')
print('Provider dengan jumlah pengguna terkecil adalah',provider.idxmin(),'dengan total',provider.min(),'pengguna')


# In[19]:


#Jumlah Pengguna Berdasarkan Merk HP
merk=df['Merek HP'].value_counts()

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(8,8))

ax.barh(merk.index, merk, align='center', color='green')
ax.set_yticklabels(merk.index)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Merek HP')
ax.set_title('Jumlah Pengguna Berdasarkan Merk HP', size=16)

rects=ax.patches

labels=[f"{i}" for i in merk]

#Make Labels
for rect,label in zip(rects,labels):
    width=rect.get_width()
    ax.text(width,rect.get_y()+rect.get_height()/2,label,ha='left',va='center')

plt.show()


# In[20]:


print(merk.index[0],'adalah merk HP yang paling banyak digunakan oleh pengguna Wifi HIGO dengan jumlah',max(merk),'pengguna')
print(merk.index[-1],'adalah merk HP yang paling sedikit digunakan oleh pengguna Wifi HIGO dengan jumlah',min(merk),'pengguna')


# In[21]:


#Jumlah Pengguna Berdasarkan Digital Interest
interest=df['Digital Interest'].value_counts(sort=False)

plt.rcdefaults()
fig, ax = plt.subplots()

ax.bar(interest.index, interest, align='center',color='red')
ax.set_xticklabels(interest.index, rotation=45)
ax.set_ylabel('Jumlah Pengguna')
ax.set_title('Jumlah Pengguna Berdasarkan Digital Interest', size=16)

rects=ax.patches

labels=[f"{i}" for i in interest]

#Make Labels
for rect,label in zip(rects,labels):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha='center',va='bottom')

plt.show()


# In[22]:


print('Pengguna memiliki ketertarikan terhadap',interest.idxmax(),'ketika menggunakan Wifi HIGO dengan jumlah',interest.max(),'pengguna')
print('Pengguna kurang tertarik terhadap',interest.idxmin(),'ketika menggunakan Wifi HIGO dengan jumlah',interest.min(),'pengguna')


# In[23]:


#Jumlah Pengguna Berdasarkan Location Type
LT=df['Location Type'].value_counts()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(LT,labels=LT.index,autopct='%1.2f%%')
plt.title('Jumlah Pengguna Berdasarkan Jenis Tempat', size=16)
plt.show()


# In[24]:


print('Pengguna lebih banyak mengunjungi',LT.idxmax(),'dengan total',LT.max(),'pengguna')
print('Pengguna lebih sedikit mengunjungi',LT.idxmin(),'dengan total',LT.min(),'pengguna')


# In[31]:


#Analisis Durasi Pengguna Dalam Menggunakan Wifi HIGO
maksimal=max(df['Durasi'])
minimal=min(df['Durasi'])
print('Pengguna menggunakan wifi HIGO paling lama selama',int(maksimal[:2]),'jam',int(maksimal[3:5]),'menit',int(maksimal[6:8]),'detik')
print('Pengguna menggunakan wifi HIGO paling cepat selama',int(minimal[:2]),'jam',int(minimal[3:5]),'menit',int(minimal[6:8]),'detik')
durasi_s=[]
for i in df['Durasi']:
    jam=int(i[:2])*60*60
    menit=int(i[3:5])*60
    detik=int(i[6:8])
    waktu=jam+menit+detik
    durasi_s.append(waktu)
rata2=np.mean(durasi_s)

import time
waktu_rata=time.strftime('%H:%M:%S', time.gmtime(rata2))
print('Rata - rata durasi pengguna menggunakan wifi HIGO adalah',waktu_rata[:2],'jam',waktu_rata[3:5],'menit',waktu_rata[6:8],'detik')

#Membuat Confidence Interval untuk populasi rata - rata durasi yang digunakan oleh setiap pengguna
#n=5832 => Cofidence Interval menggunakan distribusi z (normal)
CI3=st.norm.interval(alpha=0.95,loc=rata2,scale=st.sem(durasi_s))
CI3_1=time.strftime('%H:%M:%S', time.gmtime(CI3[0]))
CI3_2=time.strftime('%H:%M:%S', time.gmtime(CI3[1]))
print('Confidence Interval rata - rata durasi penggunaan Wifi HIGO adalah',CI3_1[:2],'jam',CI3_1[3:5],'menit',CI3_1[6:8],'detik hingga',CI3_2[:2],'jam',CI3_2[3:5],'menit',CI3_2[6:8],'detik')


# In[32]:


#Analisis Interval Jam Dengan Pengguna Terbanyak
all_time=df['Jam Login']
all_jam=[int(i[:2]) for i in all_time]
all_jam=pd.Series(all_jam)
K=list(range(7,22))
All_Jam=all_jam.value_counts()
All_Jam=All_Jam[K]
indeks=[]
for i in K:
    indeks.append(str(i)+'-'+str(i+1))

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(indeks,All_Jam,marker='o')
ax.set_title('Jumkah Pengguna Berdasarkan Interval Waktu Login')
ax.set_xlabel('Interval Jam')
ax.set_ylabel('Jumlah Pengguna')
ax.set_xticklabels(indeks,rotation=45)
ax.set_ylim(ymin=0,ymax=455)

rects=ax.lines[0]
for x_value,y_value in zip(indeks,All_Jam):
    label="{:.2f}".format(y_value)
    ax.annotate(label,(x_value,y_value),xytext=(0,5),textcoords='offset points',ha='center',va='bottom')

plt.show()


# In[38]:


print('Pengguna terbanyak terjadi pada jam',str(All_Jam.idxmax())+'.00','sampai jam',str(All_Jam.idxmax()+1)+'.00')

#Membuat Confidence Interval untuk populasi rata - rata pengguna per jam
#n=15 => Cofidence Interval menggunakan distribusi t
CI4=st.t.interval(alpha=0.95,df=len(All_Jam),loc=np.mean(All_Jam),scale=st.sem(All_Jam))
print('Confidence Interval rata - rata pengguna per jam adalah',CI4[0],'-',CI4[1],'pengguna')

#Confidence Interval untuk populasi rata-rata jam login
#n=5832 => Confidence Interval menggunakan distribusi z (normal)
CI5=st.norm.interval(alpha=0.95,loc=np.mean(all_jam),scale=st.sem(all_jam))
print('Confidence Interval rata - rata jam login pengguna adalah jam',CI5[0],'-',CI5[1])


# In[39]:


Ramai=[]
Jumlah=[]
for i in day:
    j=df[(df['Hari']==i)]
    l=[int(ii[:2]) for ii in j['Jam Login']]
    l=pd.Series(l)
    m=l.value_counts()
    idx=str(m.idxmax())+' - '+str(m.idxmax()+1)
    Ramai.append(idx)
    Jumlah.append(m.max())

Data_Ramai_Pengguna=pd.DataFrame(data={'Interval Jam':Ramai,'Jumlah':Jumlah},index=day)


# In[41]:


print('Berikut adalah data tentang interval jam yang paling banyak pengguna melakukan login ke Wifi HIGO')
Data_Ramai_Pengguna


# In[42]:


#Analisis Digital Interest Berdasarkan Rata-Rata Durasi
rata_rata=[]
for i in df['Digital Interest'].unique():
    Data1=df[df['Digital Interest']==i]
    x=0
    for j in Data1['Durasi']:
        dur=int(j[:2])*3600+int(j[3:5])*60+int(j[6:8])
        x+=dur
    rata=time.strftime('%H:%M:%S', time.gmtime(x/len(Data1)))
    rata_rata.append(rata)
df3=pd.Series(rata_rata,index=df['Digital Interest'].unique())


# In[43]:


print('Berikut adalah rata - rata durasi yang dihabiskan pengguna terhadap Digital Interest')
df3


# In[44]:


#Analisis Jenis Lokasi Berdasarkan Rata-Rata Durasi
rata_rata=[]
for i in df['Location Type'].unique():
    Data1=df[df['Location Type']==i]
    x=0
    for j in Data1['Durasi']:
        dur=int(j[:2])*3600+int(j[3:5])*60+int(j[6:8])
        x+=dur
    rata=time.strftime('%H:%M:%S', time.gmtime(x/len(Data1)))
    rata_rata.append(rata)
df4=pd.Series(rata_rata,index=df['Location Type'].unique())


# In[45]:


print('Berikut adalah rata - rata durasi yang dihabiskan pengguna ditempat lokasi')
df4


# In[46]:


#Analisis Kelompok Usia Pada Setiap Digital Interest
now_year=2021
df6=[]
idks=df['Digital Interest'].unique()
for i in idks:
    df_intr=df[df['Digital Interest']==i]
    umur=[now_year-i for i in df_intr['Tahun Lahir']]

    #Membuat kelompok interval umur
    gol_16_22=0
    gol_23_29=0
    gol_30_36=0
    gol_37_43=0
    gol_44_51=0
    for i in umur:
        if i in range(16,23):
            gol_16_22+=1
        elif i in range(23,30):
            gol_23_29+=1
        elif i in range(30,37):
            gol_30_36+=1
        elif i in range(37,44):
            gol_37_43+=1
        elif i in range(44,52):
            gol_44_51+=1
    Umur=pd.Series(data={'16-22':gol_16_22,'23-29':gol_23_29,'30-36':gol_30_36,'37-43':gol_37_43,'44-51':gol_44_51})
    df6.append(Umur)


# In[49]:


#make pie chart df['Digital Interest'].unique()[0]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(df6[0],labels='Usia '+df6[0].index+' Tahun',autopct='%1.2f%%')
plt.title('Presentase Jumlah Pengguna Yang Tertarik Dengan\n'+idks[0]+' Berdasarkan Kelompok Usia', size=16)
plt.show()


# In[50]:


#make pie chart df['Digital Interest'].unique()[1]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(df6[1],labels='Usia '+df6[1].index+' Tahun',autopct='%1.2f%%')
plt.title('Presentase Jumlah Pengguna Yang Tertarik\nDengan '+idks[1]+' Berdasarkan Kelompok Usia', size=16)
plt.show()


# In[51]:


#make pie chart df['Digital Interest'].unique()[2]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(df6[2],labels='Usia '+df6[2].index+' Tahun',autopct='%1.2f%%')
plt.title('Presentase Jumlah Pengguna Yang Tertarik\nDengan '+idks[2]+' Berdasarkan Kelompok Usia', size=16)
plt.show()


# In[52]:


#make pie chart df['Digital Interest'].unique()[3]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(df6[3],labels='Usia '+df6[3].index+' Tahun',autopct='%1.2f%%')
plt.title('Presentase Jumlah Pengguna Yang Tertarik\nDengan '+idks[3]+' Berdasarkan Kelompok Usia', size=16)
plt.show()


# In[53]:


#make pie chart df['Digital Interest'].unique()[4]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(df6[4],labels='Usia '+df6[4].index+' Tahun',autopct='%1.2f%%')
plt.title('Presentase Jumlah Pengguna Yang Tertarik\nDengan '+idks[4]+' Berdasarkan Kelompok Usia', size=16)
plt.show()


# In[56]:


#Jumlah Pengguna Berdasarkan Jenis Kelamin Pada Setiap Digital Interest
df7=pd.crosstab(df['Digital Interest'],df['Jenis Kelamin'])
x = np.arange(len(df7.index))
width = 0.35

fig, ax = plt.subplots(figsize=(12,10))

male = ax.bar(x - width/2, df7['Laki-laki'], width, label='Laki-laki')
female = ax.bar(x + width/2, df7['Perempuan'], width, label='Perempuan')

ax.set_title('Jumlah Pengguna Berdasarkan Jenis Kelamin Pada Setiap Digital Interest', size=16)
ax.set_ylabel('Jumlah Pengguna', size=14)
ax.set_xticks(x)
ax.set_xticklabels(df7.index, size=12)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
ax.legend(fontsize=14)

fig.tight_layout()

rects1=male.patches
rects2=female.patches

labels1=[f"{i}" for i in df7['Laki-laki']]
labels2=[f"{i}" for i in df7['Perempuan']]

#Make Labels
for rect,label in zip(rects1,labels1):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha="center",va="bottom",size=16)
for rect,label in zip(rects2,labels2):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha="center",va="bottom",size=16)

plt.show()


# In[ ]:




