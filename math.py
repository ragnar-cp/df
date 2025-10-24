try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))

    if num2 != 0:
        result = num1 / num2
        print("Division result:", result)
    else:
        print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers.")
