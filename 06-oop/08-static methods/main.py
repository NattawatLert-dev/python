# static methods = Method ที่เป็นของ Class โดยตรง ไม่ได้เป็นของ Object ใด Object หนึ่ง
#                  มักใช้สำหรับฟังก์ชันทั่วไปที่ใช้เป็น utility

# Instance methods = เหมาะสำหรับการทำงานกับข้อมูลของ Object (Instance) ของ Class
# Static methods = เหมาะสำหรับฟังก์ชันทั่วไปที่ไม่จำเป็นต้องเข้าถึงข้อมูลของ Class

from employee import Employee

employee = Employee("Eugune", "Manager")

print(Employee.is_valid_position("Cook"))
print(employee.get_into())