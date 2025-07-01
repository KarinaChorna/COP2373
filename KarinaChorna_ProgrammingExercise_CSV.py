# Karina Chorna
# Programming Exercise CSV
# the purpose of this code is to add and display each student's full name and grades for 3 exams.

import csv

def write_grades():
    filename = 'grades.csv'
    # prompt user to enter the number of students
    num_students = int(input("Enter the number of students: "))

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # create the header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # add each student's full name and grades
        for i in range(num_students):
            print(f"\nEnter data for student {i + 1}:")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))

            # write student record
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"\nData successfully written to {filename}.")

# call function
write_grades()


def read_grades():
    filename = 'grades.csv'

    # display the results
    print("\nStudent Grades:\n")
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"{header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8} {header[4]:<8}")
        print("-" * 60)

        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8} {row[4]:<8}")

# call function
read_grades()
