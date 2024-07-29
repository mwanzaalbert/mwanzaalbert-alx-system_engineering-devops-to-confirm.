#!/usr/bin/python3
"""
Fetches and exports all employees' TODO list progress to a JSON file.
"""
import json
import requests

def fetch_todo_list():
    """Fetches todo list from the API and saves it to todo_all_employees.json."""
    # API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch users and todos data
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    # Prepare data for JSON output
    todo_dict = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_todos = [todo for todo in todos if todo['userId'] == user_id]
        todo_dict[user_id] = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            } for todo in user_todos
        ]

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_dict, json_file)

if __name__ == "__main__":
    fetch_todo_list()