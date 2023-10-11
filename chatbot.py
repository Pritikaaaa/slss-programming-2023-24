# Chatbot
# Name: Pritika
# Date: 20 September 2023

import random
import time

# greet the user 
print("Hello there! 🤗")

# Pause for 1.5 seconds
time.sleep(1.5)
print("I'm a crude chatbot, here to talk to you")
time.sleep(1.5)

# greet the user's anme and store it in a variable
user_name = input("So... what's your name?")

#Respond with the user's name in a friendly way
print(f"It's good to meet you, {user_name}")

# Ask the user what their favouraite food is
fave_food = input("what's your favouraite food? ")

# if their favouraite food is sushi, reply with yum
if fave_food == "sushi":
    print("yum! 🍣") 
    print("I think I love sushi!") 
elif fave_food == "burger" or fave_food == "Burgers":
    print("🍔")  
    print("burgers, I hear are delicous! ")  
else: 
    # Create a list of possible responses
    list_of_food_response = [
        f"ohhh, I've never had {fave_food} before.", 
        "MmmmMMMMm. That sounds good!",
        "I heard that's delicious!!!",
        "omgg cool!!"
        ]

    # Choose one of those respones randomly
    random_food_response = random.choice(list_of_food_response)

    # Print out that chosen response
    print(random_food_response)
