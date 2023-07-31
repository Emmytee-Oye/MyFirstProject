



def calculator():







    print("Select an operation:")

    print("1. Addition")

    print("2. Subtraction")

    print("3. Multiplication")

    print("4. Division")



    choice = input("Enter your choice (1/2/3/4): ")







    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))





    if choice == "1":

        result = num1 + num2

        print("Result:", result)

    elif choice == "2":

        result = num1 - num2

        print("Result:", result)

    elif choice == "3":

        result = num1 * num2

        print("Result:", result)

    elif choice == "4":

        result = num1 / num2

        print("Result:", result)

    else:

        print("Invalid choice")







    continue_calculation = input("Do you want to perform another calculation? (yes/no): ")

    if continue_calculation.lower() == "yes":

        calculator()

    else:

        print("Calculator closed.")






calculator()





