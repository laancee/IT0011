first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
contact_number = input("Enter your contact number: ")
course = input("Enter your course: ")

student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}\nCourse: {course}\n\n"

with open("students.txt", "a") as file:
    file.write(student_info)

print("Student information has been saved to 'students.txt'.")
