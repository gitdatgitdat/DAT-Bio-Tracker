
import pandas as pd
import Query_user_data
import write_user_data
import matplotlib.pyplot as plt
from datetime import datetime
user_data = "[username].csv"


# TODO - 

try:
    open(user_data, "r")
except:
    with open(user_data, "a") as new_file:
        new_file.write("date, food, water, sleep, stress, activity\n")

new_data = query_user_data()
write_user_data(new_data)

time_series = pd.read_csv(user_data) # reload the saved data as a dataframe for analysis
time_series.plot() #make a quick plot to view the data
plt.show() 