#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


df=pd.read_csv("D:/Karir/Portofolio/Test Vidio/Data_Vidio.csv", error_bad_lines=False)
df.info()


# In[16]:


#DATA CLEANING


# In[17]:


#Dropping columns in a DataFrame
df.drop(["city"],inplace=True,axis=1)
df.info()


# In[18]:


#Changing index with unique column
df.set_index("hash_content_id", inplace=True)
df.head()


# In[19]:


#Dropping NaN values
df1=df[['category_name','completed']]
df1.dropna()
df1.info()


# In[20]:


#Data Visualization


# In[21]:


#Bar Chart
df2=pd.crosstab(df1['category_name'],df1['completed'])
x = np.arange(len(df2.index))
width = 0.35

fig, ax = plt.subplots(figsize=(12,7))

completed = ax.bar(x - width/2, df2[True], width, label='Completed')
not_completed = ax.bar(x + width/2, df2[False], width, label='Not Completed')

ax.set_title('Number of Video Category Based on Completed Video', size=16)
ax.set_ylabel('Number of Video', size=14)
ax.set_xticks(x)
ax.set_xticklabels(df2.index, size=12)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
ax.legend(fontsize=14)

fig.tight_layout()

rects1=completed.patches
rects2=not_completed.patches

labels1=[f"{i}" for i in df2[True]]
labels2=[f"{i}" for i in df2[False]]

#Make Labels
for rect,label in zip(rects1,labels1):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha="center",va="bottom")
for rect,label in zip(rects2,labels2):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha="center",va="bottom")

plt.show()


# In[22]:


df3=df['platform'].value_counts()

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(df3.index, df3, align='center')
ax.set_yticklabels(df3.index)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Platform')
ax.set_title('Number of Platform', size=16)

rects=ax.patches

labels=[f"{i}" for i in df3]

#Make Labels
for rect,label in zip(rects,labels):
    width=rect.get_width()
    ax.text(width,rect.get_y()+rect.get_height()/2,label,ha='left',va='center')

plt.show()


# In[23]:


df4=df['has_ad'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(df4,labels=['Has Ad','Has Not Ad'],autopct='%1.2f%%')
plt.title('Percentage of Video has Ad', size=16)
plt.show()


# In[24]:


df.info()


# In[25]:


df.drop(['hash_watcher_id','hash_visit_id','hash_play_id','hash_film_id','hash_event_id','play_time','end_time','referrer','average_bitrate','bitrate_range','total_bytes','buffer_duration','utm_source','utm_medium','utm_campaign','flash_version','os_version','browser_version','app_version','title','film_title','season_name'], inplace=True, axis=1)
df.info()


# In[39]:


df.to_csv('data_tableau.csv')


# In[ ]:




