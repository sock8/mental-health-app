#function for loop which makes sure the user inputs valid answers

def yesnocheck():
    options = ["YES", "Y", "NO", "N"]
    valid = False
    while not valid:
        choice = input("please type 'yes' or 'no'").upper()
        if choice in options:
            return choice
        else:
            valid = False



