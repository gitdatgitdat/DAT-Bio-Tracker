import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
user_data = "user_data.csv"


# TODO 1-off get user name

def query_user_data() -> list:
    # taking in user data of 5 questions -
    # food, water, sleep, stress, physical activity
    # on a scale of 1 to 10
    data = []
    print("On the scale of 1 to 10, how would you rate the follow:")
    data.append(input("Food: "))
    data.append(input("Water: "))
    data.append(input("Sleep: "))
    data.append(input("Stress: "))
    data.append(input("Physical activity: "))
    return data


def write_user_data(new_line: list):
    with open(user_data, "a") as my_file:
        line = str(datetime.today().date()) + ","
        for response in new_line:
            line = line + response + ','
        line = line[:-1] + "\n"
        my_file.write(line)
    print("File saved!")


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