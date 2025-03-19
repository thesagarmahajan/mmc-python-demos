""" try:
    # ValueError
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    # ZeroDivisionError
    ans = num1/num2
    print(ans)
except ValueError:
    print("Please enter only Numeric Values!")
# except ZeroDivisionError:
#     print("Haven't you attended school? Can't divide a number by zero you fool!")
except Exception as e:
    print("Some unknown exception occured. Please contact developer.")
    # log(e.__doc__)
finally:
    print("Ending") """



# Reusable Method / Library Method
def division(dividend, divisor):
    if divisor==0:
        raise ZeroDivisionError("Cannot Divide by Zero Mathematically.")
    return dividend/divisor

# Application
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

try:
    division(n1, n2)
except ZeroDivisionError:
    print(ZeroDivisionError.__doc__)
