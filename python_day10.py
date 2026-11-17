#Day 10 - Python Modules
import math
print(math.sqrt(25))
print(math.sqrt(16))
print(math.pow(2,3))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pi)

#Random Module
import random
fruits = ["Apple","Banana","Orange","Mango"]
print(random.choice(fruits))

#Datetime Module
import datetime
today = datetime.date.today()
print("Today is ", today)

now = datetime.datetime.now()
print (now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))

#Mini Project - Number Guessing Game
import random
secret_number = random.randint(1,10)
print ("===== NUMBER GUESSING GAME =====")
while True:
    try:
        guess = int(input("Guess a number (1-10): "))

        if guess < 1 or guess > 10:
            print("Please choose between 1 and 10!")

        elif guess < secret_number:
            print("Too Low! Try Again.")

        elif guess > secret_number:
            print("Too High! Try Again." )

        else:
            print("Correct! You Win!")
            break

    except ValueError:
        print("Please Enter Numbers Only!")

#Exercise 1 - Random Number
import random

for i in range(5):
    number = random.randint(1,100)
    print(number)

#Exercise 2 - Age Calculator
import random
students = ["Aung Aung", "Kyaw Kyaw", "Ba Nyo","Ba Maung", "Nyo Mya"]
print(random.choice(students))

#Exercise 3 - Age Calculator by myself
import datetime
your_birthyear = int(input("Enter your birth year : "))
current_year = datetime.date.today().year
your_age = current_year - your_birthyear
print(your_age)

#Exercise 2 from ChatGPT
import datetime
while True:
    try:
        birth_year = int(input("Enter your Birth Year: "))
        current_year = datetime.date.today().year

        if birth_year <= 0 or birth_year > current_year:
            print("Invalid Birth Year!!!")

        else:
            age = current_year - birth_year
            print("Your age is ", age)
    except ValueError:
        print("Enter Numbers Only!!!")

#Exercise 4 Mini Project
    import random

    secret_num = random.randint(1,10)
    attempts = 0
    print(" ==== YOUR GAMES ==== ")
    print(" You have only 5 attempts!!!")
    while attempts < 5:
        try:
            guess = int(input("Enter Your Number (1 - 10): "))

            if guess < 1 or guess > 10:
                print("Please Enter 1 to 10!!!")
                continue
            attempts += 1
            if guess < secret_num:
                print("Too Low!!!")
            elif guess > secret_num:
                print("Too High!!!")
            else:
                print("Correct!!! You hit the point!!!")
                break
        except ValueError:
            print("Enter Numbers Only!!!")

    else:
        print("GAME OVER")
        print("Correct number was,", secret_num)