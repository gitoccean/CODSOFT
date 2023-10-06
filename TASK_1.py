#                                ''' A To-Do List application is a useful project that helps users manage
#                                     and organize their tasks efficiently. This project aims to create a
#                                      command-line or GUI-based application using Python, allowing
#                                         users to create, update, and track their to-do lists  '''



task_list = []
task_id = 1
while True:
    print('''  To-Do List Application
press 1 to add a task
press 2 to see tasks list
press 3 to update by mark task as completed
press 4 to delete your task
press 5 to exist''')
    choice = int(input("Enter your Choice:  "))
    if choice == 1:
        task_name = str(input("Enter your task:  "))
        task_priority = str(input("Enter task priority (High,Medium,low):"))
        task_status = "not done"
        task = (task_id,task_name, task_priority, task_status)
        task_list.append(task)
        print(f"Your {task[1]} task added!")
        task_id += 1
    elif choice == 2:
        if not task_list:
            print("there is no task")
        else:
            print("-current tasks-")
            for task in task_list:
                print(f"Id: {task[0]},Task:{task[1]}, priority:{task[2]}, Status:{task[3]},")
    elif choice == 3:
        mark_task = str(input("Enter the name of task to mark as completed:  "))
        update_task = []
        task_found = False
        for task in task_list:
            if task[1] == mark_task:
                task[1] = "done"
                print(f"Task has been Marked")
                task_found = True
            else:
                print("There is no such task")
            update_task.append(task)
        task_list = update_task
    elif choice == 4:
        name_del_task = str(input("Enter the task name you want to delete:  "))
        task_del = False
        for task in task_list:
            if task[1] == name_del_task:
                task_list.remove(task)
                print(f"Your task has been deleted")
                task_del = True
            else:
                print("there is no such task")
    elif choice == 5:
        print('Thanks for using our To-Do List app....')
        break
    else:
        print('Invalid Input please choose from given functions')
