
def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        print(result)
    except ValueError:
        print("Enter a numeric value")
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
