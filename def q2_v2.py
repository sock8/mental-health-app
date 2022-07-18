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