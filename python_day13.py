#Day - 13 OOP Part 3 
#Class Attritute
class Student:
    school = "MCC"
    def __init__(self,name):
        self.name = name

student1 = Student("Mg Mg")
student2 = Student("Aye Aye")

print(student1.name,student1.school)
print(student2.name,student2.school)

#@classmethod
class Student:
    school = "MCC"
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Student.change_school("NSPU")
print(Student.school)

#staticmethod
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

result = Calculator.add(10, 20)
print (result)

#Exercise 1 
class Student:
    school = "MCC"

    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Mg Ba",20)
student2 = Student("Mg Ye", 30)

print(student1.name,student1.age,student1.school)
print(student2.name, student2.age, student2.school)


#Exercise 2 - Change School
class Student:
    school = "UCSM"

    @classmethod
    def zarni_school(cls, new_school):
        cls.school = new_school
Student.zarni_school("nspu")
print("My school is ", Student.school)

#Exercise 3 - Static Method Calculator
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    def substract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b
result1 = Calculator.add(10, 20)
result2 = Calculator.substract(20, 10)
result3 = Calculator.multiply(10, 20)
result4 = Calculator.divide(20, 10)

print("Addition ans is ", result1)
print("Substration ans is ", result2)
print("Multiplication ans is ", result3)
print("Division ans is ", result4)

#Exercise 4 - Bank Account Mini Project
class BankAccount:
    bank_name = "KBZ Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit:", amount)

        else:
            print("Invalid Amount !")
    def withdrawal(self, amount):
        if amount <= 0 :
            print ("Invalid amount !")

        elif amount > self.balance:
            print ("Insufficient balance !")

        else:
            self.balance -= amount
            print("Withdrawl:", amount)
    def check_balance(self):
        print("Bank: ", self.bank_name)
        print("Owner: ", self.owner)
        print("Balance :" , self.balance)

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

account1 = BankAccount("ZARNI", 1000000)
account1.check_balance()

print()
account1.deposit(500000)
print("Balance is :", account1.balance)

print()
account1.withdrawal(500000)
print("Balance is : ", account1.balance)

        