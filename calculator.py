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