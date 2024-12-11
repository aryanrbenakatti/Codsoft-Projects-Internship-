# To-Do List Application

## Overview
The To-Do List application is a simple yet powerful tool to help users manage and organize their tasks effectively. Built using Python, the application provides a command-line interface (CLI) that allows users to create, view, update, and track their to-do lists with ease. Tasks can be saved to a file for persistence and reloaded when the application restarts.

## Features

### Core Features
- **Add Tasks**: Create new tasks with optional descriptions and priorities.
- **View Tasks**: Display all tasks in a structured and readable format.
- **Update Tasks**: Edit task details, such as the title, description, and priority.
- **Delete Tasks**: Remove tasks from the list.
- **Mark as Completed**: Mark tasks as completed to track progress.
- **Save and Load**: Save tasks to a file (`tasks.json`) and load them later.

### Optional Features
- Task prioritization (Low, Medium, High).
- Graceful handling of missing or corrupted data files.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository or download the source code.
2. Ensure Python is installed and set up correctly on your machine.

### Running the Application
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `to_do_list.py` file.
3. Run the application:
   ```bash
   python to_do_list.py
   ```

## Usage

Upon running the application, a menu will appear with the following options:

```
To-Do List Application
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Completed
6. Save and Exit
```

### Menu Options
1. **Add Task**: Enter the task title, description (optional), and priority (Low, Medium, High).
2. **View Tasks**: Displays the list of all tasks, including their status, title, priority, and description.
3. **Update Task**: Modify an existing task's details.
4. **Delete Task**: Remove a task by its number.
5. **Mark Task as Completed**: Mark a specific task as completed.
6. **Save and Exit**: Save the tasks to `tasks.json` and exit the application.

## Example

### Sample Interaction
```plaintext
To-Do List Application
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Completed
6. Save and Exit
Choose an option: 1
Task Title: Buy groceries
Task Description: Milk, eggs, bread
Priority (Low/Medium/High): High
Task added successfully!

To-Do List Application
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Completed
6. Save and Exit
Choose an option: 2
1. Buy groceries [Pending] - High
   Description: Milk, eggs, bread
```

## File Structure
- `to_do_list.py`: Main Python script containing the application logic.
- `tasks.json`: JSON file where tasks are saved for persistence.

## How It Works
1. Tasks are stored in a list of dictionaries.
2. Data is saved and loaded using JSON for easy serialization and deserialization.
3. The application uses a menu-based system to interact with the user.

## Customization
You can extend this application by:
- Adding deadlines for tasks.
- Grouping tasks into categories.
- Integrating a GUI using libraries like `Tkinter` or `PyQt`.
- Replacing the JSON file with a database for better scalability.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

