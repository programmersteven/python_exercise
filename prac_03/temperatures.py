MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(celsius_to_fahrenheit(celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(fahrenheit_to_celsius(fahrenheit))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


    print("Thank you.")
main()
