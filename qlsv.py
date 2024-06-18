class Student:
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, course, marks):
        new_student = Student(name, roll_no, course, marks)
        self.students.append(new_student)
        print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found in the list.")
        else:
            print("Student List:")
            for student in self.students:
                print(f"Name: {student.name}, Roll No: {student.roll_no}, Course: {student.course}, Marks: {student.marks}")

    def update_student(self, roll_no, new_name, new_course, new_marks):
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = new_name
                student.course = new_course
                student.marks = new_marks
                found = True
                print(f"Student with roll number {roll_no} updated successfully!")
                break

        if not found:
            print(f"Student with roll number {roll_no} not found.")

    def delete_student(self, roll_no):
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                found = True
                print(f"Student with roll number {roll_no} deleted successfully!")
                break

        if not found:
            print(f"Student with roll number {roll_no} not found.")

    def search_student(self, keyword):
        found = False
        print("Search Results:")
        for student in self.students:
            if keyword.lower() in student.name.lower() or keyword.lower() in student.course.lower():
                print(f"Name: {student.name}, Roll No: {student.roll_no}, Course: {student.course}, Marks: {student.marks}")
                found = True

        if not found:
            print(f"No student found matching the keyword '{keyword}'.")

    def sort_students(self, by_field):
        if by_field == "name":
            self.students.sort(key=lambda student: student.name)
        elif by_field == "roll_no":
            self.students.sort(key=lambda student: student.roll_no)
        elif by_field == "course":
            self.students.sort(key=lambda student: student.course)
        elif by_field == "marks":
            self.students.sort(key=lambda student: student.marks)
        else:
            print("Invalid sorting field. Please choose from 'name', 'roll_no', 'course', or 'marks'.")

        print("Students sorted by", by_field)
        self.view_students()

if __name__ == "__main__":
    student_manager = StudentManager()

    while True:
        print("\nStudent Management Application")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Sort Students")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_no = input("Enter student roll number: ")
            course = input("Enter student course: ")
            marks = float(input("Enter student marks: "))
            student_manager.add_student(name, roll_no, course, marks)
        elif choice == "2":
            student_manager.view_students()
        elif choice == "3":
            roll_no = input("Enter roll number of student to update: ")
            new_name = input("Enter new name (or press Enter to skip): ")
            new_course = input("Enter new course ():")
