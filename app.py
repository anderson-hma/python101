# # Exercise 1 Calculate area of a rectangle
# length = float(input("The length of the Rec: "))
# width = float(input("The width of the Rec: "))

# print(f"The result: {length*width}")

# # Exercise 2 Math operation
# operator = input("Today I want to execute(+ - / *): ")
# num1 = float(input("Value for the first num: "))
# num2 = float(input("Value for the second num: "))

# if operator == "+":
#     result = num1+num2
#     print(f"The result of the operation: {result}")
# elif operator == "-":
#     result = num1-num2
#     print(f"The result of the operation: {result}")
# elif operator == "/":
#     result = num1/num2
#     print(f"The result of the operation: {result}")
# elif operator == "*":
#     result = num1*num2
#     print(f"The result of the operation: {result}")
# else:
#     print("Your operator is incorrect")
#     result = "Unidentified"

# print(f"The result of the operation: {result}")

# # Conditional expression
# # X if condition else Y
# num = float(input("Value of the number: "))
# print("positive" if num > 0 else "negative")

# role = "admin"
# print("Full access" if role == "admin" else "Limited")

# # indexing with string [start : end : step]
# string = "Welcome Player 1"
# creditcardnum = "1234567890"
# print(string[0:16:2])
# print(creditcardnum[-4:])

# # loop while true: --> else break
# name = ""
# while name == "":
#     name = input("Enter you name: ")
#     print("You have not entered a name yet.")
# print(f"Hello {name}")

# # for loop continue --> skip that count
# import time
# import os
# def clear(): return os.system('cls')


# time_to_count = int(input("Enter the time in seconds: "))
# for count in reversed(range(1, time_to_count+1)):
#     print({count})
#     seconds = count % 60
#     minutes = int(count/60) % 60
#     hours = int(count / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#     clear()
# print("Time's up")
