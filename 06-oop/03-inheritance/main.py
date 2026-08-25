# Inheritance = การสืบทอด ทำให้ class หนึ่งสามารถสืบทอด attributes และ methods จากอีก class ได้
#               ช่วยให้สามารถนำโค้ดกลับมาใช้ซ้ำและขยายความสามารถของ class ได้
#               class Child(Parent)

from dog import Dog

dog1 = Dog("Scooby")

print(dog1.name)
dog1.speak()
dog1.eat()
dog1.sleep()

# py 06-oop/03-inheritance/main.py