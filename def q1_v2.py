def q1():
    valid = False
    while not valid:

        choice = input("Would you like an overview of mental health issues?")
        if choice == "yes":
            print("""Mental health issues are
conditions that affect your mood, thinking and behaviour. 
Examples include depression, anxiety, bipolar disorder, schizophrenia, 
eating disorders, PTSD, psychosis, perinatal depression, obsessive compulsive disorder (OCD) and addictive behaviours.""")
            return choice
        elif choice == "no":
            return choice
        else:
            print("Please enter yes or no")

q1a = q1()