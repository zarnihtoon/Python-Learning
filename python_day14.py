#Day 14 - Student Management System
class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def show_info(self):
            print(f"===== {self.name.title()}'s INFO ===== ")
            print(f"Student ID : {self.student_id}")
            print(f"Name : {self.name.title()}")
            print(f"Age: {self.age}")
            print(f"Major: {self.major.capitalize()}")

#Exercise 2 - Add Student
students = []
def add_students():
    try:
                
        student_id = input("Enter Your Student's ID: ")
        #check Duplicate ID
        for student in students:
            if student.student_id == student_id:
                print("This ID Already Exists !")
                return 
        name  = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        major = input("Enter Your Major: ")
        if age <= 0:
            print("Invalid Age !")
            return 
        student = Student(student_id, name , age , major)
        students.append(student)

        print("Student Added Successfully !")
    except ValueError:
        print("Please Enter Age as a Number !")

def view_students():
    if not students:
        print("No Students Found !")
        return
    for student in students:
        student.show_info()
def search_students():
    search_id = input("Enter Your Student's ID: ")

    for student in students:
        if student.student_id == search_id:
            student.show_info() 
            return

    print("Student Not Found ! ") 

def delete_student():
    delete_id = input("Enter Student's ID: ")

    for student in students:
        if student.student_id == delete_id:
            students.remove(student)
            print("Student Deleted Successfully !")
            return
    print("Student Not Found !")
                    
while True:
    print("\n ===== STUDENT's Management System =====")
    print(" 1. Add Student ")
    print(" 2. View Student ")
    print(" 3. Search Student ")
    print(" 4. Delete Student ")
    print(" 5 . Exit ")

    choice = input("Choose: " )

    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_students()
    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You !!!")
        break
    else:
        print("Invalid Option ! Please Try Again !!!")
                
