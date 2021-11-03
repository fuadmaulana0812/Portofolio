#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Input data
open_data=pd.read_csv("D:\Karir\Portofolio\Test Vidio\Data_Vidio.csv", error_bad_lines=False, na_values=["null"])
open_data.info()


# In[6]:


#To find the most used platforms
a=open_data['platform'].value_counts()
print('the most used platform is',a.index[0],'with total',a[0],'times')


# In[55]:


#Just need web-mobile data with column of 'os_name' and 'browser_name'
web_mobile=open_data[(open_data['platform']=='web-mobile')]
columns=['os_name','browser_name']
web_mobile=web_mobile[columns]
web_mobile.info()
web_mobile.head()


# In[56]:


#make horizontal bar chart for os_name
os_name=web_mobile['os_name'].value_counts()

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(os_name.index, os_name, align='center')
ax.set_yticklabels(os_name.index)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('OS Name')
ax.set_title('List The Number of OS Names on Web Mobile', size=16)

rects=ax.patches

labels=[f"{i}" for i in os_name]

#Make Labels
for rect,label in zip(rects,labels):
    width=rect.get_width()
    ax.text(width,rect.get_y()+rect.get_height()/2,label,ha='left',va='center')

plt.show()


# In[58]:


print("It can be seen that significantly more users use Android than other OS")


# In[53]:


#Make horizontal bar chart for browser_name
browser_name=web_mobile['browser_name'].value_counts()

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(12,8))

ax.barh(browser_name.index, browser_name, align='center', height=0.5)
ax.set_yticklabels(browser_name.index)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Browser Name')
ax.set_title('List The Number of Browser Names on Web Mobile', size=16)

rects=ax.patches

labels=[f"{i}" for i in browser_name]

#Make Labels
for rect,label in zip(rects,labels):
    width=rect.get_width()
    ax.text(width,rect.get_y()+rect.get_height()/2,label,ha='left',va='center')

plt.show()


# In[57]:


print("It can be seen that many users use browsers from mobile apps, such as Chrome Mobile, UC Browser, Opera Mobile, Mobile Safari, MiuiBrowser, and others. The most used browser is Chrome Mobile with 20385 times")


# In[ ]:




