FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)
def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius) + 32


temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
match unit:
    case "c":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    case "f":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    case"_":
        print("Invalid unit of measurement")