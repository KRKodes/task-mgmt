from cs50 import SQL
from datetime import datetime

db = SQL("sqlite:///tasks.db")

def main():
    while True:
        print("Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Search Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            message = add_task()
            print(message)
        elif choice == "2":
            tasks = view_tasks()
            if isinstance(tasks, str):
                print(tasks)
            else:
                for task in tasks:
                    print(task)
        elif choice == "3":
            message = update_task()
            print(message)
        elif choice == "4":
            tasks = search_tasks()
            if isinstance(tasks, str):
                print(tasks)
            else:
                for task in tasks:
                    print(task)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Choose a number.")

def add_task():
    title = input("Enter task title: ")
    try:
        results = db.execute("SELECT title FROM tasks")
        for row in results:
            if row['title'] == title:
                return "Title already exists."
    except Exception as e:
        return f"An error occurred: {e}"

    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    completed = input("Is the task completed? (yes/no): ")
    if completed.lower() not in ['yes', 'no']:
        return "Invalid input for completion status. Please enter 'yes' or 'no'."

    category = input("Enter category: ")
    try:
        db.execute("INSERT INTO tasks (title, description, due_date, completed, category) VALUES (?, ?, ?, ?, ?)", title, description, due_date, completed.lower() == 'yes', category)
        return "Task added successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

def update_task():
    identifier_type = input("Would you like to identify the task by (1) ID or (2) Title? ")

    if identifier_type == "1":
        task_id = input("Enter task ID: ")
    elif identifier_type == "2":
        task_title = input("Enter task title: ")
    else:
        return "Invalid choice."

    title = input("Enter new task title: ")
    description = input("Enter new task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    completed = input("Is the task completed? (yes/no): ")
    if completed.lower() not in ['yes', 'no']:
        return "Invalid input for completion status. Please enter 'yes' or 'no'."

    category = input("Enter new category: ")

    try:
        if identifier_type == "1":
            db.execute("UPDATE tasks SET title = ?, description = ?, due_date = ?, completed = ?, category = ? WHERE id = ?",
                       title, description, due_date, completed.lower() == 'yes', category, task_id)
        elif identifier_type == "2":
            db.execute("UPDATE tasks SET title = ?, description = ?, due_date = ?, completed = ?, category = ? WHERE title = ?",
                       title, description, due_date, completed.lower() == 'yes', category, task_title)
        return "Task updated successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

def view_tasks():
    print("Sort by:")
    print("1. ID (numerically)")
    print("2. Title (A-Z)")
    print("3. Title (Z-A)")
    print("4. Date (oldest to newest)")
    print("5. Date (newest to oldest)")

    choice = input("Choose an option: ")

    sort_query = "SELECT * FROM tasks"

    if choice == "1":
        sort_query += " ORDER BY id"
    elif choice == "2":
        sort_query += " ORDER BY LOWER(title) ASC"
    elif choice == "3":
        sort_query += " ORDER BY LOWER(title) DESC"
    elif choice == "4":
        sort_query += " ORDER BY due_date DESC"
    elif choice == "5":
        sort_query += " ORDER BY due_date ASC"
    else:
        return "Invalid choice. Displaying unsorted tasks."

    try:
        print(f"Executing query: {sort_query}")
        result = db.execute(sort_query)
        print(f"Query result: {result}")
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"

def search_tasks():
    searchby = input("Would you like to search the task by (1) category, (2) completion, or (3) due date? ")

    if searchby == "1":
        task_cat = input("Enter task category: ")
        try:
            result = db.execute("SELECT * FROM tasks WHERE category = ?", task_cat)
            print("Search Results")
            return result
        except Exception as e:
            return f"An error occurred: {e}"
    elif searchby == "2":
        task_status = input("Enter task completion status (yes/no): ")
        if task_status.lower() not in ['yes', 'no']:
            return "Invalid input for completion status. Please enter 'yes' or 'no'."
        try:
            result = db.execute("SELECT * FROM tasks WHERE completed = ?", task_status.lower() == 'yes')
            print("Search Results")
            return result
        except Exception as e:
            return f"An error occurred: {e}"
    elif searchby == "3":
        task_date = input("Enter task date (YYYY-MM-DD): ")
        try:
            datetime.strptime(task_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."
        try:
            result = db.execute("SELECT * FROM tasks WHERE due_date = ?", (task_date,))
            print("Search Results")
            return result
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        return "Invalid choice."

if __name__ == "__main__":
    main()
