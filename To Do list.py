import os

TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        file.writelines(tasks)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

def add_task(description):
    tasks = load_tasks()
    tasks.append(description + '\n')
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(task_index, new_description):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_description + '\n'
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

def delete_task(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "3":
            task_index = int(input("Enter task index to update: "))
            new_description = input("Enter new task description: ")
            update_task(task_index, new_description)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main(