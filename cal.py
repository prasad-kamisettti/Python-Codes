
#Get user input
try:
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # division by zero error
        if num2 == 0:
            result = "Error! Division by zero is not allowed."
        else:
            result = num1 / num2
    else:
        result = "Error! Invalid operator."

    #Display the result
    # We only print the full equation if the operator was valid
    if isinstance(result, (int, float)):
        print(f"\n Result: {num1} {operation} {num2} = {result}\n")
    else:
        print(result)
