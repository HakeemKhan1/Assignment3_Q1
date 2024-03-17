import psycopg2
# Connect to the database
def connect():
    try:
        conn = psycopg2.connect(
            database="Assignment3_Q1",
            user="postgres",
            host='localhost',
            password="postgres",
            port=5432)

        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)

# Function to retrieve all students
def getAllStudents():
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            formatted_date = student[4].strftime('%Y-%m-%d')
            print(
                f" {student[0]},  {student[1]},  {student[2]},  {student[3]},  {formatted_date}")
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error retrieving students:", e)

# Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, enrollment_date))
        conn.commit()
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error adding student:", e)

# Function to update students email

def updateStudentEmail(student_id, new_email):
    conn = connect()
    try:
        cursor = conn.cursor()
        # Check if the student exists
        cursor.execute("SELECT 1 FROM students WHERE student_id = %s", (student_id,))
        if not cursor.fetchone():
            raise ValueError("Student with ID {} does not exist.".format(student_id))
        # Update the email
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                       (new_email, student_id))
        conn.commit()
        print("Student email updated successfully.")
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error updating student email:", e)
# Function to delete a student

def deleteStudent(student_id):
    conn = connect()
    try:
        cursor = conn.cursor()
        # Check if the student exists
        cursor.execute("SELECT 1 FROM students WHERE student_id = %s", (student_id,))
        if not cursor.fetchone():
            raise ValueError("Student with ID {} does not exist.".format(student_id))
        # Delete the student
        cursor.execute("DELETE FROM students WHERE student_id = %s",
                       (student_id,))
        conn.commit()
        print("Student deleted successfully.")
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error deleting student:", e)

# Function to reset the database to default
def resetDatabase():
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE students RESTART IDENTITY;")
        conn.commit()
        print("Database reset to default successfully.")
        cursor.close()
        conn.close()
        # Re-insert initial data
        initial_data = [
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
        ]
        for data in initial_data:
            addStudent(*data)
    except psycopg2.Error as e:
        print("Error resetting database:", e)

# Main function to test the application
def main():
    #Database application

    print("Start Database Application...")
    while True:
        try:
            print("\n1. Get all students")
            print("\n2. Add a new student")
            print("\n3. Update a student's email")
            print("\n4. Delete a student")
            print("\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\nAll students:")
                getAllStudents()

            elif choice == 2:
                firstName = input("Enter the student's first name: ")
                lastName = input("Enter the student's last name: ")
                email = input("Enter the student's email: ")
                enrollmentDate = input("Enter the student's enrollment date (format: YYYY-MM-DD): ")
                print("\nAdding a new student:")
                addStudent(firstName, lastName, email , enrollmentDate)

            elif choice == 3:
                studentId = input("Enter the student's ID: ")
                newEmail = input("Enter the student's new email: ")
                updateStudentEmail(studentId, newEmail)
                print("Student email updated successfully.")

            elif choice == 4:
                studentId = input("Enter the student's ID: ")
                print("\nDeleting a student:")
                deleteStudent(studentId)

            elif choice == 5:
                resetDatabase()
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid choice. Try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()