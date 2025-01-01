def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("Welcome to Temperature Converter!")
    choice = input("Type 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").strip().upper()

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid choice! Please restart the program.")
