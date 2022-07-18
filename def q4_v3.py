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


q4()