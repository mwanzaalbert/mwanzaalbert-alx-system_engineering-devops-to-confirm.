import requests
import json

def get_todo_list_progress(employee_id):
    """Fetches TODO list progress data from the API for the given employee ID.

    Args:
        employee_id (int): The ID of the employee whose progress is to be retrieved.

    Returns:
        dict: A dictionary containing employee information and TODO list progress,
              or None if the request fails.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the API request.
    """

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

    return response.json()

def export_to_json(data, employee_id):
    """Exports the employee's TODO list data to a JSON file.

    Args:
        data (dict): The data retrieved from the API.
        employee_id (int): The employee's ID.
    """

    json_data = {str(employee_id): []}
    for todo in data:
        json_data[str(employee_id)].append({
            "task": todo.get("title"),
            "completed": todo["completed"],
    
            # Assuming 'title' field contains username
            "username": todo.get("title")
        })

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

if __name__ == "__main__":
    try:
        employee_id = int(input("Enter employee ID: "))
        data = get_todo_list_progress(employee_id)
        export_to_json(data, employee_id)
        print(f"Data exported to {employee_id}.json")
    except ValueError:
        print("Invalid employee ID. Please enter an integer.")
