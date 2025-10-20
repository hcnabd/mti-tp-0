# Part 1:
student_profile = {
    "name": "Eve",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

print(student_profile)
print(student_profile["name"])
print(student_profile["major"])
print(student_profile["university"])  

# Part 2: 
student_profile["university"] = "Tech University"
student_profile["gpa"] = 3.9
del student_profile["age"]

for key in student_profile:
    print(key)

for value in student_profile.values():
    print(value)

for key, value in student_profile.items():
    print(key, value)
    
# Part 3:
library = {
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925},
    "1984": {"author": "George Orwell", "year": 1949}
}

print(library["1984"]["author"])

library["To Kill a Mockingbird"] = {"author": "Harper Lee", "year": 1960}

for title, details in library.items():
    print(title, "-", details["author"])
