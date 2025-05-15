class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_string(self):
        return f"{self.roll},{self.name},{self.marks}\n"

    @staticmethod
    def from_string(line):
        roll, name, marks = line.strip().split(',')
        return Student(roll, name, marks)


def save_student(student, filename="students.txt"):
    with open(filename, "a") as f:
        f.write(student.to_string())


def read_students(filename="students.txt"):
    students = []
    try:
        with open(filename, "r") as f:
            for line in f:
                students.append(Student.from_string(line))
    except FileNotFoundError:
        pass  # File will be created when saving the first student
    return students


def display_students():
    students = read_students()
    if not students:
        print("\nNo student records found.")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print(f"Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")


def add_student():
    try:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student = Student(roll, name, marks)
        save_student(student)
        print("Student added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter numeric value for marks.")


def main():
    while True:
        print("\n====== Student Records Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
