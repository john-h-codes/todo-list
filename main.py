from menu import display_menu
from tasks import load_tasks, save_tasks, add_task, view_tasks, delete_task, mark_task_completed
def main():
    load_tasks()
    print('Welcome to the To-Do List App by John H!')
    while True:
        display_menu()

        select_option = int(input('>>>Select menu option: '))

        print('')
        if select_option == 1:
            print('** VIEW TASKS **')
            view_tasks()
        elif select_option == 2:
            add_task()
        elif select_option == 3:
            delete_task()
        elif select_option == 4:
            mark_task_completed()
        elif select_option == 5:
            print('Goodbye!')
            save_tasks()
            break
        else:
            print('Invalid choice. Please try again')

if __name__ == "__main__":
    main()
