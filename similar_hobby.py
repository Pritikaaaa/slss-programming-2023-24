# Hobby Similarity Score
# Author: Pritika Vats
# November 15, 2023

print("Please enter hobbies, seperated by spaces")

Person_1 = ["skiing", "drawing", "coding" ]
Person_2 = ["drawing", "coding", "crocheting"]

# initialize the similarity score
similarity_score = 0

# iterate through the list
for hobby in Person_1:
    if hobby in Person_2:
        similarity_score += 1

# display the results
print(f"You have {similarity_score} hobbies in common.")
 