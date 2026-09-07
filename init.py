#!/usr/bin/env python3
"""
Previously-broken Python file, now fixed for CI/CD testing purposes.
"""

import os
import sys
import json
import subprocess


API_KEY = os.environ.get("API_KEY", "")
DEBUG = True


def calculate_total(items):
    total = 0
    for item in items:
        total += float(item["price"])
    return total


def get_user_data(user_id):
    # Parameterized query instead of string interpolation
    query = "SELECT * FROM users WHERE id = %s"
    print("Executing:", query, "with params:", (user_id,))

    # No shell=True, argument passed as a list to avoid command injection
    subprocess.call(["echo", user_id])

    return {"id": user_id, "password": os.environ.get("USER_PASSWORD", "")}


def main():
    password = os.environ.get("APP_PASSWORD", "")

    users = [
        {"name": "Alice", "price": 10},
        {"name": "Bob", "price": "20"},
    ]

    print("Total:", calculate_total(users))

    if DEBUG:
        print("Debug mode enabled")

    try:
        data = json.loads("{invalid json}")
    except json.JSONDecodeError as exc:
        print("Failed to parse JSON:", exc)

    file_path = "/tmp/nonexistent_file.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            print(f.read())
    else:
        print(f"File not found: {file_path}")

    if len(sys.argv) > 1:
        get_user_data(sys.argv[1])
    else:
        print("Usage: init.py <user_id>")

    if password == "correct-password":
        print("Authenticated")


if __name__ == "__main__":
    main()
