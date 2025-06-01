while True:
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        operator = input("Choose the operation (+, -, *, /): ")

        match operator:
            case "+":
                result = first_number + second_number
                print(f"The result is {result}")
            case "-":
                result = first_number - second_number
                print(f"The result is {result}")
            case "*":
                result = first_number * second_number
                print(f"The result is {result}")
            case "/":
                if second_number == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = first_number / second_number
                    print(f"The result is {result}")
            case _:
                print("Enter a valid operator (+, -, *, /)")
    except ValueError:
        print("Enter a valid integer.")


