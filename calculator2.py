#def main, lets CLI.py call this program and run it via CLI


def main():

    num1 = float(input("Enter a number: "))
    operator = input("Enter an operator: ")
    num2 = float(input("Enter another number: "))



    ############################################
### Ignore the comments below ###### 
    #simple algebra, this is not CAS and will not accept () ^x and other algebra symbols 
    # however, it will give the variable a value, essentially 1, so say that X = 1, you can add X into the equation doing simple algebra using charachters in math

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
    













#################################
