# SFU's Best
# Author: Pritika Vats
# Date: Nov 10, 2023

# load data from .csv file
# Read it in a meaningful way
# Link our similarity score algo to the data

# Open the file
with open("./data.csv") as f:
    # Read the first line of data

    f.readline()

# Create a profile for someone that shows their favourite place at SFU
profile = [
    "Bubble World",
    "Chef Hung",
    "Pizza Hut",
    "Quesada (Cornerstone)",
    "Subway"
]

# Initalize our top similarity score and their name
top_sim_score= 0
top_sim_name = ""
lowest_sim_score = 1_000_000
lowest_sim_name = ""

with open("./data.csv") as f:
    # throw away the header
    header = f.readline()

    # For every line of data in the file (string)
    for line in f:
        # convert the line of data into a list
        current_likes = line.split(",")

        # initalize the CURRENT similarity score
        # store the current persom's name
        current_sim_score = 0
        current_name = current_likes[1]

        # for every item in our profile 
        for item in profile:
            if item in current_likes:
                current_sim_score += 1

        # print the current sim score
        print(f"{current_name}- score: {current_sim_score}")

        # if the current score is greater > than the top sim score
        if current_sim_score > top_sim_score:
            top_sim_score = current_sim_score
            top_sim_name = current_name

        if current_sim_score < top_sim_score:
            lowest_sim_score = current_sim_score
            lowest_sim_name = current_name

print("TOP SIMILAR PERSON")
print(f"{top_sim_name} - Score: {top_sim_score}")

print("LEAST SIMILAR PERSON")
print(f"{lowest_sim_name} - Score: {lowest_sim_score}")