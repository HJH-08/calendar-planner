# Importing The Essential Libraries
from tkinter import *
from typing import List
from tkcalendar import Calendar, DateEntry
from datetime import datetime

#ADD TASK PAGE

def add_task():
    def confirm_task():
        no_task_label.pack_forget()
        if user_task_input_entry.get() == '':
            no_task_label.pack()
            return
        text = user_task_input_entry.get() + ' on ' + cal.get_date().strftime("%d/%m/%Y") + ' added to calendar'
        confirmed_task_label.config(text=text)
        confirmed_task_label.pack(pady=10)

        main_cal.calevent_create(cal.get_date(), user_task_input_entry.get(), 'reminder')
        main_cal.tag_config('reminder', background='red', foreground='yellow')
        if cal.get_date() in task_dict:
            task_dict[cal.get_date()].append(user_task_input_entry.get())
        else:
            task_dict[cal.get_date()] = [user_task_input_entry.get()]

        back_to_calendar_button.pack(padx=10, side='left')
        enter_another_task_button.pack(padx=10, side='right')

    def create_another_task():
        user_task_input_entry.delete(0, END)
        confirmed_task_label.config(text='')
        back_to_calendar_button.pack_forget()
        enter_another_task_button.pack_forget()

    top = Toplevel(tk)
    top.geometry('400x400')

    date_from_main = main_cal.get_date()
    user_input_label = Label(top, text='Enter the task and its date: ')
    user_input_label.pack(padx=10, pady=20)

    user_task_input_entry = Entry(top, width=30)
    user_task_input_entry.pack(pady=20)

    cal = DateEntry(top, width=30, background='darkblue',
                    foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
    cal.set_date(date_from_main)
    cal.pack(padx=10, pady=10)  

    confirm_button = Button(top, text="Confirm", command=confirm_task)
    confirm_button.pack(pady=10)
    no_task_label = Label(top, text="Input some task please!")

    confirmed_task_label = Label(top, wraplength=300)
    back_to_calendar_button = Button(top, text="Back to Calendar", command=top.destroy)
    enter_another_task_button = Button(top, text="Create Another Task", command=create_another_task)

def show_task_list():
    top = Toplevel(tk)
    top.geometry('400x400')
    task_list_label = Label(top, text="Your Task List", anchor=CENTER, font=("Helvetica 18 underline"))
    task_list_label.pack(pady = 20)
    task_listbox = Listbox(top)

    task_dict_sorted = {}
    for date in sorted(task_dict):
        task_dict_sorted[date] = task_dict[date]
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            task_listbox.insert(END, f'{day.strftime("%d/%m/%Y")}: {task}')

    task_listbox.pack(pady=15)
    


def delete_tasks():
    pass;

# Create The Gui Object
tk = Tk()
tk.update_idletasks()
 
# Set the geometry of the GUI Interface
tk.geometry("700x700")
 
# Add the Calendar module
main_cal = Calendar(
tk, selectmode = 'day', date_pattern = 'dd-mm-yyyy', 
background = '#00008B', foreground = 'white',
headersbackground = '#A7C7E7', headersforeground = 'black',
weekendbackground = '#f6f6f6', othermonthbackground = '#ececec',
othermonthwebackground = '#e2e2e2', cursor='hand1' )
 
#cal.pack(pady = 100, fill="both", expand=True)
main_cal.grid(row=0, column=0, columnspan=2, sticky='WENS', pady = 50)
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=1)
tk.rowconfigure(0, weight=1)
tk.rowconfigure(1, weight=1)
 
# Function to grab the selected date
def grad_date():
    date.config(text = "Selected Date is: " + main_cal.get_date())
 
# Adding the Button and Label
Button(tk, text = "Get Date", command = grad_date).grid(row=1, column=0)

Button(tk, text="Add Task", command=add_task).grid(row=1, column=1)
task_dict = {}

Button(tk, text="Task List", command=show_task_list).grid(row=2, column=0)

Button(tk, text="Delete Tasks", command=delete_tasks).grid(row=2, column=1)
 
date = Label(tk, text = "")
date.grid(row = 100, column = 0)
 
# Execute Tkinter
tk.mainloop()