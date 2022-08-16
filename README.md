![](https://github.com/HJH-08/calendar-planner/blob/main/%F0%9F%93%86_Calendar_Planner.png)

# Calendar Planner

### Easily input, complete and delete tasks

This project is written in `Python`. It allows users to constantly update the calendar when tasks 
come up and when tasks are completed. The calendar is automatically updated, whereby if there is a task on a certain date, that date turns red. By hovering the mouse over that date, tasks will pop out.
The user can:

* Add tasks into their task list
* Complete tasks which then strikesthrough their task
* Delete tasks which completely removes the task from the calendar
* View their entire task list
* View their tasks on a selected date
* View their tasks on the week of a selected date
* Save and complete which ensures data stored is kept in a `json` file, which will then be read when the calendar planner is run the next time so that the data is not lost

### Recording of the calendar planner in use

This shows how the user can add a task, and then see the task in the task list. Afterwhich, he can choose to complete the task and delete the task altogether.

![](https://github.com/HJH-08/calendar-planner/blob/main/Calendar%20Planner%20recording.gif)
<img src="https://github.com/HJH-08/calendar-planner/blob/main/Calendar%20Planner%20recording.gif" alt="Recording of calendar planner" width="1000" href=''/>

### Prerequisites

Python installed locally. Check [here](https://www.python.org/downloads/) to install depending on your OS.

### Prerequisites
Required Modules
- `tkinter`
- `tkcalendar`

To install `tkinter` (if it's not already in built):
```
$ pip install tkinter
```

To install `tkcalendar`: 
```
$ pip install tkcalendar
```

### How to run the script
``` bash
$ python calendar-planner.py
```

The calendar planner window will be opened.