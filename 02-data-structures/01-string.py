name = "tle natt"
phone = "1-234-567-89"

len(name) # 8
name.find(" ") # 3
name.rfind("t") # 7
name = name.capitalize() # Tle natt
name = name.upper() # TLE NATT
name = name.lower() # tle natt
name.isdigit() # False
name.isalpha()
result = phone.count("-") # 3
phone = phone.replace("-", " ") # 1 234 567 89

print(result)

print(help(str)) # ให้ python แสดงคำอธิบาย

# indexing = การเข้าถึงสมาชิกของลำดับข้อมูลโดยใช้ [] (indexing operator)
#            [start : end : step]
#            start = ตำแหน่งเริ่มต้น
#            end   = ตำแหน่งสิ้นสุด (ไม่รวมตำแหน่งนี้)
#            step  = จำนวนตำแหน่งที่ข้ามในแต่ละครั้ง

credit_number = "1234-5678-9012-3456"

credit_number[0] # 1
credit_number[0:4] # 1234
credit_number[:4] # 1234
credit_number[5:9] # 5678
credit_number[5:] # 5678-9012-3456
credit_number[-1] # 6
credit_number[::2] # 13-6891-46
credit_number[-4:] # 3456
credit_number[::-1] # 6543-2109-8765-4321