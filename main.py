import tkinter
from tkinter import *
import os
import time

screen = Tk()
screen.title('CS530 Smart Mirror')
startUpText = Label(screen, font = ('Times', 40), bg='black', fg='white')
screen.configure(background='black')
screen.overrideredirect(True) #can't close window by regular means, get rids of window bar

startUpText.config(text='Smart Mirror')
startUpText.pack(side=LEFT, padx= 120, pady=80)
pRight = int(screen.winfo_screenwidth()/3 - screen.winfo_reqwidth()/2) # Halves screen width & height
pDown = int(screen.winfo_screenheight()/2 - screen.winfo_reqheight()/2) # Halves screen width & height
screen.geometry("+{}+{}".format(pRight, pDown)) # Positions the window in the center of the page.

def main_screen() :
    screen.destroy()
    def timeHour() :
        string = time.strftime("%H") #how to make hour regular and not military?
        hour.config(text = string)
        hour.after(200, timeHour)
 
    def timeElse() :
        string = time.strftime(":%M:%S %p") #%p?
        other.config(text = string)
        other.after(200, timeElse)

    def greetings():
        greet = "Hi!"
        greeting.config(text=greet)


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
screen.after(3000, main_screen)
mainloop()

#do we need a close or destroy eventually??
