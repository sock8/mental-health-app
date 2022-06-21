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

q1a = q1()