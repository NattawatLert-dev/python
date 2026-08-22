# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA")) # Washington D.C
print(capitals.update({"Germany": "Berlin"})) # เพิ่ม key:value
print(capitals.pop("China")) # ลบค่า
capitals.popitem()
capitals.clear()
capitals.keys()
capitals.values()
capitals.items()