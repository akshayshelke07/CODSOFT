import os
import json

# for tasks storing
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Display
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet, Add one!")
        return
    
    print("\nYour To-Do List: ")
    for i, task in enumerate(tasks, 1):
        status = "YAPP!" if task["done"] else "OPSS!"
        print(f"{i}. [{status}]{task['title']}")
    print()

# Add new task
def add_task(tasks):
    title = input("Enter task title:").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Task title can't be empty...\n")

def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done:  ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Nice! Task marked as done.\n")
        else:
            print("Invalid task number, try again.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task:{removed['title']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# mainmenu
def main():
    tasks = load_tasks()
    while True:
        print("===== 😊To-Do list Menu 😊=====")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. EXIT")
        choice = input("Choose an option(1-5):").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! ")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()