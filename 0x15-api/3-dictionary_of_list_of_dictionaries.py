import requests
import json

def get_all_todos():
    """Fetches TODO list data for all employees.

    Returns:
        dict: A dictionary where keys are employee IDs and values are lists of tasks.
    """

    all_todos = {}
    for user_id in range(1, 11):  # Adjust the range based on the number of users
        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(url)
        data = response.json()
        all_todos[str(user_id)] = [{"username": todo.get("title"), "task": todo["title"], "completed": todo["completed"]} for todo in data]
    return all_todos

def export_to_json(data):
    """Exports the data to a JSON file.

    Args:
        data (dict): The data to be exported.
    """

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    all_todos_data = get_all_todos()
    export_to_json(all_todos_data)
    print("Data exported to todo_all_employees.json")
