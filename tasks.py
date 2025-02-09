# Tasks list (in case no file exists)
tasks = []
# Function to view tasks
def view_tasks():
    index = 1
    if len(tasks) == 0:
        print('No tasks found')
    else:
        for task in tasks:
            print(f'{index}. {task}')
            index += 1

# Function to add tasks to the list
def add_task():
    add_this_task = str(input('\tType a task to add to the list: '))
    tasks.append(add_this_task)
    print(f'*** Task "{add_this_task}" added to list ***')
    view_tasks()
    save_tasks()

# Function to delete tasks by index number
def delete_task():
    global tasks
    view_tasks()
    delete_this_task = int(input('\tSelect task number to delete: '))
    task_index = delete_this_task - 1
    if task_index > len(tasks):
        print('Invalid task number')
    else:
        print(f'*** "{tasks[task_index]}" deleted from task list ***')
        tasks.pop(task_index)
        view_tasks()
        save_tasks()

def mark_task_completed():
    global tasks
    view_tasks()
    completed_task = int(input('\tSelect completed task #: '))
    task_index = completed_task - 1
    if task_index > len(tasks):
        print('Invalid task number')
    else:
        print(f'***"{tasks[task_index]}" marked as "Completed"***')
        tasks[task_index] = f'{tasks[task_index]} (Completed)'
        save_tasks()
    view_tasks()
# Function to create a local .txt file to save tasks
def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    print('*** tasks.txt file updated ***')

# Function to load tasks from file (if it already exists)
def load_tasks():
    global tasks
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []