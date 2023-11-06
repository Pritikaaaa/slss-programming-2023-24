# Olympic Judging
# Author: Pritika Vats
# Date: Nov 3, 2023


NUM_RESPONDENTS = 5                                       

final_score = 0

for _ in range(NUM_RESPONDENTS):
  #print out the scores
    score = int(input("write down your score"))

    final_score += score

#do math
total_score = final_score / 5

#print out the final response
print(f"Your Olympic score is {total_score}")
