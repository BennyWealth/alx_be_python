
def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        print(result)
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
