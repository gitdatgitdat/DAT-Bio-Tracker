
import pandas as pd
import Functions_for_user_data as fud
import matplotlib.pyplot as plt
from tkcalendar import Calendar #, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

# TODO - main.py seems to get upset after third call

print("Welcome! May I please have your username?")
username = input("Username: ")
username = username.lower()
user_data = username + ".csv"

try:
    open(user_data, "r")
except:
    with open(user_data, "a") as new_file:
        new_file.write("date, food, water, sleep, stress, activity\n")

new_data = fud.query_user_data()
fud.write_user_data(new_data, user_data)

time_series = pd.read_csv(user_data) # reload the saved data as a dataframe for analysis
print(time_series)
time_series.plot() #make a quick plot to view the data
plt.show()


# this function is from the tkcalendar tutorial: https://github.com/j4321/tkcalendar#howtos
def show_example_calendar():
    top = tk.Toplevel(root)

    cal = Calendar(top, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', "message")
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.").pack()


root = tk.Tk()
root.title("DAT Biotracker")
ttk.Button(root, text='Example calendar with events', command = show_example_calendar).pack(padx=10, pady=10)

root.mainloop()
