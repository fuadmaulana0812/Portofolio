#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PySimpleGUI as sg
import cv2


# In[2]:


kolom1=[
    [sg.In(size=(40,1),key="-INPUT-")],
    [sg.Button("Tombol Ganti Text", key="-TOMBOL1-")],
    [sg.Submit("Submit", key="-SUBMIT-")]
]

kolom2=[
    [sg.Text("Text ini bakal berubah",key="-TEXT-")]
]

layout=[
    [
        sg.Column(kolom1),
        sg.VSeparator(),
        sg.Column(kolom2)
    ]
]

window = sg.Window("Tes User Interface",layout)

while True:
    event, values = window.read()
    if event=="Exit" or event==sg.WIN_CLOSED:
        break
    if event=="-TOMBOL1-":
        text = values["-INPUT-"]
        window["-TEXT-"].update(text)

window.close()      

