todolist = []

while True:
    user_choice = input("Enter a command (add, view, remove, exit): ")

    if user_choice == "add":
        new_task = input("Enter a task: ")
        todolist.append(new_task)

    elif user_choice == "view":
        if not todolist:
            print("The list is empty")
        else:
            print(todolist)

    elif user_choice == "remove":
        if not todolist:
            print("The list is empty")
        else:
            task_to_remove = input("Enter the task to remove: ")
            if task_to_remove in todolist:
                todolist.remove(task_to_remove)
                print("Task removed")
            else:
                print("the task is not find in the todo list")

    elif user_choice == "exit":
        break

    else:
        print("Invalid command")

