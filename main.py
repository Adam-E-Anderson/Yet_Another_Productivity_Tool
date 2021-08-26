#Lets start with a usual TODO list. Right now due to lack of knowledge this is all going to be reset everytime the program terminates.
print("Welcome to Yet Another Productivity Tool! YAPT for short.")
print("The goal of this software is to create a todo list with priorities built in. This way you can mark what is high, daily, and low priorites")

high_priority = []
daily_todo = []
low_priority = []
exit_program = False
while not exit_program:
    print("-----Menu----- \n1.Insert High Priority Item\n2.Daily To Do's\n3.Low Priorites\n4.Print Priorities")
    menu_selection = int(input())

    if menu_selection == 1:
        item = input("Enter your High Priority item: ")
        high_priority.append(item)
    elif menu_selection == 2:
        item = input("Enter your Daily To Do item: ")
        daily_todo.append(item)
    elif menu_selection == 3:
        item = input("Enter your Low Priority item: ")
        low_priority.append(item)
    elif menu_selection == 4:
        print("High Priorites")
        for i in range(len(high_priority)):
            print(i+1, high_priority[i])
    else:
        print("Invalid selection. Exiting the program")
        exit_program = True
