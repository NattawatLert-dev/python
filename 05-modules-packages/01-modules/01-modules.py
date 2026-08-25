# module = ไฟล์ที่ประกอบด้วยโค้ดที่เราต้องการนำมาใช้ในโปรแกรม
#          ใช้ 'import' เพื่อนำเข้า module (ที่มีอยู่ใน Python หรือที่เราสร้างเอง)
#          มีประโยชน์ในการแบ่งโปรแกรมขนาดใหญ่ออกเป็นไฟล์แยกกันทำให้สามารถนำโค้ดกลับมาใช้ซ้ำได้

# help(help("modules"))

# import math
import math as m
print(m.pi)

a, b, c, d = 1, 2, 3, 4
print(m.e ** a)
print(m.e ** b)
print(m.e ** c)
print(m.e ** d)

#Ex.1

import example

result = example.pi
print(result)

result1 = example.square(3)
print(result1)

