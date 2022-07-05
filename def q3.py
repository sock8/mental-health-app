def q3():
    options = ["yes", "no"]
    valid = True
    while valid:
        yes_no = input("Would you like to know how you can deal with mental health issues? enter 'yes' or 'no'")
        if yes_no in options:
            return yes_no
        else:
            valid = True

yes_no = q3()
