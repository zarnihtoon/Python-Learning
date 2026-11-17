#day 9 - Python Error Handling
#try & except
try:
        number = int(input("Enter Number: "))
        print ("Your Number is ", number)
except ValueError:
        print("Please Enter Numbers Only!")

#ZeroDivisionError
try:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    result = a/b
    print("Result: ", result)

except ZeroDivisionError:
    print("Cannot Divide By Zero!")

except ValueError:
    print("Please Enter Numbers Only!")

#IndexError
fruits = ["Apples", "Banana", "Orange"]

try:
    print(fruits[5])
except IndexError:
    print("Index Not Found!")

#using else
try:
    number = int(input("Enter Number: "))

except ValueError:
    print("Invalid Number!")
else:
    print("Your number is", number)
    print("Program Successful")

#using finally
try:
    number = int(input("Enter Number: "))
    print(number)

except ValueError:
    print("Invalid Input!")

finally:
    print("Program Successful!!!")

#Mini Project - Safe Calculator
while True:
    print("\n===== SAFE CALCULATOR =====")
    print("1. Addition")
    print("2. Substration")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "5":
        print("Calculator Closed!!!")
        break
    elif choice in ["1","2","3","4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = a + b

            elif choice == "2":
                reslut = a - b

            elif choice == "3":
                result = a * b

            elif choice == "4":
                try:
                    result = a / b
                except ZeroDivisionError:
                    print("Cannot Divided by Zero!!! ")
            print("Result:", result)   

            

        except ValueError:
            print("Enter Numbers Only!!!")

    else:
        print("Invalid Choice!!!")

#Exercise 1 - Age Checker
while True: 
    try:
        num = int(input("Enter Your Number: "))
        if num >= 18:
            print("You are an adult!")
        elif num <= 18:
            print("You are a minor!!!")
        else:
                print("Invalid!!!")
    except ValueError:
        print("Enter Numbers Only!")

#Exercise 2 - Division Program
    while True:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = num1 / num2
                print("Your Answer is", result)
            except ValueError:
                print("Enter Numbers Only!!!")
            except ZeroDivisionError:
                print("Cannot divide by zero!!!")

#Exercise 3 - Safe Notes Reader
            with open ("zarni.txt","r") as file:
                content = file.read()
                try:

                    if content:
                        print("===== YOUR NOTES ======")
                        print(content)
                    else: 
                        print("No Notes Found!!!")

                except FileNotFoundError:
                    print("Not Found Any Files!!!")

                finally:
                    print("Program Successfully Accomplinished!!!")