num1 = int(input("Enter the first numbers: "))
num2 = int(input("Enter the second numbers: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        print(f"The result is {num1 / num2}") if num2 != 0 else print("Error! Division by zero")
    case _:
        print("Invalid operation.")
    