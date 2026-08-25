# List comprehension = วิธีแบบกระชับในการสร้าง List ใน Python
#                      เขียนสั้นและอ่านง่ายกว่า loop แบบปกติ
#                      [expression for value in iterable if condition]

#Ex.1
double = []
for x in range(1, 11):
    double.append(x * 2)

print(double)

doubles = [x * 2 for x in range(1, 11)]
triple = [x * 3 for y in  range(1, 11)]

#EX.2
fruits = ["apple", "orange", "banana", "coconut"]
uppercase_fruits = [x.upper() for x in fruits]
first_letter = [y[0] for y in fruits]

print(uppercase_fruits)
print(first_letter)

#EX.3
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num > 0] # [1, 3, 5]
positive_nums2 = [num > 0 for num in numbers] # [True, False, True, False, True, False]
print(positive_nums)

#Ex.3
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grades >= 50]