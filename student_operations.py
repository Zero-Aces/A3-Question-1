# student_operations.py
from db_connection import get_database_connection

def fetch_all_students():
    with get_database_connection() as connection:  # Establish DB connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students;")  # Fetch all student records
            students = cursor.fetchall()  # Retrieve all rows
            for student in students:
                formatted_date = student[4].strftime("%Y-%m-%d")  # Format date
                formatted_student = student[:4] + (formatted_date,)  # Combine with other student info
                print(formatted_student)  # Print formatted student record

def insert_student(first_name, last_name, email, enrollment_date):
    with get_database_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT email FROM students WHERE email = %s;", (email,))  # Check for existing email
            if cursor.fetchone():
                print("Email already exists. Please use a different email.")  # Notify if email exists
                return
            # Insert new student record
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                           (first_name, last_name, email, enrollment_date))
            connection.commit()  # Commit changes

def modify_student_email(student_id, new_email):
    with get_database_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT email FROM students WHERE email = %s;", (new_email,))  # Check new email
            if cursor.fetchone():
                print("New email already in use. Please select another email.")  # Notify if new email exists
                return
            # Update student email
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
            connection.commit()  # Commit changes

def remove_student(student_id):
    with get_database_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))  # Delete student
            connection.commit()  # Commit changes
