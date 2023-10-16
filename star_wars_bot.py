# Star Wars Bot
# Author: Pritika Vats
# Date: 16 October

import time 

# greet the user
print("Hey there I am a STAR WARS BOT!")

# Pause for a second
time.sleep(2)

# Decide if the user is on the light side or the dark side
print("I will decide if you can join the Dark side.")
time.sleep(1)

# Ask the question
like_red = input("Is red your favourite color?")

# Pause for a second
time.sleep(1)

like_capes = input("Do you like capes?")
time.sleep(1)

# If they reply yes to either question
# Send them to the dark side
# Else they should be in the light side
if like_red == "yes" or like_capes == "yes":
    print("Dark side it is!")
else:
    print("You're part of the light side!")


# different response
# Ask the question

