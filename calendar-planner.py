# Importing The Essential Libraries
from tkinter import *
from tkcalendar import Calendar, DateEntry
 
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
othermonthwebackground = '#e2e2e2', cursor='hand1' )
 
#cal.pack(pady = 100, fill="both", expand=True)
cal.grid(row=0, column=0, columnspan=2, sticky='WENS', pady = 50)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)
tk.rowconfigure(0, weight=1)
tk.rowconfigure(1, weight=1)
 
# Function to grab the selected date
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Adding the Button and Label
Button(tk, text = "Get Date", command = grad_date).grid(row=1, column=0)

def add_task():
    def create_another_task():
        top.destroy()
        add_task()

    def confirm_task():
        text = user_task_input.get().capitalize() + ' on ' + cal.get_date().strftime("%m/%d/%Y") + ' added to calendar'
        print(text)
        confirmed_task_label = Label(top, text=text, wraplength=300)
        confirmed_task_label.pack(pady=10)

        back_to_calendar_button = Button(top, text="Back to Calendar", command=top.destroy)
        back_to_calendar_button.pack(padx=10, side='left')

        enter_another_task_button = Button(top, text="Create Another Task", command=create_another_task)
        enter_another_task_button.pack(padx=10, side='right')

    top = Toplevel(tk)
    top.geometry('400x400')

    user_input_label = Label(top, text='Enter the task and its date: ')
    user_input_label.pack(padx=10, pady=20)

    user_task_input = Entry(top, width=30)
    user_task_input.pack(pady=20)

    cal = DateEntry(top, width=30, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

    confirm_button = Button(top, text="Confirm", command=confirm_task)
    confirm_button.pack(pady=10)



Button(tk, text="Add Task", command=add_task).grid(row=1, column=1)
 
date = Label(tk, text = "")
date.grid(row = 100, column = 0)
 
# Execute Tkinter
tk.mainloop()