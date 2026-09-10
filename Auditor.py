
while True:
    inventory = []
    user_input = input("Enter the stock quantity")
    inventory.append(user_input)
    user_end = input("Do you want to add more stock? (yes/no): ")
    if user_end.lower() == "no" or user_end.lower() == "n":
        break
    else:
        continue

print(inventory)
