num_1 = float(input("Enter number 1: "))
num_2 = float(input("Enter number 2: "))

if num_2 != 0:
    result = num_1 / num_2
    print("Result: {:.2f}".format(result))
else:
    print("Cannot divide by zero.")