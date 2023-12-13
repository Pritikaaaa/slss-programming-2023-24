# Function Practice
# Pritika Vats
# November 27, 2023

#question 3
pyramid = ["*", "**", "***", "****", "*****", "******"]

for row in pyramid:
    print(row)
#question 1
def stars(num_stars: int) -> str:
    """Returns a given number of stars
    
    Params:
    
    num-stars - the number of stars to return
    """ #docstring

    return "*" * num_stars

print(stars(1000))

#question 2

def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """returns the biggest of three numbers given
    
    params:
    num_one - the first number
    num_two - the second number
    num_three - the third number
    
    returns:
    the biggest of the three number"""

    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three
    
print(biggest_of_three(1000, 100, 10))
print(biggest_of_three(100, 1000, 10))
print(biggest_of_three(10, 100, 1000))

