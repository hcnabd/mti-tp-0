# Part 1: 
coordinates = (10.5, 20.3)

print(coordinates)
print(coordinates[0])
print(coordinates[1])

coordinates[0] = 15.0 

# Part 2: 
person_info = ("Alice", 30, "New York")

name, age, city = person_info
print(name)
print(age)
print(city)

def get_min_max(numbers):
    return (min(numbers), max(numbers))

result = get_min_max([5, 1, 9, 2, 7])
print(result)

# Part 3:
students = [("Bob", 85), ("Charlie", 92), ("David", 78)]

for name, score in students:
    print(f"{name} scored {score}")
