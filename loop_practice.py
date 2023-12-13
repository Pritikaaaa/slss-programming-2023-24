# Loop Practice
# Author: Pritika Vats
# Date: 10 October 2023

import time

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
 #   time.sleep(1)

# Implement linear search
names = ['Anthony Maldonado', 'Randy Love', 'Christopher Valdez', 'Rodney Odom', 'Kimberly Ramos', 'Lisa Ray', 'Kevin Terry', 'Gregory Romero', 'Debbie Harris', 'Edwin Hall', 'Mark Myers', 'Lisa Long', 'Stephanie Watson', 'Katherine Fields', 'Kathryn Olson', 'Maurice Baxter', 'Russell Caldwell', 'Heather Griffin', 'Kara Lane', 'Mark Tucker', 'Kathryn Rodriguez', 'Rachael Daniels', 'Debra Whitaker', 'Angela Neal', 'Michelle Hall', 'Jessica Olson', 'Lynn Jensen', 'Marc Ray', 'Valerie Harris', 'Tina Webb', 'Donna Green', 'Derek Mcgee', 'Tammy Hall DVM', 'Christopher Johnston', 'Eric Smith', 'Matthew Lopez', 'Mary Smith', 'Dr. Heather Ramos MD', 'Eric Johnson', 'Dylan Alvarado', 'Aaron Huff', 'Robin James', 'Sandra Stevens', 'Scott Thomas', 'Philip Nelson', 'Marcus Martin', 'Mary Alexander', 'Jason James', 'Samantha Burch', 'Jessica Martinez', 'Jose Wright', 'Zachary Pineda', 'William Ramos', 'Shelby Hughes', 'Melanie Moore', 'Kimberly Fowler', 'Jordan Jones', 'Brenda Anderson', 'Russell Coleman', 'Jeremy Snow', 'Billy Wu', 'Jesse Rodriguez', 'Andrew Shea', 'Jason Castillo', 'Donald Abbott', 'Richard Cervantes Jr.', 'Jeffrey Powell', 'Angel Fernandez', 'Michelle Donovan', 'Mr. Michael Wagner DDS', 'Kimberly Gonzalez', 'Thomas Smith', 'Nichole Barnes', 'Shelly Clark', 'Ashley Ortiz', 'Jessica Lam', 'Kimberly Ray MD', 'Mason Kennedy', 'Whitney Harrington', 'Nicole Tran', 'Robert Montgomery', 'Ryan Gardner', 'Kimberly Silva', 'Stephanie Rivera', 'William Santos', 'Ashley Mcclain', 'Sophia Williams', 'Kevin Herring', 'Tyrone Leonard', 'Carolyn Jones', 'Stephanie Willis', 'Jon Lang', 'Tammy Porter', 'Robert Garcia', 'Casey Brown', 'Benjamin Aguilar', 'Nancy Norman', 'Aaron Peters', 'Blake Graham', 'Noah Harper DDS', 'Dwayne Ortiz', 'Melissa Padilla', 'Rebecca Jones', 'Michael Wood', 'Daniel Bean', 'Alexander Kaufman', 'Michael Higgins', 'Richard Bailey', 'Jay Cisneros', 'Lisa Acevedo', 'Sarah Hernandez', 'Bryan Jones', 'Mark Kennedy', 'Robert Caldwell', 'Larry Wolf', 'Robert Adkins', 'Wanda Doyle', 'Thomas Brown', 'Kevin Key', 'Stacey Fisher', 'Amber Hart', 'Paul Russell', 'Jacqueline David', 'Shannon Parker', 'Lisa Sanchez', 'Jennifer Atkins', 'Jason Woods', 'Richard Garcia', 'Luis Williams', 'Marco Weaver', 'Amy Hayes', 'Elizabeth Doyle DDS', 'Nicole Smith', 'Karen Thomas', 'Randy Reese', 'Deanna Rodriguez', 'Christian Conway', 'Craig Doyle', 'Dennis Oneill', 'Diane Jordan', 'Patrick Holder', 'Christina Thompson', 'Deanna Lee', 'Kathleen Davis', 'Brian Cox', 'Kristen Thomas', 'Samantha Smith', 'William Moss', 'Matthew Flowers', 'Megan Powell', 'Richard Williamson', 'Cindy Glenn', 'John Taylor', 'Nathaniel Lee', 'Sara Glover', 'James Jackson II', 'Carlos Henderson', 'Edward Holder', 'Whitney Hansen', 'Matthew Jacobs', 'Raymond Rodriguez', 'Christy Kennedy', 'Lisa Johnson', 'Mark Harris', 'Stephen Bowers', 'Derrick Brown', 'Stephen Schroeder', 'Martin Lawrence', 'Brian Reed', 'Trevor Booker', 'Ruben Johnson', 'Jeffrey Griffith', 'William Townsend', 'Cynthia Park', 'Carla Yang', 'Oscar Hartman', 'Shawn Hendricks', 'Timothy Oconnor', 'Gina Robertson', 'Jennifer Rodriguez', 'Jared Harris', 'Austin Austin', 'Nathan Golden', 'Samantha Flores', 'Alexis Jones', 'Susan Rice', 'Randall Holmes', 'Connie Johnson', 'Carol Young', 'Brandon Norris', 'Timothy Lester', 'Dustin Mccarthy', 'Tammy Brock', 'Heather Cummings', 'John Moreno', 'Dawn Berry', 'Jeffrey Montes', 'Joshua Smith', 'Alexa Barber', 'Mark Lewis']
search_name = "Randy Love"

for name in names:
    # check if it's the name we want
    if name == search_name:
        print(f"we found {search_name}!!")

        break # STOPS THE LOOP

else:
    print(f"we didn't find {search_name}")

# Print out Mr Ubial is cool 20 times
for _ in range(20):
    print("Mr Ubial is cool")

# repeat something 5 times and we want to keep track of how many iterations we completed
for i in range(5):
	print(i)
     
for i in range(10):
     print(f"{i + 1}. the quick brown fox")
     
for i in range(1, 100):
    print(i)

# can we count by other number
for i in range(1, 101, 2):
    print(i)

#1. print all even numbers between
#   1200 and 1500 inclusive
#   use a for loop
for i in range(1200, 1501, 2):
    print(i)


#2. print all odd numbers between
#   -150 and 0  inclusive
for i in range(-149, 1, 2):
    print(i)
