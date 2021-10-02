#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Comments
#print('comment diawali dengan pagar dan tidak akan dijalankan atau terbaca oleh program. seperti ini')
print('hello world')


# In[5]:


#Variables
x=5
y='Steven'
print('variabel x adalah',x)
print('variabel y adalah',y)


# In[8]:


#Data Types
a='aku ganteng'
b=17
c=17.23
d=1j
e=['aku', 'orang', 'ganteng']
f=('aku', 'orang', 'ganteng')
g=range(7)
h={'aku', 'orang', 'ganteng'}
i={'name' : 'Steven', 'age' : 20}
j=frozenset({'aku', 'orang', 'ganteng'})
k=False
l=b'Steven'
m=bytearray(5)
n=memoryview(bytes(5))
print('tipe data a adalah',type(a))
print('tipe data b adalah',type(b))
print('tipe data c adalah',type(c))
print('tipe data d adalah',type(d))
print('tipe data e adalah',type(e))
print('tipe data f adalah',type(f))
print('tipe data g adalah',type(g))
print('tipe data h adalah',type(h))
print('tipe data i adalah',type(i))
print('tipe data j adalah',type(j))
print('tipe data k adalah',type(k))
print('tipe data l adalah',type(l))
print('tipe data m adalah',type(m))
print('tipe data n adalah',type(n))
o=str(b) #salah satu contoh ubah int ke str
print('tipe data o adalah',type(o))


# In[11]:


#Numbers
x=12
y=8.43
z=3+5j
print('tipe data x adalah',type(x))
print('tipe data y adalah',type(y))
print('tipe data z adalah',type(z))
a=float(x)
b=int(y)
c=complex(x)
d=complex(d)
print(a)
print(b)
print(c)
print(d)
print('tipe data a adalah',type(a))
print('tipe data b adalah',type(b))
print('tipe data c adalah',type(c))
print('tipe data d adalah',type(d))


# In[22]:


#Casting
x=int('3')
y=float('3')
z=float('3.3')
v=str(3.9)
print(x)
print(y)
print(z)
print(v)


# In[7]:


#Strings
a='aku ganteng loh!'
print('Hello')
print("Hello")
print('''aku ganteng''')
print("""aku ganteng""")
print(len(a))
print(a[2:5])
print(a[-5:-2])
print(a.replace('o','a'))
print(a.upper()) #lower buat huruf kecil semua
print(a.split(' ')) #spasi adalah pemisahnya


# In[12]:


#Booleans
#Biasa dipake buat if conditional
print(bool('Steven'))
print(bool(14))
print(bool(0))
print(bool([]))


# In[19]:


#Operators
x=4
x+=1
x-=1
x*=2
x/=2
x%=3
x//=3
x**=3
print(x)
#untuk operator lainnya seperti '==','!=','>','<','>=','<=','&','|','not','is','is not',dll lebih banyak digunakan untuk if clause


# In[21]:


#Lists
mylist=['aku', 'adalah', 'orang', 'yang', 'paling', 'ganteng']
print(mylist)
print(mylist[1:3])
if 'orang' in mylist: #mencari elemen orang pada mylist
    print('yes')
print(len(mylist))
#append, insert, clear, remove, count, index, dll merupakan method yang dapat digunakan dalam list


# In[27]:


#Tuples
mytuple=('aku', 'adalah', 'orang', 'yang', 'paling', 'ganteng')
print(mytuple)
print(mytuple[1:3])
x=list(mytuple)
x[4]='sangat'
mytuple=tuple(x)
print(mytuple) #mengganti elemen dengan mengubah dari tuple ke list kemudian dibalikin


# In[30]:


#Sets
myset={'aku', 'adalah', 'orang', 'yang', 'paling', 'ganteng'}
print(myset)
myset.update(['kamu', 'cantik'])
print(myset)
#add, clear, pop, remove, update, dll merupakan method yang dapat digunakan dalam set


# In[33]:


#String Formatting
price=40
quantity=3
itemno=567
myorder='I want {} pieces of item number {} for {:.2f} dollars.'
txt='The price is {} dollars'
print(txt.format(price))
txt='The price is {:.2f} dollars'
print(txt.format(price))
print(myorder.format(quantity,itemno,price))


# In[34]:


#User Input
username=input('Enter username: ')
print("Orang paling ganteng adalah " + username)


# In[ ]:




