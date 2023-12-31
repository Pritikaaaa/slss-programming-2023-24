# Functions

A function is a block of code that can be reused over and over again.

We can input data to the function. We refer to the data as **parameters**.

We describe the parameters in the docstring. A docstring (is short for documentation string) tells a human what the purpose of the function is.

We use the term **arguments** to describe the ACTUAL data that we put into the function.

```python
def area_of_a_square(sidelength: float):
	"""Calculate and print the area of a square.
	Results are in units squared.

	Params:

	sidelength - length of one side of the square
	"""

	area = sidelength ** 2

	print(f"The area of a square with side length {sidelength} is: {area} square units.")

area_of_a_square(12.2)
```

##  Functions with Return Values



## Recursion
recursion is an elegant way to repeat patterns.

Fractals are examples of patterns that can be described recursively.

A recursive function must have three parts:

1. a function
2. a call to itself inside of the body code block
3. a base case. the base case is where the function stops calling itself.

# Fibonacci Sequence and Recursion
```
Fibonacci Sequence:
1,1,2,3,5,8,13,21,34,55.........
```