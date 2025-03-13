print("\n🖩 Welcome to the Basic Calculator! 🖩")

# Getting the User input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ").strip()

# Performing operation using Dictionary
operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2 if num2 != 0 else "Error! Division by zero is not allowed."
}

result = operations.get(operation, "Invalid operation! Please enter +, -, *, or /.")


#Displaying the result
print(f"\nResult: {num1} {operation} {num2} = {result}")
