
import pandas as pd
import Functions_for_user_data as fud
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk


# TODO - Make file saved use username as title and reference

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

#root = Tk()
#root.title("DAT Biotracker")

#mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column = 0, row = 0, sticky =(N, W ,E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight =1)


#root.mainloop()