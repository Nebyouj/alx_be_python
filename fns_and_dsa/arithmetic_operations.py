
def perform_operation(num1, num2, operation):
    
    
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0: pass
            elif num2 == 0: return ZeroDivisionError
            return num1 / num2 
        case "==":
            return True if num1 == num2 else False
        case _:
            print("Invalid operation.")