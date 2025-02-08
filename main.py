# Tasks list (in case no file exists)
tasks = []

# Function to display a menu
def display_menu():
    print('To-Do List Application')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Delete Task')
    print('4. Mark Task Completed')
    print('5. Exit')

# Function to view tasks
def view_tasks():
    index = 1
    if len(tasks) == 0:
        print('No tasks found')
    else:
        for task in tasks:
            print(index,'.', task)
            index += 1

# Function to add tasks to the list
def add_task():
    add_this_task = str(input('Type a task to add to the list: '))
    tasks.append(add_this_task)
    print(f'Task "{add_this_task}" added to list')
    view_tasks()
    save_tasks()

# Function to delete tasks by index number
def delete_task():
    global tasks
    view_tasks()
    delete_this_task = int(input('Select task number to delete: '))
    task_index = delete_this_task - 1
    if task_index > len(tasks):
        print('Invalid task number')
    else:
        print(f'"{tasks[task_index]}" deleted from task list')
        tasks.pop(task_index)
        view_tasks()
        save_tasks()

def mark_task_completed():
    global tasks
    view_tasks()
    completed_task = int(input('Select completed task #: '))
    task_index = completed_task - 1
    if task_index > len(tasks):
        print('Invalid task number')
    else:
        print(f'"{tasks[task_index]}" marked as "Completed"')
        tasks[task_index] = f'{tasks[task_index]} (Completed)'
        save_tasks()
    view_tasks()
# Function to create a local .txt file to save tasks
def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    print('tasks.txt updated.')

# Function to load tasks from file (if it already exists)
def load_tasks():
    global tasks
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []

def main():
    load_tasks()
    while True:
        display_menu()

        select_option = int(input('Select menu option (number): '))

        if select_option == 1:
            view_tasks()
        elif select_option == 2:
            add_task()
        elif select_option == 3:
            delete_task()
        elif select_option == 4:
            mark_task_completed()
        elif select_option == 5:
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again')

main()
