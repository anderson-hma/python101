# Exercise 1 Calculate area of a rectangle
length = float(input("The length of the Rec: "))
width = float(input("The width of the Rec: "))

print(f"The result: {length*width}")

# Exercise 2 Math operation
operator = input("Today I want to execute(+ - / *): ")
num1 = float(input("Value for the first num: "))
num2 = float(input("Value for the second num: "))

if operator == "+":
    result = num1+num2
    print(f"The result of the operation: {result}")
elif operator == "-":
    result = num1-num2
    print(f"The result of the operation: {result}")
elif operator == "/":
    result = num1/num2
    print(f"The result of the operation: {result}")
elif operator == "*":
    result = num1*num2
    print(f"The result of the operation: {result}")
else:
    print("Your operator is incorrect")

print(f"The result of the operation: {result}")
