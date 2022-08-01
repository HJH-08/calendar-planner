# Importing The Essential Libraries
from tkinter import *
from tkcalendar import Calendar
 
# Create The Gui Object
tk = Tk()
 
# Set the geometry of the GUI Interface
tk.geometry("700x700")
 
# Add the Calendar module
cal = Calendar(
tk, selectmode = 'day', date_pattern = 'dd-mm-yyyy', 
background = '#00008B', foreground = 'white',
headersbackground = '#A7C7E7', headersforeground = 'black',
weekendbackground = '#f6f6f6', othermonthbackground = '#ececec',
othermonthwebackground = '#e2e2e2' )
 
cal.pack(pady = 100, fill="both", expand=True)
 
# Function to grab the selected date
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Adding the Button and Label
Button(tk, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(tk, text = "")
date.pack(pady = 20)
 
# Execute Tkinter
tk.mainloop()