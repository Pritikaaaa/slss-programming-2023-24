# Loop Practice
# Author: Pritika Vats
# Date: 10 October 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "french fries"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g. 
#       * hot wheels
#          ----
#       * lego
#          ----
#          etc.

for item in groceries:
    print(f"* {item}")
    print(f"  ----")

# using the above method, create the thing below;
# *
# **
# ***
# ****
# *****
# ******

pyramid = ["*", "**", "***", "****", "*****", "******"]

for row in pyramid:
    print(row)

# countdown for new year
countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy new year!"]

for numbers in countdown:
    print(numbers)
    print(f"-")
