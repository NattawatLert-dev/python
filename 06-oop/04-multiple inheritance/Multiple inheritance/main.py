# multiple inheritance = การสืบทอดจาก Parent class มากกว่าหนึ่ง class
#                        C(A, B)

# multilevel inheritance = การสืบทอดต่อกันหลายระดับ โดย Child สืบทอดจาก Parent
#                          ที่ Parent เองก็สืบทอดมาจากอีก Parent หนึ่ง
#                          C(B) <- B(A) <- A

from dog import Dog

dog1 = Dog("Shabu")

print(dog1.name)
dog1.play()
dog1.eat()