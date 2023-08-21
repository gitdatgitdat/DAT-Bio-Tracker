from datetime import datetime

user_data = "user_data.csv"

def query_user_data():
    #taking in user data of 5 questions - 
    #food, water, sleep, stress, physical activity
    #on a scale of 1 to 10
    data = []
    print("On the scale of 1 to 10, how would you rate the follow:")
    data.append(input("Food: "))
    data.append(input("Water: "))
    data.append(input("Sleep: "))
    data.append(input("Stress: "))
    data.append(input("Physical activity: "))
    with open(user_data, "a") as my_file:
        line = str(datetime.today().date()) + ","
        for response in data:
            line = line + response + ','
        line = line[:-1] + "\n"
        my_file.write(line)
    print("File saved!")

query_user_data()

