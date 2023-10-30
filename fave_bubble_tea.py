# Bubble Tea Popularity Algorithm
# Author: Pritika
# Date: 27 October 2023

# Ask 5 users what their favouraite Bubble Tea place is
# Prints out a summary of the data
 
# ---------- CONSTATNTS

NUM_RESPONDENTS = 5

# -----------

# Like counter
CoCo_likes = 0         # Initalize the variable to 0
Suntea_likes = 0  
Chatime_likes = 0
BubbleQueen_likes = 0
other_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite place is
    # Store that information somewhere
    print("What's your favourite bubble tea place?")
    fave_place = input().strip(",.?! ").lower()

    # Tally or counting algo
    if fave_place == "coco":
        CoCo_likes += 1 
    elif fave_place == "suntea":
        Suntea_likes += 1            # alternate for above
    elif fave_place == "chatime":
        Chatime_likes += 1 
    elif fave_place == "bubblequeen":
        BubbleQueen_likes += 1
    else:
        other_likes += 1

# Print out a summary
print(f"CoCo likes: {CoCo_likes} votes | {CoCo_likes / NUM_RESPONDENTS * 100}%")
print(f"Suntea likes: {Suntea_likes} votes | {Suntea_likes / NUM_RESPONDENTS * 100}%")
print(f"Chatime likes: {Chatime_likes} votes | {Chatime_likes / NUM_RESPONDENTS * 100}%")
print(f"BubbleQueen likes {BubbleQueen_likes} | {BubbleQueen_likes / NUM_RESPONDENTS * 100}%")
print(f"other likes: {other_likes} votes | {other_likes / NUM_RESPONDENTS * 100}%")

