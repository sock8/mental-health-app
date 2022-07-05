def q3():
    options = ["yes", "no"]
    valid = True
    print("Would you like to know how you can deal with mental health issues?")
    while valid:
        yes_no = input("Please enter 'yes' or 'no'")
        if yes_no in options:
            return yes_no
        else:
            valid = True


yes_no = q3()