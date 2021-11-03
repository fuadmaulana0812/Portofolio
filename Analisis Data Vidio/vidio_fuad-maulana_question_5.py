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


# In[4]:


#To find range of date
tempp1=open_data['play_time']
tempp2=open_data['end_time']
play_year=list()
play_month=list()
play_day=list()
end_year=list()
end_month=list()
end_day=list()
for i in range(len(tempp1)):
    play_year.append(tempp1.iloc[i][:4])
    play_month.append(tempp1.iloc[i][5:7])
    play_day.append(tempp1.iloc[i][8:10])
    end_year.append(tempp2.iloc[i][:4])
    end_month.append(tempp2.iloc[i][5:7])
    end_day.append(tempp2.iloc[i][8:10])


# In[23]:


#To find range of year
print('range of year is',min(play_year),'-',max(end_year))

#To find range of month
#If range of year is 0
print('range of month is', min(play_month),'-',max(end_month))

#To find range of day
#If range of year is 0 and range of month is 0
print('range of day is', min(play_day),'-',max(end_day))

#Find number of days
number_of_days=int(max(end_day))-int(min(play_day))+1
number_of_days


# In[31]:


df=open_data[['hash_watcher_id','play_duration']]
watcher_id=df.groupby('hash_watcher_id')['play_duration'].sum()
watcher_id=watcher_id.sort_values(ascending=False)


# In[28]:


#To find play duration per day for each watcher_id
watcher_play_per_day=watcher_id/number_of_days
watcher_play_per_day


# In[30]:


#Top 10 Visitor Based on Play Duration per Day
top10=pd.DataFrame(watcher_play_per_day[:10])
top10.rename(columns={'play_duration':'play_duration_per_day'})


# In[ ]:




