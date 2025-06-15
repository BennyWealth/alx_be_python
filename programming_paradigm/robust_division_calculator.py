
def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        print(result)
    except ValueError:
        print("Enter a numeric value")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
