FILE_NAME = "students.txt"


def load_data():
    students = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line and "," in line:
                    name, marks = line.split(",")
                    students[name.lower()] = float(marks)
    except FileNotFoundError:
        pass
    return students


def save_data(students):
    with open(FILE_NAME, "w") as file:
        for name, marks in students.items():
            file.write(f"{name},{marks}\n")


def get_valid_name():
    name = input("Enter student name: ").strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    return name.lower()


def get_valid_marks():
    marks = float(input("Enter marks (0-100): "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    return marks


def add_student(students):
    try:
        name = get_valid_name()
        if name in students:
            print("Student already exists!")
            return
        marks = get_valid_marks()
        students[name] = marks
        save_data(students)
        print("Student added successfully!")
    except ValueError as e:
        print("Invalid input:", e)


def display_students(students):
    if not students:
        print("No records found.")
    else:
        print("\n--- Student Records ---")
        for name, marks in students.items():
            print(f"Name: {name.capitalize()} | Marks: {marks}")


def search_student(students):
    name = input("Enter student name to search: ").strip().lower()
    if name in students:
        print(f"Name: {name.capitalize()} | Marks: {students[name]}")
    else:
        print("Student not found.")


def update_student(students):
    try:
        name = input("Enter student name to update: ").strip().lower()
        if name not in students:
            print("Student not found.")
            return
        marks = get_valid_marks()
        students[name] = marks
        save_data(students)
        print("Student updated successfully!")
    except ValueError as e:
        print("Invalid input:", e)


def delete_student(students):
    name = input("Enter student name to delete: ").strip().lower()
    if name in students:
        del students[name]
        save_data(students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    students = load_data()

    while True:
        try:
            print("\n===== Student Record System =====")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student(students)
            elif choice == 2:
                display_students(students)
            elif choice == 3:
                search_student(students)
            elif choice == 4:
                update_student(students)
            elif choice == 5:
                delete_student(students)
            elif choice == 6:
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Enter 1-6.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()