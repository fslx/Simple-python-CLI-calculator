#def main, lets CLI.py call this program and run it via CLI


def main():

    num1 = float(input("Number: "))
    operator = input("+ - / *: ")
    num2 = float(input("Number: "))


    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    else:
        return main()
    












