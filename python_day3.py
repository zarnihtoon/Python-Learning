#Exercise 1
age = int(input("Enter Your Age: "))
if age   <= 0:
    print ("Invalid")
elif age <= 18:
    print ("U r a teenager")
else:
    print ("U r an adult")


#Exercise 2
marks = int(input("Enter Your Marks: "))

if marks < 0 or marks > 100:
    print ("Invalid Marks")
elif marks >= 80:
    print ("Grade A")
elif marks >= 70:
    print ("Grade B")
elif marks >= 60:
    print ("Grade C")
elif marks >= 50:
    print ("Grade D")
elif marks >= 40:
    print ("Grade E")
else:
    print ("Grade F")

#Exercise 3
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

if username == "admin" and password == "1234567890":
    print ("Login Success!!!")
else:
    print ("Something Wrong!!!Please check Your username and password again!!!")

#Exercise 4
num = int(input("Enter a number: "))

if num % 2 == 0:
    print ("It is even number!")
else:
    print ("It is odd number!")

#Day 3 Mini Challenge
withdrawal_money = int(input("Enter Your Amount: "))
balance = 50000
print ("======= ATM SYSTEM =======")
print ("Your Balance:", balance)
print ("Enter withdraw amount:", withdrawal_money)

if withdrawal_money < 0:
    print ("Invalid Amount!!!")

elif withdrawal_money > balance:
    print ("Insufficient Balance!!!")
    
else:
    remaining_balance = balance - withdrawal_money

    print ("Withdrawal Successful")
    print ("Remaining Balance :", remaining_balance)


