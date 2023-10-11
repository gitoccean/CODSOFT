#                                ''' A To-Do List application is a useful project that helps users manage
#                                     and organize their tasks efficiently. This project aims to create a
#                                      command-line or GUI-based application using Python, allowing
#                                         users to create, update, and track their to-do lists  '''



task_list = []
task_id = 1

while True:
    print('''To-Do List Application
    Press 1 to add a task
    Press 2 to see task list
    Press 3 to mark a task as completed
    Press 4 to delete a task
    Press 5 to exit''')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task_name = str(input("Enter your task: "))
        task_priority = str(input("Enter task priority (High, Medium, Low): "))
        task_status = "not done"
        task = [task_id, task_name, task_priority, task_status]
        task_list.append(task)
        print(f"Your '{task[1]}' task has been added!")
        task_id += 1
    elif choice == 2:
        if not task_list:
            print("There are no tasks.")
        else:
            print("- Current Tasks -")
            for task in task_list:
                print(f"Id: {task[0]}, Task: {task[1]}, Priority: {task[2]}, Status: {task[3]}")
    elif choice == 3:
        mark_task = str(input("Enter the name of the task to mark as completed: "))
        task_found = False
        for task in task_list:
            if task[1] == mark_task:
                task[3] = "done"
                print("Task has been marked as completed.")
                task_found = True
                break
        if not task_found:
            print("No task found with that name.")
    elif choice == 4:
        name_del_task = str(input("Enter the task name you want to delete: "))
        task_found = False
        for task in task_list:
            if task[1] == name_del_task:
                task_list.remove(task)
                print(f"Your '{name_del_task}' task has been deleted.")
                task_found = True
                break
        if not task_found:
            print("No task found with that name.")
    elif choice == 5:
        print('Thanks for using our To-Do List app.')
        break
    else:
        print('Invalid input. Please choose from the given options.')
