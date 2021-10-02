#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
    def __init__(self,name,age,hobby,national):
        self.name=name
        self.age=age
        self.hobby=hobby
        self.national=national
    
    def nama(self):
        print("Namanya adalah " + self.name)
        
    def umur(self):
        print(self.name + ' berumur ' + str(self.age) + 'tahun')
        
    def hobi(self):
        print(self.name+' memiliki hobi '+self.hobby)
        
    def negara(self):
        print(self.name+' berkewarganegaraan '+self.national)

