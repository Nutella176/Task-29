def get_equation():
    """Function that asks user for 2 numbers and 1 operator, calculates the result and writes it in input.txt."""
    while True:
        try:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("The value entered is not a number, try again.")
            continue

    while True:
        operator = input("Please enter one of the following operatiors (+, -, *, /): ")
        equation = f"{num1} {operator} {num2} = "
        if operator == "+":
            result = num1 + num2
            print(equation, result)
            break
        elif operator == "-":
            result = num1 - num2
            print(equation, result)
            break
        elif operator == "*":
            result = num1 * num2
            print(equation, result)
            break
        elif operator == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Cannot divide by zero")
                continue
            print(equation, result)
            break
        else:
            try:
                raise ValueError("Invalid operator")
            except ValueError as e:
                print(e)
                continue

    with open("input.txt", "a") as input_file:
        input_file.write(f"{equation} {result}\n")


def main_menu():
    """Function that gives user the option to use the calculator in get_equation function, or to read from a new file"""
    while True:
        selection = input(
            "Enter 'c' to enter equations manually or 'f' to read from file: "
        )
        if selection == "c":
            get_equation()

        elif selection == "f":
            while True:
                file_name = input("Enter file name followed by '.txt': ")
                try:
                    file = open(f"{file_name}", "r")
                    break
                except FileNotFoundError:
                    print(
                        "The file that you are trying to open does not exist, try again."
                    )
                    continue
            f_read = file.readlines()
            for line in f_read:
                print(line)
            file.close()

        else:
            print("Incorrect selection, try gain.")
            continue


main_menu()
