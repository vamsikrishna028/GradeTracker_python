import json

# Function to calculate GPA based on grade (on a 10-point scale)
def calculate_gpa(grade):
    if grade >= 90:
        return 10.0
    elif grade >= 80:
        return 9.0
    elif grade >= 70:
        return 8.0
    elif grade >= 60:
        return 7.0
    else:
        return 0.0

# Function to save the current session's records to a file
def save_records(records):
    with open('student_grades.json', 'w') as file:
        json.dump(records, file, indent=4)

# Function to load past records
def load_records():
    try:
        with open('student_grades.json', 'r') as file:
            records = json.load(file)
    except FileNotFoundError:
        records = {}
    return records

# Function to input grades for a student
def input_grades(student_name):
    subjects = []
    grades = []
    
    num_subjects = int(input(f"How many subjects do you want to enter grades for {student_name}? "))

    for i in range(num_subjects):
        subject = input(f"Enter the name of subject {i+1}: ")

        # Loop until a valid grade is entered (between 0 and 100)
        while True:
            try:
                grade = float(input(f"Enter the grade for {subject} (0-100): "))
                if 0 <= grade <= 100:  # Validate grade is between 0 and 100
                    break
                else:
                    print("Invalid input! Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numerical grade.")

        subjects.append(subject)
        grades.append(grade)

    # Calculate the GPAs for each subject
    gpas = [calculate_gpa(grade) for grade in grades]

    # Calculate the CGPA by averaging the individual subject GPAs
    cgpa = sum(gpas) / len(gpas) if len(gpas) > 0 else 0.0

    # Display grade report
    print("\n------ Grade Report ------")
    for i in range(num_subjects):
        print(f"{subjects[i]}: {grades[i]} (GPA: {gpas[i]:.2f})")

    print(f"\nCGPA: {cgpa:.2f}")

    # Ensure the 'CGPA' key is included in the returned student record
    return {
        "Subjects": subjects,
        "Grades": grades,
        "CGPA": cgpa
    }

# Function to clear a specific student's records
def clear_student_record(records, student_name):
    if student_name in records:
        del records[student_name]
        print(f"All records for {student_name} have been cleared.")
    else:
        print(f"No records found for {student_name}.")

# Main function to handle grade entry and CGPA calculation
def main():
    print("Welcome to the Enhanced Student Grade Tracker!")
    
    # Load past records
    records = load_records()

    # This will store only the current session's data (separate from the past records)
    current_session_records = {}

    while True:
        print("\nOptions:")
        print("1. Enter grades for a new student")
        print("2. Clear a student's grades")
        print("3. View all student grades")
        print("4. View a specific student's grades")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ").strip()

        if choice == '1':
            # Get student name
            student_name = input("Enter the student's name: ")

            # Input grades for the student
            student_record = input_grades(student_name)

            # Store the current session's record
            current_session_records[student_name] = student_record

            # Save current session's records
            save_records(current_session_records)

        elif choice == '2':
            student_name = input("Enter the student's name whose records you want to clear: ")
            clear_student_record(current_session_records, student_name)
            # Save updated records after clearing
            save_records(current_session_records)

        elif choice == '3':
            # Show all student grades for the current session
            print("\n------ Current Session Student Grades ------")
            for student, student_records in current_session_records.items():
                print(f"\nGrades for {student}:")
                print(f"Subjects: {student_records['Subjects']}")
                print(f"Grades: {student_records['Grades']}")
                print(f"CGPA: {student_records['CGPA']:.2f}")

        elif choice == '4':
            # Option to view grades for a specific student
            student_name = input("Enter the student's name: ")
            if student_name in current_session_records:
                print(f"\nGrades for {student_name}:")
                record = current_session_records[student_name]
                print(f"Subjects: {record['Subjects']}")
                print(f"Grades: {record['Grades']}")
                print(f"CGPA: {record['CGPA']:.2f}")
            else:
                print("No records found for that student.")
        
        elif choice == '5':
            print("Thank you for using the Grade Tracker!")
            break
        else:
            print("Invalid option! Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
