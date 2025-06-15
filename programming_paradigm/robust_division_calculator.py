
def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        print(f"The result of the division is {result:}.1f")
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
