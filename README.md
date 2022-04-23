# SmortMirror
A simple smart mirror implemented using python and tkinter made to run on a raspberry pi

## About
This software is designed to run a GUI on any platform with python installed, allowing
for as high accessibility as possible. The idea behind this is to rid the barrier
to entry of more expensive IOT devices (specifically smart mirrors) by making our code
free and open source. All users would need to build there own smart mirror then is to 
buy a monitor, raspberry pi or equivalent inexpensive computer, and one-way glass, which 
would add up to a much lower cost than the leading smart mirror brands.

## Usage
Since the code is written solely in python, the user can run this project by running `main.py`
with python

`python main.py`

Or an executable can be made from the main.py for a specified OS

The user also needs an api key from Weather Bit, which can be generated for free or using the paid option from
the Rapid API site.

Once generated, a `.env` file would then need to be placed in the root project folder with the contents:
`API_KEY = "<API key>"`