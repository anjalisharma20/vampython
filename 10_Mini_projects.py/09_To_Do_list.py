tasks = []

while True:
    print("What do you want to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")
    # elif choice == "2":
    #     print("Your tasks:")
    #     for i, task in enumerate(tasks):
    #         print(f"{i+1}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")