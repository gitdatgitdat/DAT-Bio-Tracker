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

#print("Welcome! May I please have your username?")
#username = input("Username: ")
#username = username.lower()
#user_data = username + ".csv"




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
    user_data = user.get().lower() + ".csv"
    time_series = pd.read_csv(user_data) # reload the saved data as a dataframe for analysis
    print(time_series)
    time_series.plot() #make a quick plot to view the data
    plt.show()

def input_data():
    fud.write_user_data(fud.query_user_data_CLI(), user_data)

def show_user_data_GUI():
    top = tk.Toplevel(root)
    
    top.title("Please input data")
    input_frame = ttk.Frame(top, padding = "10 10 10 10")
    input_frame.grid(column = 0, row = 0, sticky=(tk.N, tk.W, tk.E, tk.S))
    top.columnconfigure(0, weight = 1)
    top.rowconfigure(0, weight = 1)
    
    ttk.Label(input_frame, text = "On the scale of 1 to 10, how would you rate your eating habits?").grid(column = 1, row = 1, sticky = (tk.W, tk.E))
    ttk.Label(input_frame, text = "1 indicates poor eating habits and 10 indicates perfect eating.").grid(column = 1, row = 2, sticky = tk.W)
    food_entry = ttk.Entry(input_frame, width=3, textvariable=food)
    food_entry.grid(column = 2, row = 2, sticky = tk.E)
    
    ttk.Label(input_frame, text = "On the scale of 1 to 10, how would you rate your water intake?").grid(column = 1, row = 3, sticky = (tk.W, tk.E))
    ttk.Label(input_frame, text = "1 indicates not drinking enough and 10 indicates perfect amount.").grid(column = 1, row = 4, sticky = tk.W)
    water_entry = ttk.Entry(input_frame, width=3, textvariable=water)
    water_entry.grid(column = 2, row = 4, sticky = tk.E)

    ttk.Label(input_frame, text = "On the scale of 1 to 10, how would you rate your sleep?").grid(column = 1, row = 5, sticky = (tk.W, tk.E))
    ttk.Label(input_frame, text = "1 indicates poor sleep quality and 10 indicates perfect sleep.").grid(column = 1, row = 6, sticky = tk.W)
    sleep_entry = ttk.Entry(input_frame, width=3, textvariable=sleep)
    sleep_entry.grid(column = 2, row = 6, sticky = tk.E)
    
    ttk.Label(input_frame, text = "On the scale of 1 to 10, how would you rate your stress?").grid(column = 1, row = 7, sticky = (tk.W, tk.E))
    ttk.Label(input_frame, text = "PLEASE NOTE that the scale is reversed for this question.").grid(column = 1, row = 8, sticky = (tk.W, tk.E))
    ttk.Label(input_frame, text = "1 indicates little to no stress and 10 indicates extreme stress.").grid(column = 1, row = 9, sticky = tk.W)
    stress_entry = ttk.Entry(input_frame, width=3, textvariable=stress)
    stress_entry.grid(column = 2, row = 9, sticky = tk.E)
    
    ttk.Label(input_frame, text = "On the scale of 1 to 10, how would you rate your physical activity?").grid(column = 1, row = 10, sticky = (tk.W, tk.E))
    ttk.Label(input_frame, text = "1 indicates minimal activity and 10 indicates a very high level of activity.").grid(column = 1, row = 11, sticky = tk.W)
    activity_entry = ttk.Entry(input_frame, width=3, textvariable=activity)
    activity_entry.grid(column = 2, row = 11, sticky = tk.E)
    
    ttk.Button(input_frame, text = "Confirm Entries", command = write_GUI_reponses).grid(column = 1, row = 12, sticky = tk.S)

def write_GUI_reponses():
    file_name = user.get().lower() + ".csv"
    fud.write_user_data([food.get(), water.get(), sleep.get(), stress.get(), activity.get()], file_name)

def set_user():
    username = user.get().lower()
    print(username)
    user_data = username + ".csv"
    print(user_data)
    try:
        open(user_data, "r")
    except:
        with open(user_data, "a") as new_file:
            new_file.write("date, food, water, sleep, stress, activity\n")


root = tk.Tk()
root.title("DAT Biotracker")
mainframe = ttk.Frame(root, padding = "10 10 10 10")
mainframe.grid(column = 0, row = 0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

food = tk.StringVar()
water = tk.StringVar()
sleep = tk.StringVar()
stress = tk.StringVar()
activity = tk.StringVar()
user = tk.StringVar()

ttk.Label(mainframe, text = "Welcome. Please select 'Input' to log your data for the day or 'Output' to view your data thus far.").grid(column = 2, row = 1, sticky = tk.N)

ttk.Label(mainframe, text = "User:").grid(column = 1, row = 2, sticky = tk.W)
ttk.Entry(mainframe, width = 10, textvariable = user).grid(column = 2, row = 2, sticky = (tk.W, tk.E))
ttk.Button(mainframe, text = "Set user", command = set_user).grid(column = 3, row = 2, sticky = tk.E)


ttk.Button(mainframe, text = "Input", command = show_user_data_GUI).grid(column = 1, row = 3, sticky = tk.S)
ttk.Button(mainframe, text = "Output", command = plot_by_time).grid(column = 2, row = 3, sticky = tk.S)
ttk.Button(mainframe, text='Example calendar with events', command = show_example_calendar).grid(column = 3, row = 3, sticky = tk.S)

root.mainloop()
