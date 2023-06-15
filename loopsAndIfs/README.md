# Intro to Flow Control

Control flow is the order in which individual statements, 
instructions, or function calls are executed or evaluated. 
The control flow of a Python program is regulated by conditional 
statements, loops, and function calls.

1. **if**, **elif**, and **else** statements
2. **for loop**
3. **while loop**

<br />

### 1. if, elif, and else statements
if statement checks if the given conditions are correct, if so, proceeds, else, does what else is 
requested
```python
number = int(input())
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")
else:
    print(number)
```

<br />

### 2. for loop
for each given instance, run the loop
```python
listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in listNum:
    if num % 2 == 0:
        print(num)
```

ranged for loop
```python
for x in range(10):
    print("Hello")
```

<br />

### 3. while loop
while true, run the loop. We can break out or continue
with the loop using **break** and **continue**
```python
x = 0
while x < 10:
    print(f"it's working -> {x}")
    x += 1
```