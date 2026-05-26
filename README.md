# Edutech Solution Python Development Internship - Task 2

**Task 2:** Control Flow & Logic Building

**Objectives:**
if-elif-else
loops (for, while)
nested loops
logical conditions
simple calculator program

### `if-elif-else logic.py`
```python
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

### `nested loop.py`
```python
for i in range(1, 5):
    for j in range(1, 5):
        print(f"i: {i}, j: {j}")
```

### `calculator.py`
```python
# Simple Calculator Program

print("Simple Calculator")

while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == '5':
        print("Exiting calculator...")
        break

    # Invalid choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Try again.")
        continue

    # User input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Operations
    if choice == '1':
        result = num1 + num2
        print("Result =", result)

    elif choice == '2':
        result = num1 - num2
        print("Result =", result)

    elif choice == '3':
        result = num1 * num2
        print("Result =", result)

    elif choice == '4':
        if num2 == 0:
            print("Division by zero is not allowed!")
        else:
            result = num1 / num2
            print("Result =", result)
```


### Logic Flow Diagram
START
             |
             v
      Display Menu
             |
             v
      Enter Choice
             |
     ----------------
     |              |
   Choice=5? ---- YES ----> END
     |
    NO
     |
 Invalid Choice?
     |
  YES ---> Show Error ---> Menu
     |
    NO
     |
 Enter Numbers
     |
 Perform Operation
     |
 Display Result
     |
     v
    Menu

### What is logical branching in Python?
Logical branching means making decisions in a program using conditions such as if, elif, and else.

Example:
```python
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

### What is the difference between `break` and `continue`?

| Feature        | break                 | continue                 |
| -------------- | --------------------- | ------------------------ |
| Purpose        | Stops loop completely | Skips current iteration  |
| Loop Execution | Terminates loop       | Continues next iteration |
| Used In        | for / while loops     | for / while loops        |4

Example of break:
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

Output:1 2 

Example of continue:
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:1 2 4 5

### What is an infinite loop?
An infinite loop is a loop that never stops because the condition always remains True.
In this program, we use while True which creates an infinite loop. It keeps running until the user chooses option 5, which triggers a break statement to exit the loop.

Example:
```python
# Infinite loop example

while True:
    print("This is an infinite loop!")
    break
```

## Submitted by
Shrey Gamit
P.P. Savani University
CSE



