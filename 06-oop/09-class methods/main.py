# Class methods = ใช้สำหรับการทำงานที่เกี่ยวข้องกับ Class โดยตรง
#                 รับ (cls) เป็น parameter ตัวแรก ซึ่งใช้แทน Class เอง

# Instance methods = เหมาะสำหรับการทำงานกับข้อมูลของ Object (Instance) ของ Class
# Static methods = เหมาะสำหรับฟังก์ชันทั่วไปที่ไม่จำเป็นต้องเข้าถึงข้อมูลของ Class
# Class methods = เหมาะสำหรับการทำงานกับข้อมูลระดับ Class หรือการทำงานที่จำเป็นต้องเข้าถึงตัว Class โดยตรง

from student import Student

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.5)
student3 = Student("Squidward", 3.8)

print(Student.get_count())
print(Student.get_average_gpa())

"""
# Instance Method
def method(self):
    # self = Object


# Class Method
@classmethod
def method(cls):
    # cls = Class


# Static Method
@staticmethod
def method():
    # ไม่ใช้ self หรือ cls
"""