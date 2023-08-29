
def query_user_data() -> list:
    # taking in user data of 5 questions -
    # food, water, sleep, stress, physical activity
    # on a scale of 1 to 10
    data = []
    print("Welcome! May I please have your username?")
    username = input("Username: ")
    data.append(username)
    print("On the scale of 1 to 10, how would you rate your eating habits?")
    print("A 1 would indicate very poor eating habits.")
    print("A 10 would indicate perfect eating habits.")
    data.append(input("Food: "))
    print("On a scale of 1 to 10, how would you rate your water intake?")
    print("A 1 would indicate not drinking enough water")
    print("A 10 would indicate drinking the perfect amount of water")
    data.append(input("Water: "))
    print("On a scale of 1 to 10, how would you rate your sleep?")
    print("A 1 would indicate very poor sleep quality.")
    print("A 10 would indicate perfect sleep quality.")
    data.append(input("Sleep: "))
    print("On a scale of 1 to 10, how would you rate your stress?")
    print("WARNING: The scale is inverted with this question.") 
    print("Pleae pay close attention to your answer.")
    print("A 1 would indicate very low levels of stress")
    print("A 10 would indicate extreme levels of stress")
    data.append(input("Stress: "))
    print("On a scale of 1 to 10, how would you rate your physical acvitivty?")
    print("A 1 would indicate very low levels of physical activity.")
    print("A 10 would indicate very high levels of physical activity.")
    data.append(input("Physical activity: "))
    print("Wonderful! Please check in again tomorrow.")
    return data
