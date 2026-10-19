from dataclasses import dataclass

# 1. Define the Structure (Data Class)
@dataclass
class Student:
    id: int
    name: str
    age: int

# In-memory storage for students
students = []

# 2. CREATE Operation
def create_student(student_id: int, name: str, age: int):
    # Check if student ID already exists
    for s in students:
        if s.id == student_id:
            print(f"Error: Student with ID {student_id} already exists.")
            return
    new_student = Student(id=student_id, name=name, age=age)
    students.append(new_student)
    print("Student added successfully.")

# 3. READ Operation
def display_students():
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s.id} | Name: {s.name} | Age: {s.age}")

# 4. UPDATE Operation
def update_student(id, new_name=None, new_age=None):
    for s in students:
        if s.id == id:
            if new_name:
                s.name = new_name
            if new_age:
                s.age = new_age
            print("Student updated successfully.")
            return
    print("Student not found.")

# 5. DELETE Operation
def delete_student(id):
    for s in students:
        if s.id == id:
            students.remove(s)
            print("Student deleted successfully.")
            return
    print("Student not found.")

# Example Usage
create_student(1, "Reshma", 20)
create_student(2, "Riya", 22)

print("\nStudents:")
display_students()  # Fixed: changed from display_student()

update_student(1, new_name="Reshma", new_age=21)  # Fixed: changed from Update_student()

print("\nAfter Update:")
display_students()  # Fixed: changed from display_student()

delete_student(2)

print("\nAfter Delete:")
display_students()  # Fixed: changed from display_student()
