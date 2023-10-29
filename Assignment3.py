#Problem1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("First Name:", first_name)
print("Last Name:", last_name)

#Problem2
student_id = input("Enter your student ID: ")

previous_digit = None


for char in student_id:

    current_digit = int(char)
    
    print("Current Number", current_digit, "Previous Number", previous_digit, end=' ')
    
    if previous_digit is not None:
        sum_result = current_digit + previous_digit
        print("Sum:", sum_result)
    else:
        print("Sum: N/A")  
    
    previous_digit = current_digit
