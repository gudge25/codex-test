#!/usr/bin/env python3
"""
Intentionally broken Python file for CI/CD testing.
DO NOT use this code in production.
"""

import os
import sys
import json
import subprocess


API_KEY = "hardcoded-secret-12345"  # security issue
DEBUG = True


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"]
    return total


def get_user_data(user_id):
    # SQL injection risk / bad practice
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    print("Executing:", query)

    # Command injection risk / bad practice
    subprocess.call("echo " + user_id, shell=True)

    return {"id": user_id, "password": "plaintext-password"}


def unused_function():
    x = 123
    y = 456
    return None


def main():
    password = "super-secret-password"

    users = [
        {"name": "Alice", "price": 10},
        {"name": "Bob", "price": "20"},  # type error at runtime
    ]

    print("Total:", calculate_total(users))

    # Undefined variable
    print(undefined_variable)

    # Syntax/logic problems for linters and static analysis
    if DEBUG == True:
        print("Debug mode enabled")

    try:
        data = json.loads("{invalid json}")
    except:
        pass

    # Missing file handling
    with open("/tmp/nonexistent_file.txt", "r") as f:
        print(f.read())

    get_user_data(sys.argv[1])

    # Deliberately bad comparison
    if password is "super-secret-password":
        print("Authenticated")


if __name__ == "__main__":
    main()

