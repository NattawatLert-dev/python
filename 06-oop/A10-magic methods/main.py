# Magic methods = หรือเรียกว่า Dunder methods (double underscore) เช่น __init__, __str__, __eq__
#                 จะถูกเรียกใช้อัตโนมัติเมื่อใช้คำสั่งหรือการทำงานบางอย่างของ Python
#                 ช่วยให้เราสามารถกำหนดหรือปรับแต่งพฤติกรรมของ Object ได้

from student import Student

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)

print(student1)
print(student1 == student2)
print(student1 > student2)
print("Sp" in student1)