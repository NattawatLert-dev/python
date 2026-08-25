# *args     = สามารถส่ง argument แบบไม่ระบุชื่อได้หลายตัว
# **kwargs  = สามารถส่ง keyword argument ได้หลายตัว
#             * คือ unpacking operator ใช้สำหรับแยกค่าภายในข้อมูลออกมา
#             1. positional 2. default 3. keyword 4. ARBITRARY

# EX.1
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1)) # 1
print(add(1, 2)) # 3

# EX.2
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Tle", "Pear") # Tle Pear

# EX.3
def print_address(**kwargs):
    for value in kwargs.values():
  # for key in kwargs.key():
  # for key, value in kwargs.item():
        print(value)

print_address(street = "123 Fake St.",
              city = "Detroit",
              state = "MI",
              zip = "54321")

# EX.4
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

    # print(f"{kwargs.get('streer')} {kwargs.get('apt)}")
    # print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

    """
    if "apt" in kwargs:
        print(f"{kwargs.get('streer')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('streer')}")
    """
        
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street = "123 Fake St.",
               apt = "100",
               city = "Detroit",
               state = "MI",
               zip = "54321")