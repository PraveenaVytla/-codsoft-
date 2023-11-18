tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

def display_tasks():
    if not tasks:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' has been removed from the to-do list.")
    else:
        print("Invalid task index.")
while True:
    print("\nOptions: \n1. Add a task\n2. Display tasks\n3. Remove a task\n4. Quit")
    ch = input("Enter your choice: ")

    if ch == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif ch == '2':
        display_tasks()
    elif ch == '3':
        display_tasks()
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif ch == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")