#Day 8 - Python File Handeling
file = open("data.txt", "r")

#file write
file = open("data.txt","w")

file.write("Hello Python by ZARNI HTOON!!!")
file.close()

#file read
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#file read
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#with open
with open("data.txt", "w") as file:
    file.write("I am learning Python!!!")
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

with open("data.txt", "w") as file:
    file.write("Mg Mg \n")
    file.write("Ma Aye \n")
    file.write("Ba Mg\n")
with open("data.txt", "r") as file:
    print(file.readlines())

while True:
    print("\n===== NOTES APP =====")
    print("1. Write Note ")
    print("2. View Note ")
    print("3. Exit ")

    choice = input("Choose:")

    if choice == "1":
        note = input("Enter your note: ")

        with open(" notes.txt", "a") as file:
            file.write(note + "\n")

        print ("Note Saved Successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                content = file.read()

                print("\n===== YOUR NOTES =====")
                print(content)
        except FileNotFoundError:
            print("No Notes Found!")

    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid Choice")

#Exercise 1
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

name = name.strip().title()
age = age.strip()
city = city.strip().title()

with open("myinfo.txt","w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"City: {city}")

print("Information Saved Successfully!!!")

#Exercise 2
with open("student.txt", "r") as file:
    content = file.read()
    print(content)

#Exercise 2
with open ("students.txt","w") as file:
    for i in range(3):
        name = input(f"Enter Student { i + 1} Name: ")
        file.write(name + "\n")
print("\n===== STUDENT LIST =====")
with open("students.txt","r") as file:
    students = file.readlines()

    for student in students:
        print(student.strip().title())

#Exercise 3 - Note App
while True:
    print("\n===== NOTES APP =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note Added Successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                content = file.read()

                print("\n===== YOUR NOTES =====")

                if content:
                    print(content)
                else:
                    print("No Notes Found!")

        except FileNotFoundError:
            print("No Notes Found!")

    elif choice == "3":
        print("Thank You for Using Notes App!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
