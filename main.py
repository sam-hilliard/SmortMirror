import tkinter
from tkinter import *
import os
import time

def greetings():
    greet = "Hi!"
    greeting.config(text=greet)

def timeHour() :
    string = time.strftime("%H") #how to make hour regular and not military?
    hour.config(text = string)
    hour.after(200, timeHour)
 
def timeElse() :
    string = time.strftime(":%M:%S %p") #%p?
    other.config(text = string)
    other.after(200, timeElse)

root = Tk()
root.title('Mirror')
#root.configure(background='black')

clock = Label(root) #clock widget
clock.pack(anchor=NW, fill=X, padx=45)
clock.configure(background='black')
hour = Label(root, font = ('Times', 130), bg='black', fg='white') #hour section
hour.pack(in_=clock, side=LEFT)
other = Label(root, font = ('Times', 70), bg='black', fg='white') #minutes, miliseconds, and am/pm
other.pack(in_=clock, side=LEFT, anchor = N, ipady=15)


greeting = Label(root, font = ('Times', 300), bg='black', fg='white')
greeting.pack(anchor=CENTER, fill=X)
#greeting.place(relx=.5, rely=.5, anchor=CENTER)

greetings()
timeHour()
timeElse()

root.attributes("-fullscreen", True)
root.configure(background='black')
mainloop()
