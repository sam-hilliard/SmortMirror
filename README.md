# SmortMirror
A simple smart mirror implemented using python and tkinter made to run on a raspberry pi

## About
This software is designed to run a GUI on any platform with python installed, allowing
for as high accessibility as possible. The idea behind this is to rid the barrier
to entry of more expensive IOT devices (specifically smart mirrors) by making our code
free and open source. All users would need to build there own smart mirror then is to 
buy a monitor, raspberry pi or equivalent inexpensive computer, and one-way glass, which 
would add up to a much lower cost than the leading smart mirror brands.

## Structure
There are two main parts to this program:
    1. Frontend/GUI
        - Displays information to user along with a greeting.
    2. Backend
        - Makes API requests and scrapes webpages to deliver information to be used in the GUI

The Backend, while working independently of the GUI, is used by the GUI to deliver specified
information that will then be displayed on screen. This seperation not only allows for ease
of development, but also allows for customizability as the user can pick and choose what should
be displayed as well as choose to add their own.

## Usage
Since the code is written solely in python, the user can run this project by running `main.py`
with python

`python main.py`

Or an executable can be made from the main.py for a specified OS

The user also needs an api key from Weather Bit, which can be generated for free or using the paid option from
the Rapid API site.

Once generated, a `.env` file would then need to be placed in the root project folder with the contents:
`API_KEY = "<API key>"`

## Requirements
- Beautiful Soup 4
- Requests
- python_dotenv

### Installation Instructions
- `pip install bs4 requests python_dotenv`