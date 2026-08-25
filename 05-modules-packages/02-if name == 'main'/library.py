# if __name__ == "__main__": = ใช้ตรวจสอบว่าไฟล์นี้กำลังถูกรันโดยตรงหรือถูก import
#                              ถ้ารันไฟล์นี้โดยตรง → โค้ดใน if จะทำงาน
#                              ถ้าไฟล์นี้ถูก import → โค้ดใน if จะไม่ทำงาน
#                              ทำให้สามารถนำ Functions และ Classes ใน module
#                              ไปใช้ซ้ำได้โดยไม่รันโค้ดหลักของไฟล์นั้น

# ex. library = นำเข้า library เพื่อใช้งานฟังก์ชันต่าง ๆ
#               เมื่อรัน library โดยตรง จะแสดงหน้าคำแนะนำการใช้งาน (help page)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Library Help")
    print("add(a, b)       = บวกเลข")
    print("substract(a, b) = ลบเลข")
