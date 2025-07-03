print("=== Temperature Converter ===")

# Celsius to Fahrenheit
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit:.2f}°F")
except ValueError:
    print("Invalid input! Please enter a numeric value for Celsius.")

# Fahrenheit to Celsius
try:
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_converted = (fahrenheit_input - 32) * 5/9
    print(f"{fahrenheit_input}°F is {celsius_converted:.2f}°C")
except ValueError:
    print("Invalid input! Please enter a numeric value for Fahrenheit.")