student_scores = [85, 92, 78, 95, 88]

score = int(input("Enter a score to search for: "))

if score in student_scores:
    print("Score found at index:", student_scores.index(score))
else:
    print("Score not found.")

student_scores[2] = 80
print(student_scores)