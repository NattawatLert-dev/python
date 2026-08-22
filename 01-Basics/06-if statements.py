# if = ทำโค้ดบางส่วนเฉพาะเมื่อเงื่อนไขเป็น True
#      หากไม่เป็นจริง ให้ทำอย่างอื่นแทน

#EX.1
age = int(input())

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")
