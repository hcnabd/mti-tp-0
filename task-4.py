# Part 1: 
score = float(input("Enter your score (0–100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

# Part 2: 
day_number = int(input("Enter a day number (1–7): "))

if day_number == 1:
    print("Saturday")
elif day_number == 2:
    print("Sunday")
elif day_number == 3:
    print("Monday")
elif day_number == 4:
    print("Tuesday")
elif day_number == 5:
    print("Wednesday")
elif day_number == 6:
    print("Thursday")
elif day_number == 7:
    print("Friday")
else:
    print("Please enter a number between 1 and 7!")