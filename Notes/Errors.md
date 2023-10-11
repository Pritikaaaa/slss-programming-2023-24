# Syntax Errors
These type of errors are ones where you run your code and something breaks

Syntax errors are relatively easy to fix.

Syntax errors happen when we don't follow the rule correctly.

some examples are when we forget a closing bracket
# Semantic Errors
Semantic errors are much more challenging to squash.

Semantic errors are where your code doesn't mean what you actually mean.

```python
user_response = input("Do you like to eat food? ")

if user_response == "yes":
	print("You passes the human test.")
else:
	print("You must be some sort of robot.")
```

The problem with the above code is subtle. What Mr. Ubial mean is that if the user answers with ANYTHING affirmative the code should go into the _"yes"_ block.

One way to solve this problem [[Strings#string methods]]. we can use.lower() to catch all permutations of capital letters.

```python
user_response = input("Do you like to eat food? ")

if user_response.lower() == "yes":
	print("You passes the human test.")
else:
	print("You must be some sort of robot.")
```