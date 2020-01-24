print(r"Run the calculator: \n\
please note that this calculator does not support CAS and advanced arithemetic. \n\
Do you want to run the calculator? y or n: ")


option = input("")



if option == "y":
    import calculator2
    calculator2.main()
else:
    exit()    



#GUI options here:
