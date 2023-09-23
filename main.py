import Functions_for_user_data as fud
import pandas as pd
import matplotlib.pyplot as plt
from tkcalendar import Calendar #, DateEntry

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

# TODO - DT -> Pandas, QT -> TK

print("Welcome! May I please have your username?")
username = input("Username: ")
username = username.lower()
user_data = username + ".csv"

try:
    open(user_data, "r")
except:
    with open(user_data, "a") as new_file:
        new_file.write("date, food, water, sleep, stress, activity\n")


#new_data = fud.query_user_data()
#fud.write_user_data(new_data, user_data)

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

def plot_by_time():
    time_series = pd.read_csv(user_data) # reload the saved data as a dataframe for analysis
    print(time_series)
    time_series.plot() #make a quick plot to view the data
    plt.show()

def input_data():
    fud.write_user_data(fud.query_user_data(), user_data)
    

root = tk.Tk()
root.title("DAT Biotracker")
mainframe = ttk.Frame(root, padding = "10 10 10 10")
mainframe.grid(column = 0, row = 0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

ttk.Label(mainframe, text = "Welcome").grid(column = 2, row = 1, sticky = tk.N)

ttk.Button(mainframe, text = "Input", command = input_data).grid(column = 1, row = 3, sticky = tk.S)
ttk.Button(mainframe, text = "Output", command = plot_by_time).grid(column = 2, row = 3, sticky = tk.S)
ttk.Button(mainframe, text='Example calendar with events', command = show_example_calendar).grid(column = 3, row = 3, sticky = tk.S)

root.mainloop()
