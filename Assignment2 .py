#Problem=1 
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


#Problem=2
import random

print("Welcome to the Smart Number Guessing Game!")
print("I will guess the number you're thinking of in 5 questions or less.")

low = 0
high = 100
attempts = 0

while True:
    guess = random.randint(low, high)
    print(f"Is your number {guess}?")
    response = input("Enter 'h' for higher, 'l' for lower, or 'c' for correct: ").lower()

    if response == 'c':
        print(f"Great! I guessed your number {guess} in {attempts} attempts!")
        break
    elif response == 'h':
        low = guess + 1
    elif response == 'l':
        high = guess - 1
    else:
        print("Please enter 'h', 'l', or 'c' as your response.")

    attempts += 1

    if attempts >= 5:
        print("I couldn't guess your number in 5 questions. You win!")
        break
