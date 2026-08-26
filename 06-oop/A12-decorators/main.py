# Decorator = ฟังก์ชันที่ใช้เพิ่มหรือขยายความสามารถของฟังก์ชันอื่น
#             โดยไม่ต้องแก้ไขฟังก์ชันเดิม
#             โดยส่งฟังก์ชันเดิมเข้าไปเป็น argument ของ decorator
#
#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flaver):
    print(f"Here is your {flaver} ice cream")

get_ice_cream("vanilla")