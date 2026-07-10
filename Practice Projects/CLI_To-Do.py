def add_task(task):
    try:
        with open("DB.txt", "a") as file:  
            file.write(task + "\n")
        return "Task written successfully."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def remove_task(task):
    try:
        with open("DB.txt", "r") as file:  
            contents = file.readlines()

        updated_content = [content for content in contents if content.strip() != task]

        with open("DB.txt", "w") as file:  
            file.writelines(updated_content)
        
        if len(contents) == len(updated_content):
            return "Task not found."
        else:
            return "Task deleted successfully."

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def update_db(old_task, new_task):
    try:
        # Read all lines
        with open("DB.txt", "r") as file:
            lines = file.readlines()

        updated = False

        # Update matching lines
        updated_lines = []
        for line in lines:
            if line.strip() == old_task and not updated:
                updated_lines.append(new_task + "\n")
                updated = True
            else:
                updated_lines.append(line)

        with open("DB.txt", "w") as file:
            file.writelines(updated_lines)

        if updated:
            return "Task updated successfully."
        else:
            return "Task not found."

    except FileNotFoundError:
        return "File not found."
    except PermissionError:
        return "Permission denied."
    except Exception as e:
        return f"An error occurred: {e}"

def all_tasks():
    try:
        with open("DB.txt", "r") as file:
            content = file.readlines()
        
        if not content:
            print("No tasks found.")
        else:
            print("\n--- Tasks ---")
            for i, task in enumerate(content, 1):
                print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("File not found.")

def start_todo():
    try:
        while True:
            all_tasks()

            print("\nOptions:")
            print("1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                task = input("Enter new task: ").strip()
                if task:
                    add_task(task)
                else:
                    print("Task cannot be empty.")

            elif choice == "2":
                old_task = input("Enter task to update: ").strip()
                new_task = input("Enter new task: ").strip()
                if old_task and new_task:
                    print(update_db(old_task, new_task))
                else:
                    print("Invalid input.")

            elif choice == "3":
                task = input("Enter task to delete: ").strip()
                if task:
                    print(remove_task(task))
                else:
                    print("Invalid input.")

            elif choice == "4":
                print("Exiting TODO app.")
                break

            else:
                print("Invalid choice. Try again.")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")


choice = input("Do you want To-Do App?: ").strip().lower()
if choice == "yes":
    start_todo()

else:
    print("Thanks for using To-Do CLI")