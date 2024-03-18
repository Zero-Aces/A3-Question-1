# main.py
from student_operations import fetch_all_students, insert_student, modify_student_email, remove_student
from datetime import datetime

def main():
    while True:  # Main loop for user interaction
        # Display menu options
        print("\nStudent Records Management System")
        print("1. Display All Students")
        print("2. Add New Student")
        print("3. Update Student Email")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':  # Display all students
            print("\nAll student records:")
            fetch_all_students()

        elif choice == '2':  # Add new student
            print("\nAdd New Student:")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date_str = input("Enter enrollment date (YYYY-MM-DD): ")
            try:
                enrollment_date = datetime.strptime(enrollment_date_str, "%Y-%m-%d").date()  # Parse date input
                insert_student(first_name, last_name, email, enrollment_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")  # Handle invalid date format

        elif choice == '3':  # Update student email
            print("\nUpdate Student Email:")
            try:
                student_id = int(input("Enter student ID to update: "))  # Parse student ID
                new_email = input("Enter new email: ")
                modify_student_email(student_id, new_email)
            except ValueError:
                print("Invalid student ID. Please enter a numerical value.")  # Handle non-integer ID input

        elif choice == '4':  # Delete student
            print("\nDelete Student:")
            try:
                student_id = int(input("Enter student ID to delete: "))  # Parse student ID
                remove_student(student_id)
            except ValueError:
                print("Invalid student ID. Please enter a numerical value.")  # Handle non-integer ID input

        elif choice == '5':  # Exit program
            print("Exiting the program. Goodbye!")
            break

        else:  # Handle invalid menu option
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
