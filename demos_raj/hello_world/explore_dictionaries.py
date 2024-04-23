person = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 23,
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])

print(person)

person["age"] = 99

person["hair_color"] = "brown"

print(person)

try:
    print(person["non-existant-key"])
except KeyError:
    print("!! KeyError !!")

# default value for non existant key
print(person.get("middle_name", "Key does not exist!"))

del person["hair_color"]

# garbage collection
person = None
