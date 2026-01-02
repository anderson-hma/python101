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
# credit_card_num = "1234567890"
# print(string[0:16:2])
# print(credit_card_num[-4:])

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

# collection
# list  = [] ordered, changeable, ok with duplicate
# set   = {} unordered, immutable, add and remove - no duplicate
# tuple = () ordered, unchangeable, ok with duplicated - fast
# shopping cart

food_price = {}

while True:
    food = input("Enter the food name (q to quit): ").strip().lower()
    if food == "q":
        break

    price = input("Enter the price: ").strip()
    if price == "q":
        break
    food_price[food] = float(price)

for food, price in food_price.items():
    print(f"{food} costs ${price}")

while True:
    # --- Search by name ---
    search_by_name = input("Name to search (q to quit): ").strip().lower()
    if search_by_name == "q":
        break
    elif search_by_name != "":
        price = food_price.get(search_by_name)
        if price is not None:
            print(f"{search_by_name} costs {price}")
        else:
            print("Not found")

    # --- Search by price ---
    search_by_price = input("Price to search (q to quit): ").strip()
    if search_by_price == "q":
        break
    elif search_by_price != "":
        search_by_price = float(search_by_price)
        found = False

        for food, price in food_price.items():
            if price == search_by_price:
                print(f"{food} costs {price}")
                found = True

        if not found:
            print("Not found")
