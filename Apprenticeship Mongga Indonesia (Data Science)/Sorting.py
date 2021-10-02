#!/usr/bin/env python
# coding: utf-8

# In[43]:


class Sorting:
    def Bubble(data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j]>data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
    def Insertion(data):
        for i in range(1,len(data)):
            angka=data[i]
            j=i-1
            while j>=0 and angka<data[j]:
                data[j+1]=data[j]
                j-=1
            data[j+1]=angka
    def merge(data,l,m,r):
        n1=m-l+1
        n2=r-m
        L=[0]*n1
        R=[0]*n2
        for i in range(n1):
            L[i]=data[l+i]
        for j in range(n2):
            R[j]=data[m+1+j]
        i=0;j=0;k=l
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                data[k]=L[i]
                i+=1
            else:
                data[k]=R[j]
                j+=1
            k+=1
        while i<n1:
            data[k]=L[i]
            i+=1
            k+=1
        while j<n2:
            data[k]=R[j]
            j+=1
            k+=1
    def Merge(data,l,r):
        if l<r:
            m=(l+(r-1))//2
            Sorting.Merge(data,l,m)
            Sorting.Merge(data,m+1,r)
            Sorting.merge(data,l,m,r)
    def partition(data,low,high):
        i=low-1
        pivot=data[high]
        for j in range(low,high):
            if data[j]<=pivot:
                i+=1
                data[i],data[j]=data[j],data[i]
        data[i+1],data[high]=data[high],data[i+1]
        return (i+1)
    def Quick(data,low,high):
        if len(data)==1:
            return data
        if low<high:
            pi=Sorting.partition(data,low,high)
            Sorting.Quick(data,low,pi-1)
            Sorting.Quick(data,pi+1,high)
    def Max(data):
        Sorting.Bubble(data)
        print('Nilai maksimum adalah '+str(data[-1]))
    def Min(data):
        Sorting.Bubble(data)
        print('Nilai minimum adalah '+str(data[0]))
    def Median(data):
        Sorting.Bubble(data)
        n=len(data)
        if n%2==1:
            n=n-1
            print('Nilai median adalah '+str(data[int(n/2)]))
        else:
            x=(data[int(n/2)]+data[int(n/2)-1])/2
            print('Nilai median adalah '+str(int(x)))

