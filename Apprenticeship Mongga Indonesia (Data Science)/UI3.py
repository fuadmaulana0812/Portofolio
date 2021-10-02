#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PySimpleGUI as sg
import os


# In[4]:


kolom1=[
    [
        sg.Text("Image Folder "),
        sg.In(size=(20,1), key="-INPUT-"),
        sg.FolderBrowse(key="-BROWSE-")
    ],
    [
        sg.Listbox(
        values=[], size=(40,20), key="-LIST-"
        )
    ]
]

kolom2=[
    [
        sg.Text("choose an Image from list from left")
    ],
    [
        sg.Text(size=(20,1), key="-TEXT2-")
    ],
    [
        sg.Image(key="-IMG-")
    ]
]

layout=[
    [
        sg.Column(kolom1),
        sg.VSeparator(),
        sg.Column(kolom2),
        sg.Submit()
    ]
]

window=sg.Window("UI MAINAN",layout)

while True:
    event,values=window.read()
    if event == "Exit" or event==sg.WIN_CLOSED:
        break
    if event=="-BROWSE-":
        folder=values["-BROWSE-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        fnames=list()
        for f in file_list:
            filetotal=os.path.join(folder,f)
            if os.path.isfile(filetotal) and f.lower().endswith((".jpg",".png")):
                fnames.append(f)
        
        window["-LIST-"].update(fnames)
                                        
    if event=="-LIST-":
        try:
            filename=os.path.join(
                values["-BROWSE-"],values["-LIST-"][0]
            )
            window["-TEXT2"].update(filename)
            window["-IMG-"].update(filename=filename)
        except:
            pass
window.close()


# In[ ]:




