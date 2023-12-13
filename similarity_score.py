# Comparing Similarity Scores
# Author: Pritika Vats
# Date: Nov 8, 2023

# calculate similarity scores between two people

# create two lists that represent the movie people like
pritikas_favouraite_movies = [
    "Five Feet Apart",
    "The Notebook",
    "Mean Girls",
    "Escape Room",
    "Megan"
]
pringles_favourite_movies = [
    "Tangled",
    "Escape Room",
    "The Notebook",
    "Titanic",
    "Megan"
]

# initalize a similarity score
similarity_score = 0

# iterate through all movies in first list
for movie in pritikas_favouraite_movies:
    if movie in pringles_favourite_movies:
        similarity_score += 1

# display the results
print(f"pritika and pringle have a similarity score of {similarity_score}")