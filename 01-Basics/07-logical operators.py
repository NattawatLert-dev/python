# logical operator = ใช้ประเมินหลายเงื่อนไข (or, and, not)
#                    or  = อย่างน้อยหนึ่งเงื่อนไขต้องเป็น True
#                    and = ทั้งสองเงื่อนไขต้องเป็น True
#                    not = กลับค่าของเงื่อนไข (not False, not True)

temp = 25
is_raining = False

# EX.1
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# EX.2
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")