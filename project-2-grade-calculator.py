# Semester 1 – Project 2 - Grade Calculator with Menu
# LMS project link: https://elms.eng.ruh.ac.lk/mod/page/view.php?id=358
# Thisal Kenula
# 2025-07-26

import pandas as pd

# Get student name
std_name = input("Enter student name: ")

# Get number of subjects
while True:
    try:
        no_of_subjects = int(input("Enter number of subjects: "))
    except ValueError:
        print("Please enter a positive integer")
    else:
        break

# Get marks for each subject
all_marks = [0 for i in range(no_of_subjects)] # List to store all marks

for i in range(no_of_subjects):
    while True:
        try:
            marks = float(input(f"Enter marks for subject {i+1}: "))
        except ValueError:
            print("Marks should be a number")
        else:
            all_marks[i] = marks
            break

# Get credits for each subject
all_credits = [0 for i in range(no_of_subjects)] # List to store all credits
for i in range(no_of_subjects):
    while True:
        try:
            credits = float(input(f"Enter total credits for subject {i+1}: "))
        except ValueError:
            print("Credits should be a number")
        else:
            all_credits[i] = credits
            break

# Generate grades for each subject
grades = ['' for i in range(no_of_subjects)] # List to store grades

for i, mark in enumerate(all_marks):
    grade = 'F'
    if mark >= 85:
        grade = 'A'
    elif mark >= 70:
        grade = 'B'
    elif mark >= 50:
        grade = 'C'
    grades[i] = grade

# Calculate GPAs
GPAs = [0 for i in range(no_of_subjects)] # Store GPAs for each subjects
for i, grade in enumerate(grades):
    if grade == 'A':
        GPAs[i] = 4.0
    elif grade == 'B':
        GPAs[i] = 3.0
    elif grade == 'C':
        GPAs[i] = 2.0

# Calcluate SGPA
for i in range(no_of_subjects):
    GPA_sum = sum([GPAs[i]*all_credits[i] for i in range(no_of_subjects)])
    SGPA = GPA_sum/sum(all_credits)

# Output results
print("---")
print(f"Results of {std_name}")

data = {
    "Credits": all_credits,
    "Marks": all_marks,
    "Grade": grades,
    "GPA": GPAs
}

df = pd.DataFrame(data)

print(df)

print(f"SGPA = {SGPA}")
print(f"Max marks = {max(all_marks)}")
print("---")



