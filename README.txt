# Student Records Management System

## Overview

This application allows users to manage student records in a PostgreSQL database through a simple command-line interface. 
It supports Create, Read, Update, and Delete (CRUD) operations on student records.


YOUTUBE LINK:
https://youtu.be/U3ZWTaEAWrY


## Prerequisites

- Python 3.x
- PostgreSQL (pgAdmin)
- psycopg2 Python library

## Setup Instructions

### Database Setup

1. Ensure PostgreSQL is installed and running on your system.
2. Create a new database named `Tester`.
3. Import the initial schema and data:
    - Navigate to pgAdmin4
    - Right Click Databses Located Under Serves on the left hand side.
    - Click Create -> Database
    - Name it 'Tester'
    - Click 'Save'
4. Right Click the database we just created called Tester  
5. Click Query Tool
6. import the file by clicking the file icon. 

### Application Setup

1. Download the source code to your local machine.
2. Install the required Python package (psycopg2) by running:
    
    pip install psycopg2-binary
    
    or
    
    pip install psycopg2      <-- this should work for most
    
    depending on your system.

### Configuration

1. Open `db_connection.py` in a text editor.
2. Update the `get_database_connection` function with your PostgreSQL credentials:
    ```python
    connection = psycopg2.connect(
        dbname='Tester', 
        user='your_username', 
        password='your_password', 
        host='localhost'
    )
    ```

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing the application files.
3. Run the application with the command:
    ```
    python main.py
    ```
4. Follow the on-screen prompts to manage student records.

## Features

- **Display All Students**: List all student records in the database.
- **Add New Student**: Insert a new student record into the database. Duplicate emails are not allowed.
- **Update Student Email**: Update the email address for a specific student by their ID.
- **Delete Student**: Remove a student record from the database by their ID.

## Exiting the Program

- To exit the application, choose option `5` from the main menu.
