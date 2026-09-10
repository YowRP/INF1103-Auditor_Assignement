inventory = 0
while True:
    user_input = input("Please enter the stock quantity")

    if not user_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    elif int(user_input) < 0:
        print("Invalid input. Please enter a non-negative number.")
        continue
    
    inventory += int(user_input)

    user_end = input("Do you want to add more stock? (yes/no): ")
    if user_end.lower() == "no" or user_end.lower() == "n":
        break
    else:
        continue

    if inventory >= 500 :
        print("ALERT! Stock quantity has reached or exceeded 500 units.")
        break
    

print ("Total stock quantity:", inventory)


    