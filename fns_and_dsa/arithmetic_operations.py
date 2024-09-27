def perform_operation(num1:float,num2:float,operation:str):
    
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            return num1 / num2 if num2 != 0 else print("Error! Division by zero")
        case _:
            print("Invalid operation.")