"""A program that converts between degrees Fahrenheit and degrees Celsius."""


def main():
    """Main function of a program that asks whether to convert from degrees Fahrenheit to Celsius or the other way around,
    then asks to provide the number of chosen degrees, performs the calculation and returns the result."""

    choice = int(input("Input '1' to convert from Fahrenheit to Celsius, input '2' to convert from Celsius to Fahrenheit.\nYour choice: "))

    if choice == 1:
        fahrenheit = float(input("How many degrees Fahrenheit?\nYour input: "))
        celsius = (fahrenheit - 32) * (5 / 9)
        print(f"{fahrenheit} degrees Fahrenheit equal {celsius} degrees Celsius.")
    elif choice == 2:
        celsius = float(input("How many degrees Celsius?\nYour input: "))
        fahrenheit = (celsius * (9 / 5)) + 32
        print(f"{celsius} degrees Celsius equal {fahrenheit} degrees Fahrenheit.")
    else:
        print("Wrong input.")


if __name__ == "__main__":
    main()
