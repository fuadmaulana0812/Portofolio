#!/usr/bin/env python
# coding: utf-8

# In[2]:


f=open('myfile.txt', 'w')
f.write('untuk membuat file bisa menggunakan x atau w. w berlaku jika file nya belum ada')
f.close()
f=open('myfile.txt', 'r')
print(f.read())


# In[ ]:


import os
if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('file nya kaga ada woi')

