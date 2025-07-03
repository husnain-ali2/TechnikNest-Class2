print("=== Marks Percentage Calculator ===")
subjects = ["Math", "Science", "English", "Social Studies", "Computer Science"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject} (out of 60): "))
    marks.append(mark)

total = sum(marks)
percentage = (total / 300) * 100

# Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "Fail"

print(f"\nTotal Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")