#PROBLEM 1
student_data = {
    "Ali B.": {"Physics": 80, "Math": 90},
    "Aisha G.": {"Physics": 78, "Math": 89},
    "Nur D.": {"Physics": 60, "Math": 76},
    "Mehmet C.": {"Physics": 100, "Math": 84},
    "Usama H.": {"Physics": 98, "Math": 90},
    "Hamza K.": {"Physics": 70, "Math": 80},
    "Farouk T.": {"Physics": 67, "Math": 73},
    "Deniz A.": {"Physics": 99, "Math": 91},
    "Yasmine R.": {"Physics": 87, "Math": 100},
    "Ahmet S.": {"Physics": 93, "Math": 91}
}


for student, grades in student_data.items():
    print(f"Student: {student}, Physics Grade: {grades['Physics']}, Math Grade: {grades['Math']}")

#PROBLEM 2
def calculate_product_sum(numbers):
    product = 1
    total_sum = 0
    
    for num in numbers:
        product *= num
        total_sum += num
    
    return product, total_sum


numbers_list_1 = [101, 64]
numbers_list_2 = [3.50, -5, 13.1111]
numbers_list_3 = [-55.13, 23]


product_1, sum_1 = calculate_product_sum(numbers_list_1)
product_2, sum_2 = calculate_product_sum(numbers_list_2)
product_3, sum_3 = calculate_product_sum(numbers_list_3)

print("Numbers List 1 - Product:", product_1, ", Sum:", sum_1)
print("Numbers List 2 - Product:", product_2, ", Sum:", sum_2)
print("Numbers List 3 - Product:", product_3, ", Sum:", sum_3)
