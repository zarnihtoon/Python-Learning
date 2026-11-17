#Day 12 - Python OOP ( Part - 2 )
#Inheritance: : means we can use properties and methods of Parent Class in Child Class!!!
class Animal:
    def eat(self):
        print("Animal is eating !")
class Dog(Animal):
    def bark(self):
        print("Dog is barking !")

dog1 = Dog()
dog1.eat()
dog1.bark()

#Using super() : we can reuse ___init()___ if we use super()
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")
        print(f"Major: {self.major}")

student1 = Student("ZARNI", 20, "BIS")
student1.show_info()

#Encapsulation - Protecting Data
#Means : Instead of correction of data directly, we can correct using methods
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print("Balance: ", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit Successful ! ")
        else:
            print("Invalid Amount!")

account = BankAccount(1000000)

account.check_balance()
account.deposit(50000)
account.check_balance()

#Polymorphism - although methos name is same, can't work when objects are different
class Dog:
    def sound(self):
        print("Woof Woof !")
class Cat:
    def sound(self):
        print("Meow Meow !")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

#Exercise 1 - Animal Inheritance
class Animal():
    def eat(self):
        print("At the moment...")

class Dog(Animal):
    def bark(self):
        print("The sun is shinning ")

class Cat(Animal):
    def meow(self):
        print("The wind is breezing ")

class time(Animal):
    def second(self):
        print("Time is running ")

class battery(Animal):
    def laptop(self):
        print("My laptop battery is draining quickly ")

class zarni(Animal):
    def htoon(self):
        print("ZARNI is missing someone...")

dog = Dog()
cat = Cat()
time = time()
battery = battery()
zarni = zarni()


dog.eat()
dog.bark()
cat.meow()
time.second()
battery.laptop()
zarni.htoon()

#Exercise 2 - Person & Student
class Person():
    def __init__(self, name , age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")

student1 = Student("ZARNI", 20, "BIS")

student1.show_info()

#Exercise 3 - Bank Account Encapsulation
class BankAccount():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit Successfully! ")
        else:
            print("Invalid Amount!!")

    def withdrwal(self, amount):
        if amount <= 0:
            print("Invalid Amount!!!")
        elif amount > self.__balance:
            print("Insufficient Balance!!!")
        else:
            self.__balance -= amount
            print("Withdrawl Successful!!!")
    def check_balance(self):
        print("The remaining balance is ", self.__balance)

account = BankAccount(1000000)

account.check_balance()
account.deposit(200000000)
account.withdrwal(500000)
account.check_balance()

#Employee Polymorphism
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print("\n ==== Manager ====")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def show_info(self):
        print("\n ==== Developer ===== ")
        print(f"Name: {self.name} ")
        print(f"Salary: {self.salary}")
        print(f"Language: {self.programming_language}")
manager = Manager("Mg Mg ", 8000000, "IT")
developer = Developer("Ma Zar", 90900, "Python")

manager.show_info()
developer.show_info()
