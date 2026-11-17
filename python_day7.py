name = "zar n htun"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

#Exercise 1 Strip
text = " Hello Python "
print (text.strip())

#Exercise 2 Replace
message = "I like Java"
print(message.replace("Java", "Python"))

#Exercise 3 Split
fruits = "apple, banana, orange"
result = fruits.split("<>")
print (result)

#Exercise 4 Find word in String
email = "zarni@gmail.com"
print (email.find("@"))
print (email.count("a"))
print (email.startswith("zarni"))
print (email.endswith(".com"))

#Exercise 5 f string
name = "ZARNI"
age = 20
major = "BIS"

print (f"My name is {name}")
print (f"I am {age} years old")
print (f"My major is {major}")

#Exercise  5 Project - User Profile
name = input("Enter your name: ")
email = input("Enter your email: ")
city = input("Enter your city: ")

name = name.strip().title()
email = email.strip().lower()
city = city.strip().title()

print("\n===== USER PROFILE =====")
print(f"Name : {name}")
print(f"Email: {email}")
print(f"City: {city}")

#Practice 1 Name Formatter
name = input("Enter your name: ")
print(name.upper())
print(name.lower())
print(name.title())

#Practice 2 Email Checker
email = input("Enter your email: ")

if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")

#Practice 3 Student Profile
name = input("Enter your name: ")
age = input("Enter your age: ")
major = input("Enter your major: ")
city = input("Enter your city: ")

name = name.strip().title()
age = age.strip()
major = major.strip().upper()
city = city.strip().title()

print(f"\n====== {name}'s Profile ======")
print(f"Name : {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"City: {city}")