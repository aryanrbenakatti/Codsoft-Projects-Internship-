import json

# Task Manager Class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", priority="Low"):
        task = {
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False,
        }
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['title']} [{status}] - {task['priority']}")
                if task["description"]:
                    print(f"   Description: {task['description']}")

    def update_task(self, index, title=None, description=None, priority=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if priority:
                task["priority"] = priority
            print("Task updated successfully!")
        else:
            print("Invalid task index!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index!")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task index!")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(self.tasks, f)
        print("Tasks saved successfully!")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                self.tasks = json.load(f)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found.")

# Main Function
def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description (optional): ")
            priority = input("Priority (Low/Medium/High): ")
            manager.add_task(title, description, priority)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.view_tasks()
            index = int(input("Task number to update: ")) - 1
            title = input("New Title (leave blank to keep current): ")
            description = input("New Description (leave blank to keep current): ")
            priority = input("New Priority (leave blank to keep current): ")
            manager.update_task(index, title, description, priority)
        elif choice == "4":
            manager.view_tasks()
            index = int(input("Task number to delete: ")) - 1
            manager.delete_task(index)
        elif choice == "5":
            manager.view_tasks()
            index = int(input("Task number to mark as completed: ")) - 1
            manager.mark_completed(index)
        elif choice == "6":
            manager.save_tasks()
            break
        else:
            print("Invalid option, please try again!")

if __name__ == "__main__":
    main()
