#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Dictionaries
mydict={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(mydict)
print(mydict.get('model'))
mydict['year']=2018
for i in mydict:
    print(i)
    print(mydict[i])
#keys adalah kata kunci, values adalah isi dari kata kunci tersebut, items berguna untuk membaca keys dan values
mydict['color']='red' #add items
print(mydict)
print(mydict.popitem()) #hapus item terakhir
mydict.pop('model') #remove items
print(mydict)
del mydict['year'] #hapus juga
print(mydict)


# In[38]:


#If...Else
b=[12,13,14,15,16,17,18]
a=[3,14,20,12]
for i in range(len(a)):
    if a[i]>b[0] and a[i]<b[6]:
        print(a[i], 'berada pada interval',b[0], 'sampai', b[6])
    elif a[i]==b[6] or a[i]==b[0]:
        print(a[i], 'merupakan batas interval',b[0],'sampai',b[6])
    else:
        print(a[i], 'berada diluar interval',b[0],'sampai',b[6])


# In[39]:


#While Loops
i=0
while i<10:
    i+=1
    if i==3:
        continue
    elif i==6:
        break
    print(i)


# In[42]:


#For Loops
a=[1,2,3]
b=[2,3,4]
for i in a:
    for j in b:
        if i==j:
            continue
        print(i,j)


# In[ ]:




