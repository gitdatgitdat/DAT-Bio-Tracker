
def main():
    satisfied = False
    while not satisfied:
        name = input("Please enter your name:\n")
        age = ""
        while not age:
            try:
                age = int(input("Please enter your age:\n"))
            except:
                print("Please enter age as digits.")
        we_good = input("Your name is " + name + " and age is " + str(age) + " correct? y/n?\n")
        we_good = we_good.lower()
        if(we_good == "yes" or we_good == "yep" or we_good == "y"):
            satisfied = True
        else:
            print("I'm sorry, let's try again.\n")

main()