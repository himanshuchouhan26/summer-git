'''
# Q.1
a=int(input("Enter a number: "))
if(a%2==0):
  print("Number is odd")
else:
  print("Number is even")


# Q.2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)
print("The largest number is:", largest)

# Q.3
year=int(input("Enter a year: "))
if(year%4==0 and year%100!=0 or year%400==0):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year. ")

# Q.4
percentage = int(input("Enter percentage: "))

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
else:
    print("Grade F")

# Q.5
letter = input("Enter a letter: ").lower()
if letter in 'aeiou':
    print("This is a Vowel")
else:
    print("This is a Consonant")

# Q.6
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero error")
else:
    print("Invalid operator")

# Q.7
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Q.8
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

# Q.9
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Invalid triangle")

# Q.10
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print(f"BMI = {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")

# Q.11
price = float(input("Enter the price of the product: "))

if (price > 1000):
    discount = 0.10
elif (500 <= price <= 1000):
    discount = 0.05
else:
    discount = 0.0

final_price = price - (price * discount)
print(f"Final price after discount: {final_price:.2f}")

# Q.12
month = input("Enter the name of the month: ").capitalize()
year = int(input("Enter the year: "))

if month in ["January", "March", "May", "July", "August", "October", "December"]:
    print("No. of days = 31")
elif month in ["April", "June", "September", "November"]:
    print("No. of days = 30")
elif month == "February":
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("No. of days = 29")
    else:
        print("No of days = 28")
else:
    print("Invalid month")

# Q.13
balance = 1000 

print("Welcome to the ATM")
print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print(f"Your balance is: {balance}")
elif choice == 2:
    deposit = float(input("Enter amount to deposit: "))
    balance += deposit
    print(f"Deposited successfully. New balance is: {balance}")
elif choice == 3:
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw <= balance:
        balance -= withdraw
        print(f"Withdrawal successful. New balance is: {balance}")
    else:
        print("Insufficient balance.")
else:
    print("Invalid choice")

# Q.14
age = int(input("Enter the age: "))

if 0 <= age <= 1:
    print("Infant")
elif 2 <= age <= 4:
    print("Toddler")
elif 5 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")
else:
    print("Invalid age")


# Q.15
day_num = int(input("Enter a number (1-7): "))

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

print(days.get(day_num, "Invalid number"))

'''
