# variable scope = ขอบเขตที่ตัวแปรสามารถมองเห็นและเข้าถึงได้
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
#                    Local    = ภายในฟังก์ชัน
#                    Enclosed = ฟังก์ชันด้านนอกของฟังก์ชันซ้อน
#                    Global   = ระดับโปรแกรม
#                    Built-in = ตัวแปร/ฟังก์ชันที่มีมาให้ใน Python

def func1():
    x = 1

    def func2():
        print(x) 
    func2()

func1() # 1
