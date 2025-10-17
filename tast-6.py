# Part 1: 
total = 0      
count = 0

number = int(input("Enter an integer: "))

while number != 0:
    total += number
    count += 1
    number = int(input("Enter another integer: "))

if count > 0:
    average = total / count
    print("Average of the entered numbers: ", average)
else:
    print("Wshbik have some fun (-_-;)")
    
# Part 2: 
while True:
    number = int(input("Enter a number: "))
    if number > 0:
        print(f"{number} is a positive number!")
        break
    else:
        print("That’s a negative number!")