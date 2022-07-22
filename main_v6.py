# 1st function for asking the user if
# they want an overview of mental health issues


def q1():
    valid = False
    while not valid:

        choice = input("Would you like an overview of mental health issues?").upper()
        if choice == "YES" or choice == "Y":
            print("""Mental health issues are conditions that affect your mood,
            thinking and behaviour.
            Examples include depression, anxiety, bipolar disorder,
            schizophrenia,
            eating disorders, PTSD, psychosis, perinatal depression,
            obsessive compulsive disorder (OCD) and addictive behaviours.""")
            return choice
        elif choice == "NO" or choice == "N":
            return choice
        else:
            print("Please enter yes or no")


# 2nd function for displaying more information about mental health issues
def q2(more):
    options = {'causes': """causes of mental health issues include:
Genetics, stressful environments, childhood trauma, stressful events,
negative thoughts, unhealthy habits,
drugs and alcohol, social isolation etc.\n""",
               'symptoms': """symptoms of mental health issues include:
Confused thinking Excessive fears or worries, Extreme mood changes,
Withdrawal from friends and activities,
low energy, or problems sleeping,
Extreme feelings of guilt, Suicidal thinking etc."""}

    if more == "YES" or more == "Y":
        valid = False
        while not valid:
            choice = input("""what would you like to find out more about
             mental health issues?
             Type 'c' to find out about the causes, 'e' to find out about
             the effects and 'b' to find out about both.""").upper()
            if choice == "C":
                print(options['causes'])
                break
            elif choice == "E":
                print(options['symptoms'])
                break
            elif choice == "B":
                print(options['causes'], options['symptoms'])
                break
            else:
                print("please type c or e or b")
    else:
        return


# 3rd function for asking the user if they want to learn
# how they can deal with mental health issues
def q3():
    options = ["YES", "Y", "NO", "N"]
    valid = True
    print("Would you like to know how you can deal with mental health"
          " issues?")
    while valid:
        yes_no = input("Please enter 'yes' or 'no'").upper()
        if yes_no in options:
            return yes_no
        else:
            valid = True


# 4th function for displaying ways to deal with mental health issues
def q4():
    options = {1: """ways to prevent mental health issues include:
Avoidance of alcohol and drugs, Exercising, Improvement on your social life,
meditation, Taking good rest,
Seeking for help, etc.""",
               2: """some treatment methods for mental health issues are:
Psychotherapy, Medication, Case management, Hospitalization, Support
group, Self help plan and Peer support""",
               3: """ways to prevent mental health issues include:
Avoidance of alcohol and drugs, Exercising, Improvement on your
social life, meditation, Taking good rest,
Seeking for help, etc.
some treatment methods for mental health issues are:
Psychotherapy, Medication, Case management, Hospitalization,
Support group, Self help plan and Peer support"""}
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


# 5th function for providing links for further research to user
def q5():
    print("Would you like to conduct further research")
    Valid = False
    while not Valid:
        choice = input("Please enter yes or no").upper()
        if choice == "YES" or choice == "Y":
            print("""link to sources:
'https://www.healthnavigator.org.nz/health-a-z/m/mental-health-conditions
/#:~:text=Mental%20health%20conditions%20refer
%20conditions'
'https://www.health.govt.nz/your-health/conditions-and-treatments/mental
-health'
'https://www.mayoclinic.org/diseases-conditions/mental-illness/symptoms
-causes/syc-20374968'\n"""
                  "Thank you for using my program")
            break
        elif choice == "NO" or choice == "N":
            print("Thank you for using my program")
            break
        else:
            Valid = False


# loop for repeating program
Valid = True
while Valid:
    name = input("Welcome to the mental health information hub, what is"
                 " your name?")
    print("Hello {}, this program will help you learn more about mental"
          " health issues".format(name))

    q1a = q1()
    valid = False
    while not valid:
        more = input("Would you like to find out more about what mental"
                     " health issues are? type yes or no").upper()
        if more == "YES" or more == "Y":
            q2a = q2(more)
            break
        elif more == "NO" or more == "N":
            break
        else:
            print("try again")

    yes_no = q3()
    if yes_no == "YES" or yes_no == "Y":
        q4()

    q5()

    Valid = False
    print("Would you like to run the program again? Please enter 'yes' or 'no'"
          )
    while not Valid:
        end = input().upper()
        if end == "YES" or end == "Y":
            Valid = True
        elif end == "NO" or end == "N":
            break
        else:
            print("please type yes or no")
            Valid = False
