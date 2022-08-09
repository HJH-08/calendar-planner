# Importing The Essential Libraries
from ast import If
from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import datetime
from tkinter import font

#ADD TASK PAGE
def add_back_to_calendar_button(master):
    back_to_calendar_button = Button(master, text="Back to Calendar", command=master.destroy)
    back_to_calendar_button.pack()

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def add_task():
    def confirm_task():
        no_task_label.pack_forget()
        if user_task_input_entry.get() == '':
            no_task_label.pack()
            return
        text = user_task_input_entry.get() + ' on ' + cal.get_date().strftime("%d/%m/%Y") + ' added to calendar'
        confirmed_task_label.config(text=text)
        confirmed_task_label.pack(pady=10)

        main_cal.tag_config('reminder', background='red', foreground='yellow')
        if cal.get_date() in task_dict:
            if user_task_input_entry.get() not in task_dict[cal.get_date()]:
                task_dict[cal.get_date()].append(user_task_input_entry.get())
                main_cal.calevent_create(cal.get_date(), user_task_input_entry.get(), 'reminder')

        else:
            task_dict[cal.get_date()] = [user_task_input_entry.get()]
            main_cal.calevent_create(cal.get_date(), user_task_input_entry.get(), 'reminder')

        global task_dict_sorted
        task_dict_sorted = {}
        for date in sorted(task_dict):
            task_dict_sorted[date] = task_dict[date]

        back_to_calendar_button.pack_forget()
        back_to_calendar_button.pack(padx=10, side='left')
        enter_another_task_button.pack(padx=10, side='right')

    def create_another_task():
        user_task_input_entry.delete(0, END)
        confirmed_task_label.config(text='')
        back_to_calendar_button.pack_forget()
        back_to_calendar_button.pack()
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
    back_to_calendar_button.pack()
    enter_another_task_button = Button(top, text="Create Another Task", command=create_another_task)

def show_task_list():
    top = Toplevel(tk)
    top.geometry('400x400')

    def items_selected(event):
        task_info_label.config(text=task_listbox.get(ANCHOR))
        task_info_label.pack()


    tasks_list_frame = Frame(top)
    tasks_list_scrollbar = Scrollbar(tasks_list_frame, orient=VERTICAL)
    task_list_label = Label(top, text="Your Task List", anchor=CENTER, font=("Helvetica 18 underline"))
    task_list_label.pack(pady = 20)

    global task_listbox
    task_listbox = Listbox(tasks_list_frame, width=40, font=big_font, yscrollcommand=tasks_list_scrollbar.set)
    tasks_list_scrollbar.config(command=task_listbox.yview)
    task_listbox.bind('<<ListboxSelect>>', items_selected)

    task_info_label = Label(top, text='')

    task_dict_sorted = {}
    for date in sorted(task_dict):
        task_dict_sorted[date] = task_dict[date]
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' not in task:
                task_listbox.insert(END, f'{day.strftime("%d/%m/%Y")}: {task}')
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' in task:
                completed_task = day.strftime("%d/%m/%Y") + ':' + task
                task_listbox.insert(END, strike(completed_task))
    
    tasks_list_scrollbar.pack(side=RIGHT, fill=Y)
    tasks_list_frame.pack()
    task_listbox.pack(pady=15)
    add_back_to_calendar_button(top)
    


