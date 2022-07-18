def q1():
    valid = False
    while not valid:

        choice = input("Would you like an overview of mental health issues?")
        if choice == "yes":
            print("""Mental health issues are conditions that affect your mood, thinking and behaviour. 
Examples include depression, anxiety, bipolar disorder, schizophrenia, 
eating disorders, PTSD, psychosis, perinatal depression, obsessive compulsive disorder (OCD) and addictive behaviours.""")
            return choice
        elif choice == "no":
            return choice
        else:
            print("Please enter yes or no")

def q2(more):
    options = {'causes': """causes of mental health issues include: 
Genetics, stressful environments, childhood trauma, stressful events, negative thoughts, unhealthy habits, drugs and alcohol, social isolation etc.""",
'symptoms': """\nsymptoms of mental health issues include:
Confused thinking Excessive fears or worries, Extreme mood changes, Withdrawal from friends and activities, low energy, or problems sleeping, 
Extreme feelings of guilt, Suicidal thinking etc."""}

    if more == "yes":
        valid = False
        while not valid:
            choice = input("""what would you like to find out more about mental health issues?
             Type 'c' to find out about the causes, 'e' to find out about the effects and 'b' to find out about both.""")
            if choice == "c":
                print(options['causes'])
                break
            elif choice == "e":
                print(options['symptoms'])
                break
            elif choice =="b":
                print(options['causes'], options['symptoms'])
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
    options = {1: """ways to prevent mental health issues include:
Avoidance of alcohol and drugs, Exercising, Improvement on your social life, meditation, Taking good rest, Seeking for help, etc.""",
               2: """some treatment methods for mental health issues are:
Psychotherapy, Medication, Case management, Hospitalization, Support group, Self help plan and Peer support""",
               3: """ways to prevent mental health issues include:
Avoidance of alcohol and drugs, Exercising, Improvement on your social life, meditation, Taking good rest, Seeking for help, etc.
some treatment methods for mental health issues are:
Psychotherapy, Medication, Case management, Hospitalization, Support group, Self help plan and Peer support"""}
    print("""Please select a topic to learn about;
type 1 to find out about prevention methods,
type 2 to find out about treatment methods,
type 3 to find out about prevention methods and treatment methods""")
    valid = True
    while valid:
        try:
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
        except ValueError:
            print("please type 1, 2 or 3")

def q5():
    print("Would you like to conduct further researach")
    Valid = False
    while not Valid:
        choice = input("Please enter yes or no")
        if choice == "yes":
            print("""link to sources:
'https://www.healthnavigator.org.nz/health-a-z/m/mental-health-conditions/#:~:text=Mental%20health%20conditions%20refer%20conditions'
'https://www.health.govt.nz/your-health/conditions-and-treatments/mental-health'
'https://www.mayoclinic.org/diseases-conditions/mental-illness/symptoms-causes/syc-20374968'""" "\nThank you for using my program")
            break
        elif choice == "no":
            print("Thank you for using my program")
            break
        else:
            Valid = False

Valid = True
while Valid:
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

    q5()

    Valid = False
    print("Would you like to run the program again? Please enter 'yes' or 'no'")
    while not Valid:
        end = input()
        if end == "yes":
            Valid = True
        elif end == "no":
            break
        else:
            print("please type yes or no")
            Valid = False