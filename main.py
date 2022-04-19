import tkinter
from tkinter import *
import os

def greetings():
    greet = "Hi!"
    greeting.config(text=greet)


root = Tk()
root.title('Mirror')
#root.configure(background='black')
    
greeting = Label(root, font = ('Times', 300), bg='black', fg='white')
greeting.pack(anchor=CENTER, fill=X)
#greeting.place(relx=.5, rely=.5, anchor=CENTER)

greetings()

root.attributes("-fullscreen", True)
root.configure(background='black')
mainloop()
