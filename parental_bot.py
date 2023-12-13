# Parental Bot
# Author: Pritika Vats
# Date: November 17, 2023

tasks_to_do = [
input("Did you eat? "),
input("Did you study? "),
input("Did you do your laundry? "),
input("Did you call your grandma? "),]

good_kid_score = 0 

for task in tasks_to_do:
    if "yes" in tasks_to_do:
        good_kid_score += 1 
    if "no" in tasks_to_do:
        good_kid_score -= 1

if good_kid_score == 0:
    print("I'm coming over!!!!!!!!!!!!!!!!")

elif good_kid_score == 1 or 2:
    print("Ok. you better do the rest")

elif good_kid_score == 3 or 4:
    print("Good!!")