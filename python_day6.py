def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()

#parameters & arguments
def greet(name):
    print("Hello", name)
greet("Mg Mg")
greet("Aye Aye")

def student_info(name, age):
    print("Name: ", name)
    print("Age: ", age)

student_info("Mg Mg", 20)

def add( a, b):
    result = a  + b
    return result
answer = add(10, 20)
print (answer)

#4.Combination of Functions & Lists
marks = [80, 75, 90, 65, 85]

def calculate_average(scores):
    total = sum(scores)
    average = total/len(scores)
    return average
result = calculate_average(marks)
print ("Average Marks: ",result)

#Exercise 1
def greet(name):
    print ("Hello", name)

greet("Htoon")
greet("Zarni")

#Simple Calculator
def add(a, b):
    adding = a  * b
    return adding

bar = add(10, 30)
print(bar)

#Student Average Calculator
marks = [80, 75, 90, 65, 85]

def calculate_average(blar):
    total = sum(blar)
    average = sum(blar)/len(blar)
    return average

mark = calculate_average(marks)
print(mark)

#Student Registration System
students = [
    {"name": "Mg Mg", "age": 20, "major": "BIS"},
    {"name": "Aye Aye", "age": 19, "major": "SE"},
    {"name": "Ko Ko", "age": 21, "major": "KE"}
]
def show_students():
    for student in students:
        print("Name: ", student["name"])
        print("Age: ",student["age"])
        print("Major: ",student["major"])
        print("---------------")

def search_student(name):
    for student in students:
        if student["name"].lower() ==  name.lower():
            return student
        return None

def count_students():
    return len(students)

show_students
result = search_student("Mg Mg")
print ("Search for :", result)

print ("Total Students:", count_students())