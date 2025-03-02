def add_student():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    age = input("Enter age: ")
    contact_number = input("Enter contact number: ")
    course = input("Enter course: ")

    student_info = f"Last name: {last_name}\nFirst name: {first_name}\nAge: {age}\nContact number: {contact_number}\nCourse: {course}\n\n"
    
    with open("student.txt", "a") as file:
        file.write(student_info)
    
    print("Student information has been saved to 'students.txt'.\n")

add_student()
