from tkinter import *
from tkinter.ttk import*
from time import strftime #importing shit

root = Tk() #setting root as tk
root.title("Clock") #app title lmao
def time():  #TIME
    string = strftime('%H:%M:%S %p') #time format
    label.config(text=string) #how it should be displayed
    label.after(1000, time) #for making sure the time changes


label = Label(root, font=("ds-digital", 80), background = "black", foreground="red") #actual features of the app
label.pack(anchor='center') #center placement

time() #calling time
mainloop() #looping program
