# Database Management System (DBMS) for Student Records

This Python script facilitates basic management operations on a PostgreSQL database containing student records. It allows users to perform the following actions:

1. **Get all students**: Retrieve and display all student records from the database.
2. **Add a new student**: Insert a new student record into the database.
3. **Update a student's email**: Modify the email address of a student in the database.
4. **Delete a student**: Remove a student record from the database.
5. **Reset the database to default**: Clear all existing records and initialize the database with default data.

## Requirements

- Python 3.x
- psycopg2 (Python PostgreSQL database adapter)
- PostgreSQL

## Installation

1. Clone or download this repository to your local machine.
2. Ensure Python 3.x and PostgreSQL are installed.
3. Install the psycopg2 library using pip:

   ```
   pip install psycopg2
   ```

## Configuration

- Modify the database connection parameters in the `connect()` function to match your PostgreSQL database configuration (database name, user, host, password, port).

## Usage

1. Run the script `main.py`.
2. Follow the on-screen prompts to select the desired operation.

## Notes

- Make sure to handle sensitive database credentials securely.
- Use caution when resetting the database, as it will delete all existing records.
