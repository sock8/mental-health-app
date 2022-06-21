def q1():
    valid = False
    while not valid:

        choice = input("Would you like an overview of mental health issues?")
        if choice == "yes":
            print("Mental health issues are")
            return choice
        elif choice == "no":
            return choice
        else:
            print("Please enter yes or no")
name = input("Welcome to the mental health information hub, what is your name?")
print("Hello {}, this program will help you learn more about mental health issues".format(name))


q1a = q1()