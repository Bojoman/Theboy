# Basic Calculator Program

def calculator(predefined_inputs):
    print("Welcome to the Basic Calculator!")

    # Input numbers and operation from the predefined inputs
    try:
        num1 = float(predefined_inputs.get("num1", 0))
        num2 = float(predefined_inputs.get("num2", 0))
        operation = predefined_inputs.get("operation", "+")

        # Perform the operation and display the result
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please choose from +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please provide numeric values for the numbers.")

# Example usage of the calculator
if __name__ == "__main__":
    # Simulate predefined inputs
    inputs = {
        "num1": 10,
        "num2": 5,
        "operation": "/"
    }
    calculator(inputs)
