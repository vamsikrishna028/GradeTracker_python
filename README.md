Name: Sykam Vamsi Krishna Company: CODTECH IT SOLUTIONS Intern ID:CT08DS312 Domain:Python Programming Mentor: Neela Santhosh Kumar Duration:December 5th, 2024 - January 5th, 2025
Overview
The Enhanced Student Grade Tracker is a Python program designed to help students and educators track academic performance. It allows users to input grades for different subjects, calculate individual subject GPAs, and compute the overall CGPA. The program also stores and displays grade records for multiple students, with options to view and clear records.

Features
Grade Input: Enter grades for multiple subjects for a student.
GPA Calculation: Calculate GPA for each subject based on the 10-point scale.
CGPA Calculation: Calculate the cumulative CGPA based on the student's grades.
Record Management: View, add, or clear student records.
Persistent Storage: Store student records in a student_grades.json file, making it available for future sessions.

output:
Welcome to the Enhanced Student Grade Tracker!
Options:
1. Enter grades for a new student
2. Clear a student's grades
3. View all student grades
4. View a specific student's grades
5. Exit
Please select an option (1-5): 1
Enter the student's name: vaamsi
How many subjects do you want to enter grades for vaamsi? 3
Enter the name of subject 1: dwm
Enter the grade for dwm (0-100): 89
Enter the name of subject 2: wan
Enter the grade for wan (0-100): 80
Enter the name of subject 3: flat
Enter the grade for flat (0-100): 78
------ Grade Report ------
dwm: 89.0 (GPA: 9.00)
wan: 80.0 (GPA: 9.00)
flat: 78.0 (GPA: 8.00)

CGPA: 8.67

Options:
1. Enter grades for a new student
2. Clear a student's grades
3. View all student grades
4. View a specific student's grades
5. Exit
Please select an option (1-5): 1
Enter the student's name: Abhiram
How many subjects do you want to enter grades for Abhiram? 3
Enter the name of subject 1: dwm
Enter the grade for dwm (0-100): 89
Enter the name of subject 2: wan
Enter the grade for wan (0-100): 78
Enter the name of subject 3: flat
Enter the grade for flat (0-100): 86

------ Grade Report ------
dwm: 89.0 (GPA: 9.00)
wan: 78.0 (GPA: 8.00)
flat: 86.0 (GPA: 9.00)

CGPA: 8.67

Options:
1. Enter grades for a new student
2. Clear a student's grades
3. View all student grades
4. View a specific student's grades
5. Exit
Please select an option (1-5): 4
Enter the student's name: Abhiram

Grades for Abhiram:
Subjects: ['dwm', 'wan', 'flat']
Grades: [89.0, 78.0, 86.0]
CGPA: 8.67

Options:
1. Enter grades for a new student
2. Clear a student's grades
3. View all student grades
4. View a specific student's grades
5. Exit
Please select an option (1-5): 3

------ Current Session Student Grades ------

Grades for vaamsi:
Subjects: ['dwm', 'wan', 'flat']
Grades: [89.0, 80.0, 78.0]
CGPA: 8.67

Grades for Abhiram:
Subjects: ['dwm', 'wan', 'flat']
Grades: [89.0, 78.0, 86.0]
CGPA: 8.67

Options:
1. Enter grades for a new student
2. Clear a student's grades
3. View all student grades
4. View a specific student's grades
5. Exit
Please select an option (1-5): 2
Enter the student's name whose records you want to clear: vaamsi
All records for vaamsi have been cleared.

Options:
1. Enter grades for a new student
2. Clear a student's grades
3. View all student grades
4. View a specific student's grades
5. Exit
Please select an option (1-5): 5
Thank you for using the Grade Tracker!
