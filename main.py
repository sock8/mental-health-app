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

def q2(more):
    options = {'causes': "efiohaofshfsohfa", 'effects': "ioawuooidhasyifoejtbibnafuodcn09mjfishiufidsouisuvovfo8ub0eyfasioofhsohigltyuui"}
    if more == "yes":
        valid = False
        while not valid:
            choice = input("""what would you like to find out more about mental health issues?
             Type 'c' to find out about the causes, 'e' to find out about the effects and 'b' to find out about both.""")
            if choice == "c":
                print(options['causes'])
                break
            elif choice == "e":
                print(options['effects'])
                break
            elif choice =="b":
                print(options)
                break
            else:
                print("please type c or e or b")
    else:
        return

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

def q4():
    options = {1: "prevention methods", 2: "treatment methods", 3: "prevention methods and treatment methods"}
    print("""Please select a topic to learn about;
type 1 to find out about prevention methods,
type 2 to find out about treatment methods,
type 3 to find out about prevention methods and treatment methods""")
    valid = True
    while valid:
        choice = int(input(""))
        if choice == 1:
            print(options[1])
            break
        elif choice == 2:
            print(options[2])
            break
        elif choice == 3:
            print(options[3])
            break
        else:
            print("please type 1, 2 or 3")
            valid = True

name = input("Welcome to the mental health information hub, what is your name?")
print("Hello {}, this program will help you learn more about mental health issues".format(name))


q1a = q1()
valid = False
while not valid:
    more = input("Would you like to find out more about what mental health issues are? type yes or no")
    if more == "yes":
        q2a = q2(more)
        break
    elif more == "no":
        break
    else:
        print("try again")

yes_no = q3()
if yes_no == "yes":
    q4()
