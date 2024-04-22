from typing import Any

num: list[int] = [1, 2, 3, 4, 5]

letters: list[str] = ["a", "b", "c", "d", "e"]

people: list[dict[str, Any]] = [
    {"name": "Bob", "age": 23},
    {"name": "Aaron", "age": 32},
    {"name": "Sharon", "age": 40},
]

# add a new dictionary to the list
people.append({"name": "Sally", "age": 72})

for person in people:
    print(person["name"], person["age"])
