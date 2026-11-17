#Day 11 - Python OOP(Class & Object)
#Class
class Student:
    name = "ZARNI"
    age = 20
    major = "BIS"

student1 = Student()

print(student1.name)
print(student1.age)
print(student1.major)

#_init_method
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
student1 = Student("ZARNI",20,"BIS")
student2 = Student("Aye Aye", 19, "SE")

print(student1.name)
print(student2.age)

#writing function into class
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

student1 = student("ZARNI", 20)
student1.introduce()

#We can change data in class
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

student1 = Student("ZARNI", "BIS")
print(student1.major)
student1.major = "SE"
print(student1.major)

#Exercise 1
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
student1 = Student("Z",20, "BIS")
student2 = Student("BA", 20, "KE")

print(student1.name,student1.age, student1.major)
print(student2.name, student2.age, student2.major)

#Exercise 2
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def introduce(self):
        print(f"My name is {self.name} !!!")
        print(f"I am {self.age} years old!!!")

student1 = Student("Z",20,"BIS")
student1.introduce()

#Exercise 3
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print("Deposit Successfully!!!")
            else:
                print("Invalid Amount!!!")

    def withdraw(self, amount):
            if amount <= 0:
                print("Invalid Amount!!!")
            elif amount > self.balance:
                print("Insufficent Balance!!!")

            else:
                self.balance -= amount
                print("Withdrawl Successful!!!")

    def check_balance(self):
            print("Account Holder:", self.account_holder)
            print("Balance:", self.balance)

account1 = BankAccount("ZARNI", 100000)
account1.deposit(50000)
account1.withdraw(30000)
account1.check_balance()

#Exercise 4 - Mini Project
class Student:
    def __init__(self,name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")

students = []
while True:
    print("==== STUDENT SYSTEM ==== ")
    print(" 1. Add Student ")
    print(" 2. View Student ")
    print(" 3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter Name: ")
        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("Enter Numbers Only!!!")
            continue
        major = input("Enter Major: ")
        student = Student(name, age, major)
        students.append(student)
        print("Student Added Successfully!!!")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Found !!!")

        else:
            for student in students:
                print("\n ----------------- ")
                student.show_info()

    elif choice == "3":
        print("Thank You !!! ")
        break
    else:
        print("Invalid Choice ! ! !")
        

        
