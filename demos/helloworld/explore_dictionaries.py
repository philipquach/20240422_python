person = {"first_name": "Bob", "last_name": "Smith", "age": 23}

person["first_name"]
person["last_name"]
person["age"]

print(person)

person["hair_color"] = "brown"

for key in person:
    print(key, person[key])

try:
    print(person["middle_name"])
except KeyError:
    print("KeyError: middle_name")

# safely access a key that may not exist
print(person.get("middle_name"))

del person["hair_color"]
