# class variables = ตัวแปรที่ใช้ร่วมกันระหว่างทุก object ของ class
#                  กำหนดไว้นอก constructor
#                  ทำให้สามารถแชร์ข้อมูลร่วมกันระหว่างทุก object ที่สร้างจาก class นั้น

from Student import Student

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_student)
 
print(f"My graduating class of {Student.class_year} has {Student.num_student} students")