def delete_tasks_window():
    
    def delete_task():
        if task_listbox.get(ANCHOR):
            task_date, task = task_listbox.get(ANCHOR).split(': ', 1)
            task_date_object = datetime.strptime(task_date, '%d/%m/%Y').date()
            global task_dict
            global task_dict_sorted
            task_dict[task_date_object].remove(task)
            #TASK DICT UPDATES = TASK DICT SORTED ALSO UPDATES?
            #task_dict_sorted[task_date_object].remove(task) 
            main_cal.calevent_remove(date=task_date_object)
            for task in task_dict_sorted[task_date_object]:
                main_cal.calevent_create(task_date_object, task, 'reminder')

            task_delete_label.config(text=f'{task_listbox.get(ANCHOR)} has been deleted.')
            task_listbox.delete(ANCHOR)

            if task_listbox.size() == 0:
                task_delete_label.config(text="Your task list is empty!")
                delete_button['state'] = 'disable'
        else:
            task_delete_label.config(text='Select a task to delete!')


    def items_selected(event):
        task_delete_label.config(text=f'{task_listbox.get(ANCHOR)} is going to be deleted')

    top = Toplevel(tk)
    top.geometry('400x400')
    tasks_list_frame = Frame(top)
    tasks_list_scrollbar = Scrollbar(tasks_list_frame, orient=VERTICAL)
    task_list_label = Label(top, text="Delete from your task list", anchor=CENTER, font=("Helvetica 18 underline"))
    task_list_label.pack(pady = 20)
    global task_listbox
    task_listbox = Listbox(tasks_list_frame, font=big_font, width=40, yscrollcommand=tasks_list_scrollbar.set)
    task_listbox.bind('<<ListboxSelect>>', items_selected)
    tasks_list_scrollbar.config(command=task_listbox.yview)
    
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' not in task:
                task_listbox.insert(END, f'{day.strftime("%d/%m/%Y")}: {task}')
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' in task:
                completed_task = day.strftime("%d/%m/%Y") + ':' + task
                task_listbox.insert(END, strike(completed_task))
        
    tasks_list_scrollbar.pack(side=RIGHT, fill=Y)
    tasks_list_frame.pack()
    task_listbox.pack(pady=15)
    task_delete_label = Label(top, text='')
    task_delete_label.pack()
    delete_button = Button(top, text='Delete Tasks', command=delete_task)
    if task_listbox.size() == 0:
        task_delete_label.config(text="Your task list is empty!")
        delete_button['state'] = 'disable'
    delete_button.pack()
    add_back_to_calendar_button(top)



#SHOW TASKS FOR DAY 


def show_tasks_for_day():
    top = Toplevel(tk)
    tasks_list_frame = Frame(top)
    tasks_list_scrollbar = Scrollbar(tasks_list_frame, orient=VERTICAL)
    task_complete_label = Label(top, text='')
    task_listbox_day = Listbox(tasks_list_frame, width=40, font = big_font, yscrollcommand=tasks_list_scrollbar.set)
    

    def complete_task():
        if not task_listbox_day.get(ANCHOR):
            task_complete_label.config(text='Chooese a task to complete!')
            return

        task_completed = task_listbox_day.get(ANCHOR)
        task_completed_index = task_listbox_day.get(0, END).index(task_completed)
        task_completed_strike = strike(task_completed)
        task_listbox_day.insert(END, task_completed_strike)
        task_listbox_day.delete(task_completed_index)
        task_complete_label.config(text=f'{task_listbox_day.get(ANCHOR)} has been completed')

        #global task_dict, task_dict_sorted
        #task_dict[date_obj].append(task_completed_strike) UPDATES TASK_DICT TOO
        task_dict_sorted[date_obj].append(task_completed_strike)
        #task_dict[date_obj].remove(task_completed)
        task_dict_sorted[date_obj].remove(task_completed)
        delete_completed_tasks_button['state'] = 'normal'
        complete_button['state'] = 'disable'
        for task in task_dict_sorted[date_obj]:
            if '\u0336' not in task:
                complete_button['state'] = 'normal'

    def delete_completed_tasks():
        complete_button['state'] = 'disable'
        day_tasks = task_dict_sorted[date_obj].copy()
        day_tasks.reverse()
        for task in day_tasks:
            if '\u0336' in task:
                task_dict_sorted[date_obj].remove(task)
                task_index = task_listbox_day.get(0, END).index(task)
                task_listbox_day.delete(task_index)

                main_cal.calevent_remove(date=date_obj)
                for task in task_dict_sorted[date_obj]:
                    main_cal.calevent_create(date_obj, task, 'reminder')
            if '\u0336' not in task:
                complete_button['state'] = 'normal'
        if task_listbox_day.size() == 0:
            task_complete_label.config(text="Your task list is empty!")
        delete_completed_tasks_button['state'] = 'disable'
        
        
    complete_button = Button(top, text='Complete Task', state='disable', command=complete_task)
    delete_completed_tasks_button = Button(top, text='Delete All Completed Tasks', state='disable', command=delete_completed_tasks)
    date = main_cal.get_date()
    date_obj =  datetime.strptime(date, '%d-%m-%Y').date()
    if date_obj in task_dict_sorted:
        for task in task_dict_sorted[date_obj]:
            task_listbox_day.insert(END, task)
    else:
        task_complete_label.config(text='No tasks for the day')

    def items_selected(event):
        if task_listbox_day.get(ANCHOR):
            if '\u0336' in task_listbox_day.get(ANCHOR):
                complete_button['state'] = 'disable'
                task_complete_label.config(text='This task has been completed!')
            elif '\u0336' not in task_listbox_day.get(ANCHOR):
                complete_button['state'] = 'normal'
                task_complete_label.config(text=f'Is {task_listbox_day.get(ANCHOR)} completed?')
    
    top.geometry('400x400')
   
    
    task_list_label = Label(top, text=f"Tasks for day: {date}", anchor=CENTER, font=("Helvetica 18 underline"))
    task_list_label.pack(pady = 20)
    
    task_listbox_day.bind('<<ListboxSelect>>', items_selected)
    tasks_list_scrollbar.config(command=task_listbox_day.yview)
    
    tasks_list_scrollbar.pack(side=RIGHT, fill=Y)
    tasks_list_frame.pack()
    task_listbox_day.pack(pady=15)
    task_complete_label.pack()
    if task_listbox_day.size() == 0:
        task_complete_label.config(text="Your task list is empty!")

    if date_obj in task_dict_sorted:
        for task in task_dict_sorted[date_obj]:
            if '\u0336' in task:
                delete_completed_tasks_button['state'] = 'normal'
            if '\u0336' not in task:
                complete_button['state'] = 'normal'
    complete_button.pack()
    delete_completed_tasks_button.pack()
    add_back_to_calendar_button(top)





#SHOW TASKS FOR THE WEEK    
#ADD DATES TO THE LISTBOX, TITLE, MAKE SURE WHEN TASK COMPLETES, IT GETS REMOVED CORRECTLY
#FROM TASK_DICT
def show_tasks_for_week():

    dates_list = []
    date_obj = datetime.strptime(main_cal.get_date(), '%d-%m-%Y').date()
    for _ in range(7):
        new_date = date_obj + main_cal.timedelta(days=_)
        dates_list.append(new_date)
        if new_date.weekday() == 6:
            break;
    

    top = Toplevel(tk)
    tasks_list_frame = Frame(top)
    tasks_list_scrollbar = Scrollbar(tasks_list_frame, orient=VERTICAL)
    task_list_label = Label(top, text="Your Task List for the week", anchor=CENTER, font=("Helvetica 18 underline"))
    task_list_label.pack(pady = 20)
    task_complete_label = Label(top, text='')

    def items_selected(event):
        if task_listbox.get(ANCHOR):
            if '\u0336' in task_listbox.get(ANCHOR):
                complete_button['state'] = 'disable'
                task_complete_label.config(text='This task has been completed!')
                return
            elif '\u0336' not in task_listbox.get(ANCHOR):
                complete_button['state'] = 'normal'
                task_complete_label.config(text=f'Is {task_listbox.get(ANCHOR)} completed?')

    def complete_task():
        if '\u0336' in task_listbox.get(ANCHOR):
            task_complete_label.config(text='This task has been completed!')
        if not task_listbox.get(ANCHOR):
            task_complete_label.config(text='Chooese a task to complete!')
            return
        task_completed = task_listbox.get(ANCHOR)
        task_completed_index = task_listbox.get(0, END).index(task_completed)
        task_completed_strike = strike(task_completed)
        task_listbox.insert(END, task_completed_strike)
        task_listbox.delete(task_completed_index)
        task_complete_label.config(text=f'{task_listbox.get(ANCHOR)} has been completed')

        
        #task_dict[date_obj].append(task_completed_strike) UPDATES TASK_DICT TOO
        task_dict_sorted[date_obj].append(task_completed_strike)
        #task_dict[date_obj].remove(task_completed)
        task_dict_sorted[date_obj].remove(task_completed)
        delete_completed_tasks_button['state'] = 'normal'
        complete_button['state'] = 'disable'
        for date in dates_list:
            if date in task_dict_sorted:
                for task in task_dict_sorted[date]:
                    if '\u0336' not in task:
                        complete_button['state'] = 'normal'


    def delete_completed_tasks():
        complete_button['state'] = 'disable'
        day_tasks = task_dict_sorted[date_obj].copy()
        day_tasks.reverse()
        for task in day_tasks:
            if '\u0336' in task:
                task_dict_sorted[date_obj].remove(task)
                task_index = task_listbox.get(0, END).index(task)
                task_listbox.delete(task_index)

                main_cal.calevent_remove(date=date_obj)
                for task in task_dict_sorted[date_obj]:
                    main_cal.calevent_create(date_obj, task, 'reminder')

                if '\u0336' not in task:
                    complete_button['state'] = 'normal'
        delete_completed_tasks_button['state'] = 'disable'
        if task_listbox.size() == 0:
            task_complete_label.config(text='No tasks for the week')

    task_listbox = Listbox(tasks_list_frame, width=40, font=big_font, yscrollcommand=tasks_list_scrollbar.set)
    tasks_list_scrollbar.config(command=task_listbox.yview)
    task_listbox.bind('<<ListboxSelect>>', items_selected)
    complete_button = Button(top, state='disable', text='Complete Task', command=complete_task)
    delete_completed_tasks_button = Button(top, text='Delete All Completed Tasks', state='disable', command=delete_completed_tasks)
    
    for day in dates_list:
        if day in task_dict_sorted:
            for task in task_dict_sorted[day]:
                task_listbox.insert(END, task)
    if task_listbox.size() == 0:
        task_complete_label.config(text='No tasks for the day')
        complete_button['state'] = 'disable'
        delete_completed_tasks_button['state'] = 'disable'

    
    tasks_list_scrollbar.pack(side=RIGHT, fill=Y)
    tasks_list_frame.pack()
    task_listbox.pack(pady=15)
    task_complete_label.pack()
    if task_listbox.size() == 0:
        task_complete_label.config(text="Your task list is empty!")
        complete_button['state'] = 'disable'
        delete_completed_tasks_button['state'] = 'disable'
    for date in task_dict_sorted:
        for task in task_dict[date]:
            if '\u0336' in task:
                delete_completed_tasks_button['state'] = 'normal'
            if '\u0336' not in task:
                complete_button['state'] = 'normal'
    complete_button.pack()
    delete_completed_tasks_button.pack()
    add_back_to_calendar_button(top)



# Create The Gui Object
tk = Tk()
tk.update_idletasks()
big_font = font.Font(size=15)
 
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
task_dict_sorted = {}

Button(tk, text="Task List", command=show_task_list).grid(row=2, column=0)

Button(tk, text="Delete Tasks", command=delete_tasks_window).grid(row=2, column=1)

Button(tk, text="Tasks for the selected day", command=show_tasks_for_day).grid(row=1, column=3)
Button(tk, text="Tasks for the selected week", command=show_tasks_for_week).grid(row=2, column=3)
 
date = Label(tk, text = "")
date.grid(row = 100, column = 0)
 
# Execute Tkinter
tk.mainloop()