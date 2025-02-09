Basic TO-DO list application
This console-based To-Do list application has 5 functions:
  1. View List - lets you know if there is nothing on the list
  2. Add Task - Prompts user to type a task to add to the list, automatically saves item to "tasks.txt"
  3. Delete Task - prompts user to enter task number to remove from list,
       only accepts integers ranging from 1 to len(task_list) with automatic handling for converting an input of '1' to '0'
  4. Mark Task as Completed - prompts user to enter task number to mark as '(Completed)'
       has the same rules as "Delete Task" function (wont allow invalid entries)
  5. Exit Program - (Duh)

The only real upgrade over the most basic task manager is that the tasks are saved to a .txt file that is automatically referenced each time the program is opened, allowing the user to close the program without losing the task list.
To practice creating more "professional" programs, the program is split into 3 separate .py files ('main', 'menu', and 'tasks').
