import json
import os

DB_FILE = "students.json"  # Ye file hamara database hai


# ========================
# LOAD & SAVE (Database)
# ========================

def load_data():
    # Agar file exist nahi karti toh empty list return karo
    if not os.path.exists(DB_FILE):
        return []

    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)  # JSON ko Python list mein convert karo

    except json.JSONDecodeError:
        return []  # File corrupt ho toh empty list return karo


def save_data(data):
    # Python list ko JSON file mein save karo
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ========================
# GRADE CALCULATION
# ========================

def calculate_grade(marks):

    if 90 <= marks <= 100:
        return "A+"

    elif 80 <= marks <= 89:
        return "A"

    elif 70 <= marks <= 79:
        return "B"

    elif 60 <= marks <= 69:
        return "C"

    elif 50 <= marks <= 59:
        return "D"

    elif 40 <= marks <= 49:
        return "E/Pass"

    else:
        return "Fail"


# ========================
# INPUT VALIDATION
# ========================

def get_valid_marks():

    # Jab tak valid marks na mile tab tak loop chalao
    while True:

        try:
            marks = int(input("Enter Marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Numbers only.")


def find_student(data, roll_no):

    # Roll number match karne pe student return karo
    for student in data:

        if student["roll_no"] == roll_no:
            return student

    return None


# ========================
# ADD STUDENT
# ========================

def add_student(data):

    print("\n===== ADD STUDENT =====")

    name = input("Enter Student Name: ").strip()

    # Empty name check
    if not name:
        print("Name cannot be empty.")
        return

    # Numbers-only name check
    if name.isdigit():
        print("Name cannot contain only numbers.")
        return

    roll_no = input("Enter Roll Number: ").strip()

    # Empty roll number check
    if not roll_no:
        print("Roll number cannot be empty.")
        return

    # Duplicate roll number check
    if find_student(data, roll_no):
        print("Roll number already exists.")
        return

    marks = get_valid_marks()

    grade = calculate_grade(marks)

    # Student data dictionary mein store karo
    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade
    }

    # List mein add karo
    data.append(student)

    # JSON file mein save karo
    save_data(data)

    print("Student added successfully.")


# ========================
# VIEW ALL STUDENTS
# ========================

def view_all(data):

    print("\n===== ALL STUDENTS =====")

    if not data:
        print("No records found.")
        return

    for student in data:

        print(
            f"Name: {student['name']} | "
            f"Roll: {student['roll_no']} | "
            f"Marks: {student['marks']} | "
            f"Grade: {student['grade']}"
        )


# ========================
# UPDATE STUDENT
# ========================

def update_student(data):

    print("\n===== UPDATE MARKS =====")

    roll_no = input("Enter Roll Number: ").strip()

    student = find_student(data, roll_no)

    if not student:
        print("Student not found.")
        return

    print(f"Current Marks: {student['marks']}")

    new_marks = get_valid_marks()

    # Marks aur grade update karo
    student["marks"] = new_marks
    student["grade"] = calculate_grade(new_marks)

    save_data(data)

    print("Updated successfully.")


# ========================
# DELETE STUDENT
# ========================

def delete_student(data):

    print("\n===== DELETE STUDENT =====")

    roll_no = input("Enter Roll Number: ").strip()

    student = find_student(data, roll_no)

    if not student:
        print("Student not found.")
        return

    confirm = input(
        f"Delete {student['name']}? (yes/no): "
    ).lower()

    if confirm == "yes":

        data.remove(student)

        save_data(data)

        print("Deleted successfully.")

    else:
        print("Cancelled.")


# ========================
# SEARCH STUDENT
# ========================

def search_student(data):

    print("\n===== SEARCH =====")

    keyword = input(
        "Enter Name or Roll Number: "
    ).lower().strip()

    found = False

    for student in data:

        # Partial search
        if (
            keyword in student["name"].lower()
            or keyword in student["roll_no"].lower()
        ):

            print(
                f"Name: {student['name']} | "
                f"Roll: {student['roll_no']} | "
                f"Marks: {student['marks']} | "
                f"Grade: {student['grade']}"
            )

            found = True

    if not found:
        print("No student found.")


# ========================
# LEADERBOARD
# ========================

def leaderboard(data):

    print("\n===== LEADERBOARD =====")

    if not data:
        print("No data available.")
        return

    # Marks descending order mein sort karo
    sorted_students = sorted(
        data,
        key=lambda x: x["marks"],
        reverse=True
    )

    print(f"{'Rank':<6}{'Name':<20}{'Marks':<10}{'Grade'}")

    print("-" * 45)

    # enumerate automatic rank deta hai
    for rank, student in enumerate(sorted_students, start=1):

        print(
            f"{rank:<6}"
            f"{student['name']:<20}"
            f"{student['marks']:<10}"
            f"{student['grade']}"
        )


# ========================
# STATISTICS DASHBOARD
# ========================

def statistics(data):

    print("\n===== STATISTICS =====")

    if not data:
        print("No data available.")
        return

    # Sirf marks ki list
    marks_list = [
        student["marks"] for student in data
    ]

    total = len(data)

    average = sum(marks_list) / total

    topper = max(
        data,
        key=lambda x: x["marks"]
    )

    passed = len([
        m for m in marks_list if m >= 40
    ])

    pass_pct = (passed / total) * 100

    # Grade-wise count
    grade_count = {}

    for student in data:

        grade = student["grade"]

        if grade in grade_count:
            grade_count[grade] += 1

        else:
            grade_count[grade] = 1

    print(f"Total Students  : {total}")

    print(
        f"Topper          : "
        f"{topper['name']} ({topper['marks']} marks)"
    )

    print(f"Average Marks   : {average:.2f}")

    print(f"Pass Percentage : {pass_pct:.2f}%")

    print("\nGrade-wise Count:")

    for grade, count in grade_count.items():

        print(f"{grade}: {count}")


# ========================
# MAIN MENU
# ========================

def main():

    # Program start hote hi data load karo
    data = load_data()

    while True:

        print("""
==================================
 STUDENT RESULT MANAGEMENT SYSTEM
==================================

1. Add Student
2. View All Students
3. Update Student Marks
4. Delete Student
5. Search Student
6. Leaderboard
7. Statistics Dashboard
8. Exit
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(data)

        elif choice == "2":
            view_all(data)

        elif choice == "3":
            update_student(data)

        elif choice == "4":
            delete_student(data)

        elif choice == "5":
            search_student(data)

        elif choice == "6":
            leaderboard(data)

        elif choice == "7":
            statistics(data)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


# ========================
# PROGRAM START
# ========================

if __name__ == "__main__":
    main()