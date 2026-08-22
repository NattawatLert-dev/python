# conditional expression = รูปแบบย่อของ if-else ที่เขียนในบรรทัดเดียว (ternary operator)
#                          ใช้แสดงผลหรือกำหนดค่าหนึ่งในสองค่าตามเงื่อนไข
#                          X if condition else Y

num = 5
a = 6
b = 7

# print("Position" if num > 0 else "Negative")
result = "EVENT" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b

print(result)