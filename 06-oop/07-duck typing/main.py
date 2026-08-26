# "Duck typing" = อีกวิธีหนึ่งในการทำ Polymorphism โดยไม่ต้องใช้ Inheritance
#                 Object ต้องมี attributes/methods ที่จำเป็นอย่างน้อย
#                 "ถ้ามันดูเหมือนเป็ด และร้องเหมือนเป็ด มันก็คือเป็ด"

from dog import Dog
from cat import Cat
from car import Car

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)