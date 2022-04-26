from tkinter import *
import time
from fetch_top_headlines import TopHeadlinesAPI
from fetch_weather_data import WeatherAPI

#SPLASH SCREEN STARTS
screen = Tk()
screen.title('CS530 Smart Mirror')
startUpText = Label(screen, font = ('Times', 40), bg='black', fg='white')
screen.configure(background='black')
screen.overrideredirect(True)    #can't close splash window by regular means, get rids of window bar

startUpText.config(text='Smart Mirror')
startUpText.pack(side=LEFT, padx= 120, pady=80)
width = int(screen.winfo_screenwidth()/3 - screen.winfo_reqwidth()/2) # Halves screen width & height
height = int(screen.winfo_screenheight()/2 - screen.winfo_reqheight()/2) # Halves screen width & height
screen.geometry("+{}+{}".format(width, height)) # Positions the window in the center of the page.
#SPLASH SCREEN ENDS

# initializing APIs
weatherAPI = WeatherAPI("San Diego", "CA", "US")
topHeadlinesAPI = TopHeadlinesAPI(3)

temperature, cur_weather = weatherAPI.fetch_cur()

def main_screen() :
    screen.destroy() #destroys splash screen
    
    def timeHour() : #gets hour place for clock
        string = time.strftime("%H") 
        hour.config(text = string)
        hour.after(200, timeHour)
 
    def timeElse() :
        string = time.strftime(":%M:%S %p") #gets minutes, second, and meridian places for clock
        other.config(text = string)
        other.after(200, timeElse)

    def greetings(): #creates customizable greeting
        greet = "Hi!"
        greeting.config(text=greet)

    def display_temperature(): #pulls temperature from web based api
        degree_sign = u"\N{DEGREE SIGN}"
        string = str(temperature) + degree_sign + "F"
        temperature_label.config(text=string)
        temperature_label.after(200, display_temperature)

    def display_descript(): #pulls weatehr description from web based api
        string = cur_weather['description'] + " "
        weather_label.config(text=string)
        weather_label.after(200, display_descript)

    def display_headlines(): #pulls headlines from web based api and displays it
        article = Label(root)
        article.pack(anchor=SW, fill=X)
        article.configure(background='black')
        heading = Label(root, text="TODAY'S TOP STORIES:", font=('Times', 50), bg='black', fg='white')
        heading.pack(in_=article, side=LEFT, padx=5, pady=5)

        headlines = topHeadlinesAPI.fetch_headlines()
        string = headlines[0] + "\n" + headlines[1] + "\n" + headlines[2] + "\n"
        label = Label(root, text=string, font=('Times', 25), justify=LEFT, bg='black', fg='white')
        label.pack(side=BOTTOM, anchor=SW, padx=5, pady=5)
        label.after(200, display_headlines)

    def Close():
        root.destroy()

    root = Tk() #main window = mirror screen
    root.title('Mirror')
    root.configure(background='black')
    root.overrideredirect(True)
    w = root.winfo_screenwidth()               
    h = root.winfo_screenheight()               
    root.geometry("%dx%d" % (w, h))

    top = Label(root) #top container for clock and weather
    top.pack(anchor=NW, fill=X, padx=15)
    top.configure(background='black')
    hour = Label(root, font = ('Times', 130), bg='black', fg='white') #diplays hour section
    hour.pack(in_=top, side=LEFT)
    other = Label(root, font = ('Times', 70), bg='black', fg='white') #displays minutes, miliseconds, and am/pm
    other.pack(in_=top, side=LEFT, anchor = N, ipady=15)
    temperature_label = Label(root, font = ('Times', 100), bg='black', fg='white') #displays tempterature
    temperature_label.pack(in_=top, side=RIGHT)
    weather_label = Label(root, font = ('Times', 50), bg='black', fg='white') #displays weather description
    weather_label.pack(in_=top, side=RIGHT, anchor = N, ipady=15)

    greeting = Label(root, font = ('Times', 300), bg='black', fg='white') #displays customizable greeting
    greeting.pack(anchor=CENTER, fill=X, padx = 130, pady=130)
    
    exit_button = Button(root, bg='black', fg='black', height=25, width=20,
                         highlightcolor='black', activebackground='black', activeforeground='black',
                         borderwidth=0, highlightthickness=0, command=Close)  #discreet button to close easier
    exit_button.pack(anchor= SE, side=RIGHT, padx = 25, pady = 25)

    greetings()
    timeHour()
    timeElse()
    display_temperature()
    display_descript()
    display_headlines()

screen.after(3000, main_screen)
mainloop()
