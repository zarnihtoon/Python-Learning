#Day 2 - Data Types & Operators
#1 String ( str )
name = "Zarni"
city = "Magway"

print(name)
print(city)

#2 Integer ( int )
age = 20
quantity = 5

print(age)
print(quantity)

#3 Float ( float )
price = 2500.00
height = 5.9

print(price)
print(height)

#4 Boolean ( bool )
is_student = True
is_married = False

print(is_student)
print(is_married)

name = "Zarni"
age = 20
price = 5000.50
is_student = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_student))

#Exercise 1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero")

#Exercise 2
product_name = input("Product Name: ")
price = float(input("Product Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print("\n===== RECEIPT =====")
print("Product:", product_name)
print("Price:", price, "MMK")
print("Quantity:", quantity)
print("Total:", total, "MMK")

#Exercise 3
age = int(input("Enter your age: "))

future_age = age + 5

print("Current age:", age)
print("After 5 years:", future_age)