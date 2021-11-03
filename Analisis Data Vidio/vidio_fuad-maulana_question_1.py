#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Package
import pandas as pd #for data processing
import numpy as np #for operation mathematics in array
import matplotlib.pyplot as plt #for make plot data
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Input data
open_data=pd.read_csv("D:\Karir\Portofolio\Test Vidio\Data_Vidio.csv", na_values=["null"], error_bad_lines=False)
open_data.info()


# In[3]:


#VIDEO CATEGORY ANALYSIS BASED ON FINISHED VIDEO


# In[4]:


#For this analysis, just need 2 column 'complete' and 'category_name'
df=open_data[['completed', 'category_name']]
df=df.dropna() #Delete NaN values 
df.info()


# In[5]:


#Find number of 'True' and 'False' in 'completed' column
Completed_data=df['completed'].value_counts(sort='False')
Completed_data


# In[6]:


#Make pie chart to find Percentage of Video is Completed
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(Completed_data,labels=['Not Completed','Completed'],autopct='%1.2f%%')
plt.title('Percentage of Video is Completed', size=16)
plt.show()


# In[7]:


#Find number of video each category
Category_data=df['category_name'].value_counts(sort=False)
Category_data


# In[8]:


#Make horizontal bar chart about video category
Category=df['category_name'].value_counts()

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(Category.index, Category, align='center')
ax.set_yticklabels(Category.index)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Video Category')
ax.set_title('Number of Video Category', size=16)

rects=ax.patches

labels=[f"{i}" for i in Category]

#Make Labels
for rect,label in zip(rects,labels):
    width=rect.get_width()
    ax.text(width,rect.get_y()+rect.get_height()/2,label,ha='left',va='center')

plt.show()


# In[9]:


#To find correlation about value of 'completed' and 'category_name' column
df1=pd.crosstab(df['category_name'],df['completed'])
corr=df1/df1.sum()
corr


# In[12]:


print('It is known that the entertainment category is most watched but not completed with a percentage of 34.35% of the total content not completed.\nWhile the news category is the most watched to the end with a percentage of 44.31% of the total content completed.')


# In[13]:


#Make plot bar for data 'completed' and 'category_name'
x = np.arange(len(df1.index))
width = 0.35

fig, ax = plt.subplots(figsize=(12,7))

completed = ax.bar(x - width/2, df1[True], width, label='Completed')
not_completed = ax.bar(x + width/2, df1[False], width, label='Not Completed')

ax.set_title('Number of Video Category Based on Completed Video', size=16)
ax.set_ylabel('Number of Video', size=14)
ax.set_xticks(x)
ax.set_xticklabels(df1.index, size=12)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
ax.legend(fontsize=14)

fig.tight_layout()

rects1=completed.patches
rects2=not_completed.patches

labels1=[f"{i}" for i in df1[True]]
labels2=[f"{i}" for i in df1[False]]

#Make Labels
for rect,label in zip(rects1,labels1):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha="center",va="bottom")
for rect,label in zip(rects2,labels2):
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha="center",va="bottom")

plt.show()


# In[14]:


#Take top 4 Video Category
Top1=df[(df['category_name']==Category.index[0])] #Entertainment
Top2=df[(df['category_name']==Category.index[1])] #News
Top3=df[(df['category_name']==Category.index[2])] #Sports
Top4=df[(df['category_name']==Category.index[3])] #Movies

#Count values completed and not completed
Top1=Top1['completed'].value_counts(sort=False)
Top2=Top2['completed'].value_counts(sort=False)
Top3=Top3['completed'].value_counts(sort=False)
Top4=Top4['completed'].value_counts(sort=False)


# In[15]:


plt.style.use('ggplot')

fig, ax = plt.subplots(ncols=2, nrows=2)
fig.suptitle('Percentage of Top 4 Video Category is Completed or Not', size=16)

ax[0,0].axis('equal')
ax[0,0].pie(Top1,labels=['Not Completed','Completed'],autopct='%1.2f%%')
ax[0,0].set_title(Category.index[0],size=12)

ax[0,1].axis('equal')
ax[0,1].pie(Top2,labels=['Not Completed','Completed'],autopct='%1.2f%%')
ax[0,1].set_title(Category.index[1],size=12)

ax[1,0].axis('equal')
ax[1,0].pie(Top3,labels=['Not Completed','Completed'],autopct='%1.2f%%')
ax[1,0].set_title(Category.index[2],size=12)

ax[1,1].axis('equal')
ax[1,1].pie(Top4,labels=['Not Completed','Completed'],autopct='%1.2f%%')
ax[1,1].set_title(Category.index[3],size=12)

plt.show()


# In[17]:


print("It is known that the entertainment and movies category has a percentage of more than 80% of unfinished videos.\nWhile the news category has a percentage of 35% of the completed videos.")
print("Customers have a high interest in these 4 categories. But many videos aren't watched till the end.\nThis is possible due to several factors. one factor is the content of the video.\nThe customers is curious about the video, but chooses not to watch the video until it's finished because the content of the video is not interesting.\nOf the 4 categories, the new category has the largest percentage of videos watched to completion by customers")


# In[ ]:




