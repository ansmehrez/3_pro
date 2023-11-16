from termcolor import colored
import random

def print_welcome_message():
    print(colored("Welcome to the todo list manager", 'green'))

def add_task(todo_list):
    new_task = input("Enter a task: ")
    todo_list.append(new_task)

def view_tasks(todo_list):
    if not todo_list:
        print("The list is empty")
    else:
        print("Tasks:")
        for task in todo_list:
            print(f"- {task}")

def remove_task(todo_list):
    if not todo_list:
        print("The list is empty")
    else:
        task_to_remove = input("Enter the task to remove: ")
        if task_to_remove in todo_list:
            todo_list.remove(task_to_remove)
            print("Task removed")
        else:
            print("Task not found in the todo list")

def main():
    todo_list = []

    while True:
        user_choice = input("Enter a command (add, view, remove, exit): ").lower()

        if user_choice == "add":
            add_task(todo_list)
        elif user_choice == "view":
            view_tasks(todo_list)
        elif user_choice == "remove":
            remove_task(todo_list)
        elif user_choice == "exit":
            print("Thanks for using the todo list manager!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    print_welcome_message()
    main()
