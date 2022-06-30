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


q4()
