while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    if num1 == num2 == num3 == 0:
        break

    total = num1 + num2 + num3

    if num1 == num2 == num3:
        total *= 3

    print(f"The sum is: {total}")
