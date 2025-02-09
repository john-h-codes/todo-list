# Tasks list (in case no file exists)
tasks = []

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

# Function to view tasks
def view_tasks():
    index = 1
    if len(tasks) == 0:
        print('No tasks found')
    else:
        for task in tasks:
            print(f'\t{index}. {task}')
            index += 1
    print('')

# Function to add tasks to the list
def add_task():
    print('** ADD A TASK ** ')
    add_this_task = str(input('>>>Type a task to add to the list: '))
    tasks.append(add_this_task)
    print(f'Task "{add_this_task}" added to list')
    view_tasks()
    save_tasks()

# Function to delete tasks by index number
def delete_task():
    global tasks
    while True:
        print('** DELETE A TASK **')
        view_tasks()
        delete_this_task = input('>>>Select task number to delete: ')
        if delete_this_task.isdigit():
            task_index = int(delete_this_task) - 1
            if 0 <= task_index < len(tasks):
                print(f'"{tasks[task_index]}" deleted from task list')
                tasks.pop(task_index)
                view_tasks()
                save_tasks()
                break  # Exit if successful
            else:
                print(f'Invalid task number. Please enter a number between 1 and {len(tasks)}.')
        else:
            print('Invalid input. Please enter a valid number.')

# Function to mark task as completed
def mark_task_completed():
    global tasks
    while True:
        print('** MARK A TASK AS COMPLETED **')
        view_tasks()
        completed_task = input('>>>Select completed task #: ')
        if completed_task.isdigit():
            task_index = int(completed_task) - 1
            if 0 <= task_index < len(tasks):
                print(f'"{tasks[task_index]}" marked as "Completed"')
                tasks[task_index] = f'{tasks[task_index]} (Completed)'
                save_tasks()
                view_tasks()
                break
            else:
                print(f'Invalid task number. Please enter a number between 1 and {len(tasks)}')
        else:
            print('Invalid input. Please enter a valid number.')

