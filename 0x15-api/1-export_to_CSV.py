import requests
import csv


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


def export_to_csv(data, employee_id):
    """Exports the employee's TODO list data to a CSV file.

    Args:
        data (dict): The data retrieved from the API.
        employee_id (int): The employee's ID.
    """

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": todo.get("title"),  # Assuming 'title' field contains username
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"]
            })


if __name__ == "__main__":
    try:
        employee_id = int(input("Enter employee ID: "))
        data = get_todo_list_progress(employee_id)
        export_to_csv(data, employee_id)
        print(f"Data exported to {employee_id}.csv")
    except ValueError:
        print("Invalid employee ID. Please enter an integer.")
