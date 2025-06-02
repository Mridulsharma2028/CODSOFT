tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i+1}. {task['task']} [{status}]")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: ")) - 1
        tasks[task_no]["done"] = True
        print("Task marked as done!")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
