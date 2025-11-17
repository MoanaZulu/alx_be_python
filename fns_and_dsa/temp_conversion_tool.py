# Temperature Conversion Tool

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("25°C =", celsius_to_fahrenheit(25), "°F")
    print("77°F =", fahrenheit_to_celsius(77), "°C")
