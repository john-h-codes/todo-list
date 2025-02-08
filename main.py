# global variable for tasks list
tasks = ['clean bathroom', 'take out trash', 'finish coding']

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
    global tasks
    add_this_task = str(input('Type a task to add to the list: '))
    tasks.append(add_this_task)
    print(f'Task "{add_this_task}" added to list')
    view_tasks()

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

def mark_task_completed():
    completed_task = int(input('Select completed task #: '))
    task_index = completed_task - 1
    if task_index > len(tasks):
        print('Invalid task number')
    else:
        print(f'"{tasks[task_index]}" marked as "Completed"')
        tasks[task_index] = f'{tasks[task_index]} (Completed)'
    view_tasks()

def main():
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
