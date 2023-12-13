In Python, data can be grouped in categories called Type.

| Name             |  Example    |
| ---              | ---         |
| string           | "Hello"     | 
| list             | [1, 2 ,3 ,4]|
| integers or `int`  | 1  -10  23  |
| float            | 3.5 -3.5 1.0 |
| `bool` or   boolean| True False  |



An example of using these types of data:


```python
favourite_food = "tempura"
my_age = 16.0   #my_age is of type
```

## Type Conversion

in python, there are some *special functions* that allow us to change the type of something.
```python
intro_string = "My age is "    # Type string
my_age = 15                    # Type int

#aside
"my name is" + "slim shady"    # My name isslimshady

print(into_string + my_age)    # THIS BREAKS
```

we can use the following *built in* function to covert into different types:
```python
int()
float()
str()

list()

```

we can fix the example above in this way:

```python
intro_string = "my age is "
my_age = 16

print(intro_string + str(my_age))
print(intro_string + " " + str(my_age))
print(f"{intro_string} {my_age}")

```