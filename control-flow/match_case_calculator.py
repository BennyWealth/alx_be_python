while True:
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        operator = input("Choose the operation (+, -, *, /): ")
        match operator:
            case "+":
                    print(f"The result is { first_number + second_number}")
            case "-":
                    print(f"The result is { first_number - second_number}")
            case "*":
                    print(f"The result is { first_number * second_number}")
            case "/":
                    print(f"The result is { first_number / second_number}")
            case _:
                print("Enter the correct operator ")
    except ValueError:
          print("Enter an integer: ")


