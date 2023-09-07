
import pandas as pd
import Functions_for_user_data as fud
import matplotlib.pyplot as plt

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

new_data = fud.query_user_data()
fud.write_user_data(new_data, user_data)

time_series = pd.read_csv(user_data) # reload the saved data as a dataframe for analysis
time_series.plot() #make a quick plot to view the data
plt.show()
