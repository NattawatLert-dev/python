
# super() = ฟังก์ชันที่ใช้ใน Child class เพื่อเรียกใช้ methods จาก Parent class (superclass)
#           ช่วยให้สามารถเพิ่มหรือขยายความสามารถของ methods ที่สืบทอดมาได้

from circle import Circle
from square import Square
from triangle import Triangle

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

circle.describe()
print()
square.describe()