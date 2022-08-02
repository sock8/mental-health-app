# function for loop which makes sure the user inputs valid answers


def yesnocheck():
    options = ["YES", "Y", "NO", "N"]
    valid = False
    # loop for making sure the user inputs a valid answer
    while not valid:
        choice = input("Please type 'yes' or 'no'.").upper()
        if choice in options:
            return choice
        else:
            valid = False


# function for asking the user if
# they want an overview of mental health issues


def mentalhealth_overview():
    print("Would you like an overview of mental health issues?")
    choice = yesnocheck()
    if choice == "YES" or choice == "Y":
        print("""\nMental health issues are conditions that affect your mood,
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


# function for displaying more information about mental health issues
def moreaboutmentalhealth():
    print("\nWould you like to find out more about "
          "what mental health issues are?")
    yes_no = yesnocheck()
    options = {'causes': """\nCauses of mental health issues include:
Genetics, stressful environments, childhood trauma, stressful events,
negative thoughts, unhealthy habits,
drugs and alcohol, social isolation etc.\n""",
               'symptoms': """\nSymptoms of mental health issues include:
Confused thinking Excessive fears or worries, Extreme mood changes,
Withdrawal from friends and activities,
low energy, or problems sleeping,
Extreme feelings of guilt, Suicidal thinking etc."""}

    if yes_no == "YES" or yes_no == "Y":
        print("""\nWhat would you like to find out more about
             mental health issues?
             Type 'c' to find out about the causes, 'e' to find out about
             the effects and 'b' to find out about both.""")
        valid = False
        # loop for making the user input a valid answer
        while not valid:
            choice = input("Please type c or e or b").upper()
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
                valid = False
    else:
        return


# function for displaying ways to deal with mental health issues
def mentalhealth_solution():
    print("\nWould you like to know how you can deal with mental health"
          " issues?")
    yes_no = yesnocheck()

    options = {1: """\nWays to prevent mental health issues include:
Avoidance of alcohol and drugs, Exercising, Improvement on your social life,
meditation, Taking good rest,
Seeking for help, etc.""",
               2: """\nSome treatment methods for mental health issues are:
Psychotherapy, Medication, Case management, Hospitalization, Support
group, Self help plan and Peer support etc.""",
               3: """\nways to prevent mental health issues include:
Avoidance of alcohol and drugs, Exercising, Improvement on your
social life, meditation, Taking good rest,
Seeking for help, etc.
some treatment methods for mental health issues are:
Psychotherapy, Medication, Case management, Hospitalization,
Support group, Self help plan and Peer support."""}

    if yes_no == "YES" or yes_no == "Y":
        print("""\nPlease select a topic to learn about;
    type 1 to find out about prevention methods,
    type 2 to find out about treatment methods,
    type 3 to find out about prevention methods and treatment methods.""")
        valid = True
        # loop making sure the user inputs a valid answer
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
                    print("Please type 1, 2 or 3.")
                    valid = True
            except ValueError:
                print("Please type 1, 2 or 3.")
    else:
        return


# function for providing links for further research to user
def further_research():
    print("\nWould you like to conduct further research?")
    choice = yesnocheck()
    if choice == "YES" or choice == "Y":
        print("Link to sources:")
        print('https://www.healthnavigator.org.nz/health-a-z/m/mental-health-'
              'conditions/#:~:text=Mental%20health%20conditions%'
              '20refer%20conditions')
        print('https://www.health.govt.nz/your-health/conditions'
              '-and-treatments/mental-health')
        print('https://www.mayoclinic.org/diseases-conditions/'
              'mental-illness/symptoms-causes/syc-20374968\n')
    else:
        pass

# loop for repeating program
valid = True
while valid:
    name = input("Welcome to the mental health information hub, what is"
                 " your name?")
    print("Hello {}, this program will help you learn more about mental"
          " health issues.".format(name))

    mentalhealth_overview()

    moreaboutmentalhealth()

    mentalhealth_solution()

    further_research()

    print("Would you like to run the program again?"
          )
    end = yesnocheck()
    if end == "YES" or end == "Y":
        Valid = True
    else:
        print("\nThank you for using my program.")
        break
