import json

# File handling functions
def open_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []

def save_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def save_as_file(new_filename, data):
    save_file(new_filename, data)

def calculate_grade(class_standing, major_exam):
    return (0.6 * class_standing) + (0.4 * major_exam)

def show_all_records(records):
    for record in records:
        print(record)

def order_by_last_name(records):
    return sorted(records, key=lambda x: x[1][1])

def order_by_grade(records):
    return sorted(records, key=lambda x: calculate_grade(x[2], x[3]), reverse=True)

def show_student_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            return record
    return "Student not found."

def add_record(records, student_id, first_name, last_name, class_standing, major_exam):
    if not isinstance(records, list):
        records = []
    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    return records

def edit_record(records, student_id, new_first_name, new_last_name, new_class_standing, new_major_exam):
    for i, record in enumerate(records):
        if record[0] == student_id:
            records[i] = (student_id, (new_first_name, new_last_name), new_class_standing, new_major_exam)
            return records
    return "Student not found."

def delete_record(records, student_id):
    records = [record for record in records if record[0] != student_id]
    return records

def main():
    filename = "students.json"
    records = open_file(filename)
    if not isinstance(records, list):
        records = []
    
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            records = open_file(filename)
            print("File opened successfully.")
        elif choice == "2":
            save_file(filename, records)
            print("File saved successfully.")
        elif choice == "3":
            new_filename = input("Enter new filename: ")
            save_as_file(new_filename, records)
            print("File saved as successfully.")
        elif choice == "4":
            show_all_records(records)
        elif choice == "5":
            records = order_by_last_name(records)
            show_all_records(records)
        elif choice == "6":
            records = order_by_grade(records)
            show_all_records(records)
        elif choice == "7":
            student_id = input("Enter student ID: ")
            print(show_student_record(records, student_id))
        elif choice == "8":
            student_id = input("Enter student ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_standing = float(input("Enter class standing grade: "))
            major_exam = float(input("Enter major exam grade: "))
            records = add_record(records, student_id, first_name, last_name, class_standing, major_exam)
            print("Record added successfully.")
        elif choice == "9":
            student_id = input("Enter student ID: ")
            new_first_name = input("Enter new first name: ")
            new_last_name = input("Enter new last name: ")
            new_class_standing = float(input("Enter new class standing grade: "))
            new_major_exam = float(input("Enter new major exam grade: "))
            records = edit_record(records, student_id, new_first_name, new_last_name, new_class_standing, new_major_exam)
            print("Record updated successfully.")
        elif choice == "10":
            student_id = input("Enter student ID to delete: ")
            records = delete_record(records, student_id)
            print("Record deleted successfully.")
        elif choice == "11":
            save_file(filename, records)
            print("Exiting program. Data saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
