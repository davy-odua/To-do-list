#python# TO-DO LIST
# Options:
# 1. Add task
# 2. View tasks
# 3. Delete task
# 4. Mark task as complete
# 5. Quit
#This is my final to do list

tasks = []
while True:
    print("-----MY TO-DO LIST-----")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ").strip()
        tasks.append(task)
    elif choice == "2":
        print("TASKS")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        task = input("Enter a task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found")
    elif choice == "4":
        print("Thank you")
        break
    else:
        print(f"{choice} is an invalid choice")



