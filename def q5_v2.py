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

q5()