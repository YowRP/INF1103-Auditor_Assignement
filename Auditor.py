inventory = 0
while True:
    user_input = input("Please enter the stock quantity")
    inventory += int(user_input)
    user_end = input("Do you want to add more stock? (yes/no): ")
    if user_end.lower() == "no" or user_end.lower() == "n":
        break
    else:
        continue