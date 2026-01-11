import os

FILE_NAME = "results.txt"

# ------------------ User Defined Data Structure ------------------
class Student:
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
        self.result = "Pass" if marks >= 40 else "Fail"

    def to_record(self):
        return f"{self.sid},{self.name},{self.marks},{self.result}\n"


# ------------------ File Handling Functions ------------------
def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                sid, name, marks, result = line.strip().split(",")
                students.append({
                    "sid": sid,
                    "name": name,
                    "marks": int(marks),
                    "result": result
                })
    return students


def save_students(students):
    with open(FILE_NAME, "w") as f:
        for s in students:
            f.write(f"{s['sid']},{s['name']},{s['marks']},{s['result']}\n")


# ------------------ CRUD Operations ------------------
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student = Student(sid, name, marks)
    students = load_students()
    students.append({
        "sid": student.sid,
        "name": student.name,
        "marks": student.marks,
        "result": student.result
    })
    save_students(students)
    print("Student record added successfully.")


def view_students():
    students = load_students()
    if not students:
        print("No records found.")
        return

    print("\nID\tName\tMarks\tResult")
    print("-" * 30)
    for s in students:
        print(f"{s['sid']}\t{s['name']}\t{s['marks']}\t{s['result']}")


def update_student():
    sid = input("Enter Student ID to update: ")
    students = load_students()

    for s in students:
        if s["sid"] == sid:
            s["name"] = input("Enter new name: ")
            s["marks"] = int(input("Enter new marks: "))
            s["result"] = "Pass" if s["marks"] >= 40 else "Fail"
            save_students(students)
            print("Record updated successfully.")
            return

    print("Student not found.")


def delete_student():
    sid = input("Enter Student ID to delete: ")
    students = load_students()
    new_students = [s for s in students if s["sid"] != sid]

    if len(new_students) == len(students):
        print("Student not found.")
    else:
        save_students(new_students)
        print("Record deleted successfully.")


# ------------------ Result Analysis ------------------
def analyze_results():
    students = load_students()
    if not students:
        print("No data available for analysis.")
        return

    marks_list = [s["marks"] for s in students]
    pass_count = sum(1 for s in students if s["result"] == "Pass")
    fail_count = len(students) - pass_count

    print("\n--- Result Analysis ---")
    print("Total Students:", len(students))
    print("Passed:", pass_count)
    print("Failed:", fail_count)
    print("Pass Percentage:", (pass_count / len(students)) * 100)
    print("Average Marks:", sum(marks_list) / len(marks_list))
    print("Highest Marks:", max(marks_list))
    print("Lowest Marks:", min(marks_list))


# ------------------ Main Menu ------------------
def main():
    while True:
        print("\n--- Student Exam Result Analysis System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Analyze Results")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            analyze_results()
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")


# ------------------ Program Entry ------------------
main()
