#List []
students = ["Mg Mg", "Aye Aye", "Ko Ko"]
print (students)
print (students[0])
print (students[1])

fruits = ["Apple","Orange", "Mango"]
fruits.append("Banana")
fruits.remove("Orange")
fruits[0] = "Grape"
fruits[2] = "Guava"
fruits.append("ZARNI")

print (fruits)
print (len(fruits))

#Skip Tuple Bez similar to List and the difference is we cannot change data in Tuple
#Dictionary
student = { 
    "name": "Mg Mg",
    "age" : 20,
    "major":"BIS"
}
print (student["name"])
print (student["age"])
print (student["major"])

#Dictionary
student = { 
    "name": "Mg Mg",
    "age" : 20,
    "major":"BIS"
}
print (student["name"])
print (student["age"])
print (student["major"])

student["age"] = 21
student["city"] = "Mandalay"

del student["major"]
print (student)

#Combination of Lists & Dictionaries
students = [
    {"name": "Mg Mg", "age":20},
    {"name": "Aye Aye", "age":19},
    {"name": "Ko Ko", "age":21}
]
print(students[0]["name"])
print(students[1]["name"])

#Exercise 1
shopping_list = ["Milk", "Egg", "Bread"]

shopping_list.append("Apple")
shopping_list.remove("Egg")
print(shopping_list)

#Exercise 2
#Student Information
student = { 
    "name" : "ZARNI HTOON",
    "age" : 20,
    "major" : "BIS",
    "city" : "Myothit"
}
student["age"] = 21
student["city"] = "Magway"
print (student)

#Exercise 3 - Mark Calculator
marks = [80, 75, 90, 65, 85]

print("All Marks: ",marks)
print("First Marks: ",marks[0])
print("Last Marks: ", marks[-1])
print("Total Subjects: ",len(marks))
print("Total Marks: ",sum(marks))
print(sum(marks)/len(marks))

students = [
    {"name": "Mg Mg", "age" : 21},
    {"name": "Aye Aye", "age" : 45},
    {"name": "Ko Ko", "age": 43}
]
print("----- Student Information -----")
for student in students:
    print("Name: ",student["name"])
    print("Age:" ,student["age"])
    print("-------------")


#Extra Exercise
numbers = [10, 30, 20, 50, 40]

numbers.append(60)
numbers.remove(30)
numbers.sort()
numbers.reverse()

print(numbers)
print("The maximum number: ",max(numbers))
print("The minimum number: ",min(numbers))
print("total number",sum(numbers))
