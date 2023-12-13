# Chip Rater
# Author: Pritika Vats
# Date: 1 Nov 23

# Interview people about their
# perception of how delicious chips are
# based on a set of questions
# in the end, we'll give an aggregate score

# greet the user
print("Please answer the following questions based on the chip that you just ate.")

# create a list of questions to ask
questions = [
    "How crispy is the chip on a scale from 1 to 5? 5 is very crispy. 1 is mushy",
    "How would you rate the taste from 1 to 5. 5 is the best taste ever. 1 is I would rather eat dirt.",
    "From 1 to 5, how you would rate the packaging. 5 is I would buy this just for the packaging. 1 is someone was paid to put this together?"
]

final_score = 0

# ask the question to the users
for question in questions:
    print(question)


    # store their response
    rating = int(input().strip(",.?!"))
    final_score += rating 

# do some math - average
average_score = final_score / len(questions)

# print the results to the users
print(f"the average score of this chip is: {average_score:.2f}/ 5")