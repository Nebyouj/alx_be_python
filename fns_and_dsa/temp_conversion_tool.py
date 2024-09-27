FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR + 32) * celsius
     

try:
    temperature = float(input("Enter the temperature to convert: "))
    if not temperature.replace('.','',1).isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.") 
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    if unit == "c":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F") if temperature > -273.15 else print("Invalid temperature")
    elif unit == "f":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C") if temperature > -459.67 else print("Invalid temperature")
    else:
        print("Invalid unit of measurement")
except ValueError as e:
    print(e)