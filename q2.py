def q2(more):
    options = {'causes': "efiohaofshfsohfa", 'effects': "ioawuooidhasyifoejtbibnafuodcn09mjfishiufidsouisuvovfo8ub0eyfasioofhsohigltyuui"}
    if more == "yes":
        valid = False
        while not valid:
            choice = input("""what would you like to find out more about mental health issues?
             Type 'c' to find out about the causes and 'e' to find out about the effects.""")
            if choice == "c":
                print(options['causes'])
                break
            elif choice == "e":
                print(options['effects'])
                break
            else:
                print("please type c or e")
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
