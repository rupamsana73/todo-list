tasks = []

def show_tasks():
    if not tasks:
        print(" No tasks available.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(" Task added successfully.")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_no - 1)
            print(f" Task removed: {removed}")
        except:
            print(" Invalid task number.")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print(" Exiting To-Do List. Goodbye!")
        break
    else:
        print(" Invalid choice. Try again.")
