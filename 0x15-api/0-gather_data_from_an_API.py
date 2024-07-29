#!/usr/bin/python3

import requests


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


def display_progress(data):
    """Displays the employee's TODO list progress in the specified format.

    Args:
        data (dict): The data retrieved from the API.
    """

    if not data:
        print("No data found for the provided employee ID.")
        return

    employee_name = data[0].get('title')  # Assuming 'title' field contains employee name
    num_done_tasks = sum(todo.get('completed', False) for todo in data)
    total_tasks = len(data)

    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for todo in data:
        if todo.get('completed', False):
            print(f"\t{todo.get('title')}")


if __name__ == "__main__":
    try:
        employee_id = int(input("Enter employee ID: "))
        data = get_todo_list_progress(employee_id)
        display_progress(data)
    except ValueError:
        print("Invalid employee ID. Please enter an integer.")
