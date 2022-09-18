#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import numpy as np
import cv2
from PIL import Image, ImageTk
import pandas as pd


# In[2]:


x=tk.Tk()
x.title("Colour detector")
x.resizable(False,False)
x.geometry('500x500+140+80')
x.config(bg='#2c9158')
toptitle = Label(x,text="What colour is THAT!? ",bg = "white",fg='blue',font=('Times new roman',24,'bold'),relief=GROOVE,bd=10).pack(fill=X,side=TOP)
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# In[3]:



def show_frame():
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1288)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,728)
    while True:
        _,frame=cap.read()
        hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        height,width, _=frame.shape
    
        cx=int(width/2)
        cy=int(height/2)
    
        pixel_center = hsv_frame[cy,cx]
        hue_value=pixel_center[0]
    
        color="undefined"
        if hue_value<5:
            color="RED"
        elif hue_value<22:
            color="ORANGE"
        elif hue_value<33:
            color="YELLOW"
        elif hue_value<78:
            color = "GREEN"
        elif hue_value<131:
            color="BLUE"
        elif hue_value<178:
            color="VOILET"
        
        else:
            color="RED"
        pixel_center_bgr = hsv_frame[cy,cx]
        b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
        cv2.putText(frame,color,(10,78),0,1.5,(b,g,r),2)
        cv2.circle(frame,(cx,cy),5,(25,25,25),3)
    
        cv2.imshow("Frame",frame)
        key=cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def exit():
    x.destroy()
det_btn = Button(x, text='       Start       ', font=('Lucida Calligraphy', 20),command=show_frame, bg='orange', fg='red',bd=9)
det_btn.place(relx=0.32,rely=0.35)

exit_btn = Button(x, text='     Exit          ', font=('Lucida Calligraphy', 20),command=exit,bg='orange', fg='red',bd=9)
exit_btn.place(relx=0.32,rely=0.54)


x.mainloop()


# In[ ]:




