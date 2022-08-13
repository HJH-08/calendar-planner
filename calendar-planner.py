# Importing The Essential Libraries
from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import datetime
from tkinter import font

def add_back_to_calendar_button(master):
    back_to_calendar_button = Button(master, text="Back to Calendar", command=master.destroy)
    back_to_calendar_button.pack()
#ADD TASK PAGE
#SAVE INFO INTO EXCEL?

def show_instructions():
    top = Toplevel(tk)
    top.geometry('600x700')


    def hide_intro():
        intro_label.config(text='')
        intro_button.config(text='Introduction', command=show_intro)
    def show_intro():
        intro_label.config(text=intro_text)
        intro_button.config(text='Hide Introduction', command=hide_intro)
    intro_text = ("This is a calendar app planner. Blue on the calendar means selected date, and the default selected date is" 
    " today. Red on the calendar means there is a reminder on that date. Hover over that date and wait a few seconds for the" 
    " task(s) to show up.")
    intro_label = Label(top, wraplength=600, text='', font=("Helvetica 12"))
    intro_button = Button(top, text="Introduction", command=show_intro)
    intro_button.pack(pady=(30,0))
    intro_label.pack(pady=5)

    def hide_addtask():
        addtask_label.config(text='')
        addtask_button.config(text='About Add Tasks', command=show_addtask)
    def show_addtask():
        addtask_label.config(text=addtask_text)
        addtask_button.config(text='Hide Add Tasks', command=hide_addtask)
    addtask_text = ("Add any task on any date using the add task button. The calendar will be updated when the added task is" 
    " confirmed. You cannot add any repeated tasks in any single day. Tasks are case sensitive.")
    addtask_label = Label(top, wraplength=600, text='', font=("Helvetica 12"))
    addtask_button = Button(top, text="About Add Tasks", command=show_addtask)
    addtask_button.pack()
    addtask_label.pack(pady=5)

    def hide_deletetask():
        deletetask_label.config(text='')
        deletetask_button.config(text='About Delete Tasks', command=show_deletetask)
    def show_deletetask():
        deletetask_label.config(text=deletetask_text)
        deletetask_button.config(text='Hide Delete Tasks', command=hide_deletetask)
    deletetask_text = ("Select any task from the task list to delete. Upon confirmation, the task will be removed permenantly."
    " The calendar will automatically be updated.")
    deletetask_label = Label(top, wraplength=600, text='', font=("Helvetica 12"))
    deletetask_button = Button(top, text="About Delete Tasks", command=show_deletetask)
    deletetask_button.pack()
    deletetask_label.pack(pady=5)

    def hide_tasklist():
        tasklist_label.config(text='')
        tasklist_button.config(text='About Tasks Lists', command=show_tasklist)
    def show_tasklist():
        tasklist_label.config(text=tasklist_text)
        tasklist_button.config(text='Hide Tasks Lists', command=hide_tasklist)
    tasklist_text = "This button shows you all your tasks that you have inputted in the planner."
    tasklist_label = Label(top, wraplength=600, text='', font=("Helvetica 12"))
    tasklist_button = Button(top, text="About Tasks Lists", command=show_tasklist)
    tasklist_button.pack()
    tasklist_label.pack(pady=5)

    def hide_taskforday():
        taskforday_label.config(text='')
        taskforday_button.config(text='About Tasks For The Day', command=show_taskforday)
    def show_taskforday():
        taskforday_label.config(text=taskforday_text)
        taskforday_button.config(text='Hide Tasks For The Day', command=hide_taskforday)
    taskforday_text = ("This button will show you what tasks you have on any selected day. If you do not have any tasks," 
    " it will say that your task list is empty. You can choose to complete a task. By completing a task, the task will appear" 
    " cancelled, but it will still appear on the calendar. In order to delete a specific task, go to the delete tasks button"
    " to delete the task. All completed tasks are grouped together at the buttom according to their date. You can choose to" 
    " delete all completed tasks at one go too.")
    taskforday_label = Label(top, wraplength=600, text='', font=("Helvetica 12"))
    taskforday_button = Button(top, text="About Tasks For The Day", command=show_taskforday)
    taskforday_button.pack()
    taskforday_label.pack(pady=5)

    def hide_taskforweek():
        taskforweek_label.config(text='')
        taskforweek_button.config(text='About Tasks For The Week', command=show_taskforweek)
    def show_taskforweek():
        taskforweek_label.config(text=taskforweek_text)
        taskforweek_button.config(text='Hide Tasks For The Week', command=hide_taskforweek)
    taskforweek_text = ("This button shows you the tasks you have from the selected day to the end of that particular week."
    " Functionalities are the same as the Show Task for Day button.")
    taskforweek_label = Label(top, wraplength=600, text='', font=("Helvetica 12"))
    taskforweek_button = Button(top, text="About Tasks For The Week", command=show_taskforweek)
    taskforweek_button.pack()
    taskforweek_label.pack(pady=5)

    add_back_to_calendar_button(top)



def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def unstrike(text):
    newtext = text.replace('\u0336', '')
    return newtext

def add_task():
    def confirm_task():
        no_task_label.pack_forget()
        repeated_task_label.pack_forget()
        confirmed_task_label.config(text='')
        if user_task_input_entry.get() == '':
            no_task_label.pack()
            return
        if cal.get_date() in task_dict_sorted:
            if user_task_input_entry.get() in task_dict_sorted[cal.get_date()]:
                repeated_task_label.pack()
                return
        text = user_task_input_entry.get() + ' on ' + cal.get_date().strftime("%d-%m-%Y") + ' added to calendar'
        confirmed_task_label.config(text=text)
        confirmed_task_label.pack()

        main_cal.tag_config('reminder', background='red', foreground='yellow')
        if cal.get_date() in task_dict:
            if user_task_input_entry.get() not in task_dict[cal.get_date()]:
                task_dict[cal.get_date()].append(user_task_input_entry.get())
                main_cal.calevent_create(cal.get_date(), user_task_input_entry.get(), 'reminder')

        else:
            task_dict[cal.get_date()] = [user_task_input_entry.get()]
            main_cal.calevent_create(cal.get_date(), user_task_input_entry.get(), 'reminder')

        
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
                    foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
    cal.set_date(date_from_main)
    cal.pack(padx=10, pady=10)  

    confirm_button = Button(top, text="Confirm", command=confirm_task)
    confirm_button.pack(pady=10)
    no_task_label = Label(top, text="Input some task please!")
    repeated_task_label = Label(top, text="This is a repeated task. Input a different task!", wraplength=150)

    confirmed_task_label = Label(top, wraplength=300)
    back_to_calendar_button = Button(top, text="Back to Calendar", command=top.destroy)
    back_to_calendar_button.pack()
    enter_another_task_button = Button(top, text="Create Another Task", command=create_another_task)

def show_task_list():
    top = Toplevel(tk)
    top.geometry('500x500')

    def items_selected(event):
        if task_listbox.get(ANCHOR):
            task_info_label.config(text=unstrike(task_listbox.get(ANCHOR)))
        task_info_label.pack()


    tasks_list_frame = Frame(top)
    tasks_list_scrollbar = Scrollbar(tasks_list_frame, orient=VERTICAL)
    task_list_label = Label(top, text="Your Task List", anchor=CENTER, font=("Helvetica 18 underline"))
    task_list_label.pack(pady = 20)

    global task_listbox
    task_listbox = Listbox(tasks_list_frame, width=40, font=big_font, yscrollcommand=tasks_list_scrollbar.set)
    tasks_list_scrollbar.config(command=task_listbox.yview)
    task_listbox.bind('<<ListboxSelect>>', items_selected)

    task_info_label = Label(top, text='', font='Helvetica 12')

    task_dict_sorted = {}
    for date in sorted(task_dict):
        task_dict_sorted[date] = task_dict[date]
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' not in task:
                task_listbox.insert(END, f'{day.strftime("%d-%m-%Y")}: {task}')
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' in task:
                completed_task = day.strftime("%d-%m-%Y") + ': ' + task
                task_listbox.insert(END, strike(completed_task))
    
    tasks_list_scrollbar.pack(side=RIGHT, fill=Y)
    tasks_list_frame.pack()
    task_listbox.pack(pady=15)
    task_info_label.pack(pady=15)
    if task_listbox.size() == 0:
        task_info_label.config(text="Your task list is empty. Input some tasks in the add tasks tab!")
    add_back_to_calendar_button(top)
    


def delete_tasks_window():
    
    def delete_task():
        if task_listbox.get(ANCHOR):
            if '\u0336' in task_listbox.get(ANCHOR):
                task_date, task_unstrike = unstrike(task_listbox.get(ANCHOR)).split(': ', 1);
                task = strike(task_unstrike)

            if '\u0336' not in task_listbox.get(ANCHOR):
                task_date, task = task_listbox.get(ANCHOR).split(': ', 1)
                
            task_date_object = datetime.strptime(task_date, '%d-%m-%Y').date()

            task_dict[task_date_object].remove(task)
            #TASK DICT UPDATES = TASK DICT SORTED ALSO UPDATES?
            #task_dict_sorted[task_date_object].remove(task) 
            main_cal.calevent_remove(date=task_date_object)
            for task in task_dict_sorted[task_date_object]:
                main_cal.calevent_create(task_date_object, task, 'reminder')

            task_delete_label.config(text=f'{task_date}: {task} has been deleted.')
            task_listbox.delete(ANCHOR)

            if task_listbox.size() == 0:
                task_delete_label.config(text="Your task list is empty!")
                delete_button['state'] = 'disable'
        else:
            task_delete_label.config(text='Select a task to delete!')


    def items_selected(event):
        task_delete_label.config(text=f'{task_listbox.get(ANCHOR)} is going to be deleted')

    top = Toplevel(tk)
    top.geometry('500x500')
    tasks_list_frame = Frame(top)
    tasks_list_scrollbar = Scrollbar(tasks_list_frame, orient=VERTICAL)
    task_list_label = Label(top, text="Delete from your task list", anchor=CENTER, font=("Helvetica 15 underline"))
    task_list_label.pack(pady = 10)
    global task_listbox
    task_listbox = Listbox(tasks_list_frame, font=big_font, width=40, yscrollcommand=tasks_list_scrollbar.set)
    task_listbox.bind('<<ListboxSelect>>', items_selected)
    tasks_list_scrollbar.config(command=task_listbox.yview)
    
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' not in task:
                task_listbox.insert(END, f'{day.strftime("%d-%m-%Y")}: {task}')
    for day in task_dict_sorted:
        for task in task_dict_sorted[day]:
            if '\u0336' in task:
                completed_task = day.strftime("%d-%m-%Y") + ': ' + task
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
    delete_button.pack(pady=10)
    add_back_to_calendar_button(top)



#SHOW TASKS FOR DAY 


def show_tasks_for_day():
    top = Toplevel(tk)
    top.geometry('550x550')
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
        task_complete_label.config(text=f'{task_completed} has been completed')

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
            if '\u0336' not in task:
                task_listbox_day.insert(END, task)
        for task in task_dict_sorted[date_obj]:
            if '\u0336' in task:
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
    
   
    
    task_list_label = Label(top, text=f"Tasks for day: {date}", anchor=CENTER, font=("Helvetica 18 underline"))
    task_list_label.pack(pady = 15)
    
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
    complete_button.pack(pady=12)
    delete_completed_tasks_button.pack(pady=12)
    add_back_to_calendar_button(top)



#SHOW TASKS FOR THE WEEK    
def show_tasks_for_week():

    dates_list = []
    date_obj = datetime.strptime(main_cal.get_date(), '%d-%m-%Y').date()
    for _ in range(7):
        new_date = date_obj + main_cal.timedelta(days=_)
        dates_list.append(new_date)
        if new_date.weekday() == 6:
            break;
    selected_date = dates_list[0].strftime("%d-%m-%Y")
    end_date = dates_list[-1].strftime("%d-%m-%Y")
    

    top = Toplevel(tk)
    top.geometry('550x550')
    tasks_list_frame = Frame(top)
    tasks_list_scrollbar = Scrollbar(tasks_list_frame, orient=VERTICAL)
    task_list_label = Label(top, text=f"Task List for the week: {selected_date} to {end_date}", anchor=CENTER, font=("Helvetica 14 underline"))
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
        task_date, task_details = task_completed.split(': ')
        task_complete_label.config(text=f'{task_completed} has been completed')

        task_date_obj = datetime.strptime(task_date, "%d-%m-%Y").date()
        #task_dict[date_obj].append(task_completed_strike) UPDATES TASK_DICT TOO
        task_dict_sorted[task_date_obj].append(strike(task_details))
        #task_dict[date_obj].remove(task_completed)
        task_dict_sorted[task_date_obj].remove(task_details)
        delete_completed_tasks_button['state'] = 'normal'
        complete_button['state'] = 'disable'
        for date in dates_list:
            if date in task_dict_sorted:
                for task in task_dict_sorted[date]:
                    if '\u0336' not in task:
                        complete_button['state'] = 'normal'


    def delete_completed_tasks():
        complete_button['state'] = 'disable'
        day_tasks = []
        for date in dates_list:
            if date in task_dict_sorted:
                for task in task_dict_sorted[date]:
                    if '\u0336' in task:
                        day_tasks.append(f'{date}: {task}')
                    if '\u0336' not in task:
                        complete_button['state'] = 'normal'
        day_tasks.reverse()
        for task in day_tasks:
            date_str, task_details = task.split(': ')
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            date_listbox_plus_first_part = strike(date.strftime('%d-%m-%Y')) + strike(': ')
            task_index = task_listbox.get(0, END).index(f'{date_listbox_plus_first_part}{task_details}')
            task_listbox.delete(task_index)
            task_dict_sorted[date].remove(task_details)

            

            main_cal.calevent_remove(date=date)
            for task in task_dict_sorted[date]:
                main_cal.calevent_create(date, task, 'reminder')

                

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
            day_formatted = day.strftime("%d-%m-%Y")
            for task in task_dict_sorted[day]:
                if '\u0336' not in task:
                    task_listbox.insert(END, f'{day_formatted}: {task}')
    for day in dates_list:
        if day in task_dict_sorted:
            day_formatted = day.strftime("%d-%m-%Y")
            for task in task_dict_sorted[day]:
                if '\u0336' in task:
                    striked_first_part = strike(day_formatted) + strike(': ')
                    task_listbox.insert(END, f'{striked_first_part}{task}')

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
    complete_button.pack(pady=12)
    delete_completed_tasks_button.pack(pady=12)
    add_back_to_calendar_button(top)



# Create The Gui Object
tk = Tk()
tk.update_idletasks()
column_number = 3
row_number = 5
for _ in range(0, column_number):
    Grid.columnconfigure(tk, _, weight=1)
for _ in range(0, row_number):
    Grid.rowconfigure(tk, _, weight=1)
    if _ == 2:
        Grid.rowconfigure(tk, _, weight=8)

big_font = font.Font(size=15)
 
# Set the geometry of the GUI Interface
tk.geometry("500x500")
 
title_label = Label(tk, text='Calendar Planner', font=("Helvetica 20 bold underline"), anchor='center')
title_label.grid(row=0, column=1)#, columnspan=3)

details_button = Button(tk, text='Show information', command=show_instructions, anchor='center')
details_button.grid(row=1, column=1)


# Add the Calendar module
main_cal = Calendar(
tk, selectmode = 'day', date_pattern = 'dd-mm-yyyy', 
background = '#00008B', foreground = 'white',
headersbackground = '#A7C7E7', headersforeground = 'black',
weekendbackground = '#f6f6f6', othermonthbackground = '#ececec',
othermonthwebackground = '#e2e2e2', cursor='hand1' )
 
main_cal.grid(row=2, column=0, columnspan=3, sticky='WENS', pady = 50)



Button(tk, text="Add Task", command=add_task).grid(row=3, column=0)
task_dict = {}
task_dict_sorted = {}

Button(tk, text="Task List", command=show_task_list).grid(row=3, column=2)

Button(tk, text="Delete Tasks", command=delete_tasks_window).grid(row=3, column=1)

Button(tk, text="Tasks for the day", command=show_tasks_for_day).grid(row=4, column=0, pady=20)
Button(tk, text="Tasks for the week", command=show_tasks_for_week).grid(row=4, column=1, pady=20)

 
# Execute Tkinter
tk.mainloop()