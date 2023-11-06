# McDolands
# Author: Pritika Vats
# Date: Nov 6, 2023

# greet the users
print("Welcome to McDolands ")

# ask for the order
burger_order = input("Would you like a burger for $5?  (Yes/No) ")

fries_order = input("Would you like fries for $3?  (Yes/No) ")


if burger_order.lower() == "yes" and fries_order.lower() == "yes" :
    total_cost = 5 + 3 + 1.12                 #14% of 8 = 1.12
    # print out the total cost
    print(f"Your total is ${total_cost}")

elif burger_order.lower() == "yes" and fries_order.lower() == "no" :
    total_for_burger = 5 + 0.7               #14% of 5 = 0.7
     # print out the total cost
    print(f"Your total is ${total_for_burger}")

elif burger_order.lower() == "no" and fries_order.lower() == "yes":
    total_for_fries = 3 + 0.42                #14% of 3 = 0.42
     # print out the total cost
    print(f"Your total is ${total_for_fries}")

else:
    burger_order.lower() == "no" and fries_order.lower() == "no"
    print("Your total is $0. ")
