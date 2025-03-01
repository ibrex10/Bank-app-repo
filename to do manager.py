import os  # allow user to interact with the native pyhon operative system
import json  # use to store or transporting data
import sys #Allows exiting the program gracefully
from datetime import datetime # Used to track task creation and completion times

print("\nWELCOME TO TODO LIST MANAGER ")

#Defines a class TodoListManager that contains all functionalities for managing tasks.
class TodoListManager:


# asks user to input their name and stores it in self.user_name.
#Loads existing tasks from three files Active.txt, Completed.txt, Deleted.txt and It calls the load_tasks() method to read these files.
#Sets task_id_counter based on the number of active tasks. Each new task gets a unique ID
    def __init__(self):
        self.user_name: str = input("\nEnter your name to continue: ")
        self.active_tasks = self.load_tasks('Active.txt')
        self.completed_tasks = self.load_tasks('Completed.txt')
        self.deleted_tasks = self.load_tasks('Deleted.txt')
        self.task_id_counter = len(self.active_tasks) + 1
        self.main_menu() #Calls main_menu() to display the main menu and let the user interact with the app.


#Reads tasks from a file using JSON. If the file does not exist, it returns an empty list.
    def load_user_name(self):
        if os.path.exists('namesfile.txt'):
            with open('namesfile.txt', 'r') as file:
                return file.read().strip()
        else:
            name = input("Enter your name: ")
            with open('namesfile.txt', 'w') as file:
                file.write(name)
            return name


#Takes a filename and a task list. Writes the tasks into the file in JSON format.
    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

## Opens the file in write mode and # Saves the tasks list as a JSON file
    def save_tasks(self, filename, tasks):
        with open(filename, 'w') as file:
            json.dump(tasks, file)

#Greets the user with their name.
    def main_menu(self):
        print(f"""\nHello {self.user_name} , this is your Todo List manager. 

How may I help you today?""")

# Displays the main menu options. Loops forever (while True) until the user chooses exit.
        while True:
            print("\nMain Menu:")
            print("1. Add Task")
            print("2. View Active Tasks")
            print("3. View Completed Tasks")
            print("4. View Deleted Tasks")
            print("5. Edit Task Name")
            print("6. Mark Task as Completed")
            print("7. Delete Task")
            print("8. Exit")
# Calls handle_choice(choice) to execute the selected action.
            choice = input("Choose an option: ")
            self.handle_choice(choice)




#Checks which menu option was selected. and Calls the corresponding function for that action. else print invalid message
    def handle_choice(self, choice):
        if choice == '1':
            self.add_task()
        elif choice == '2':
            self.view_tasks(self.active_tasks, "Active Tasks")
        elif choice == '3':
            self.view_tasks(self.completed_tasks, "Completed Tasks")
        elif choice == '4':
            self.view_tasks(self.deleted_tasks, "Deleted Tasks")
        elif choice == '5':
            self.edit_task_name()
        elif choice == '6':
            self.mark_task_completed()
        elif choice == '7':
            self.delete_task()
        elif choice == '8':
            self.exit_program()
        else:
            print("Invalid option. Please try know what you are doing. Expected an integer number from 1 to 10")



# Asks the user to enter a task name. and Creates a dictionary storing task details.
#Adds the task to the list and increments the task counter.
    def add_task(self):
        task_name = input("Enter the task name: ")
        task = {
            "id": self.task_id_counter,
            "name": f"{task_name}",
            "time_created": f"{datetime.now().isoformat()}"
        }
        self.active_tasks.append(task)
        self.task_id_counter += 1
        print(f"{self.user_name}, your Task has added successfully.")


# Prints all tasks from a given list. and if the list is empty, prints "Task list Empty".
    def view_tasks(self, tasks, title):
        print(f"\n{title}:")
        for task in tasks:
            print(f"""
            ID: {task['id']}, 
            Name: {task['name']}, 
            Created: {task['time_created']}"""
                  )
        if tasks == 0:
            print("Task list empty")


# Shows active tasks and asks the user to enter a task ID, Finds the task and updates its name. if ID not exist print Task ID not found .
    def edit_task_name(self):
        self.view_tasks(self.active_tasks, "Active Tasks")
        task_id = int(input("Enter the task ID to edit: "))
        for task in self.active_tasks:
            if task['id'] == task_id:
                new_name = input("Enter the new task name: ")
                task['name'] = new_name
                print(f"{self.user_name}Task name updated successfully.")
                return
        print("Task ID not found.")


# Shows active tasks and asks for task ID, Moves the task from active.txt file to completed.txt.
    def mark_task_completed(self):
        self.view_tasks(self.active_tasks, "Active Tasks")
        task_id = int(input("Enter the task ID to mark as complete: "))
        for task in self.active_tasks:
            if task['id'] == task_id:
                task['time_finished'] = datetime.now().isoformat()
                self.completed_tasks.append(task)
                self.active_tasks.remove(task)
                print("Task marked has completed.")
                return
        print("Task ID not found.")


# Shows active tasks and asks for task ID, Moves the task from Completed.txt file to Delected.txt file.
    def delete_task(self):
        self.view_tasks(self.active_tasks, "Active Tasks")
        task_id = int(input("Enter the task ID to delete: "))
        for task in self.active_tasks:
            if task['id'] == task_id:
                self.deleted_tasks.append(task)
                self.active_tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task ID not found.")


# Saves all tasks before exiting and Displays a goodbye message and exits the program.
    def exit_program(self):
        self.save_tasks('Active.txt', self.active_tasks)
        self.save_tasks('Completed.txt', self.completed_tasks)
        self.save_tasks('Deleted.txt', self.deleted_tasks)
        print("\nYou have selected exit program")
        print(f"\nThanks {self.user_name}, All tasks are saved. and your program exit successfully  .")
        print(f"\nSo sad to see you go {self.user_name}. please visit again soon")
        print(f"\n \n \n@copy GROUP 3")
        sys.exit()


if __name__ == "__main__":
    TodoListManager()