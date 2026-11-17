#Exercise 1
for i in range(1, 11):
    print (i)

#Exercise 2
num = int(input("Enter a number: "))
for i in range(10):
    print ("Your answer is ", num ," x ", i , " = ", num * i)

#Exercise 3
password = ""
while password != "python123":
    password = input("Enter Your Password: ")

print (" Login Successful")

#Exercise 3 (Alternative Method)
password = ""
while password != "python123":
    password = input ("Enter Your Password: ")
    if password != "python123":
        print ( " Login Unsuccessful ")
print ( " Login Successful ")

#Exercise 4
balance = 100000

while True:
    print ("===== ATM Menu ======")
    print ("1. Check Balance ")
    print ("2. Withdraw ")
    print ("3. Exit ")

    choice = input("Choose: ")

    if choice == "1":
        print ("Your Balance is ", balance)

    elif choice == "2":
        amount = int(input("Enter Your Amount: " ))

        if amount <= 0:
            print ("Invalid Amount!!!")

        elif amount > balance:
            print ("Insufficient Balance!!!")

        elif amount < balance:
            balance -= amount
            print ("Withdrawal Successful")
            print ("Your remaining balance is ", balance)

    elif choice == "3":
        print (" Thank You!!!")
        break

    else:
        print ("Invalid Choice!!!")
