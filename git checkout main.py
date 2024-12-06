'''
Assign ( = )
assign_copy ชี้ไปที่ออบเจกต์เดียวกับ original
ทุกการเปลี่ยนแปลงใน original จะส่งผลต่อ assign_copy

Shallow Copy (copy.copy())
shallow_copy คัดลอก value เป็นอิสระจาก original
แต่ items ซึ่งเป็น list ซ้อนกัน ยังคงอ้างอิงถึง list ของ original ดังนั้นการเปลี่ยนแปลงใน list ด้านใน ([99, 4]) ส่งผลต่อ shallow_copy

Deep Copy (copy.deepcopy())
deep_copy แยกออกอย่างสมบูรณ์ทั้ง value และ items
ไม่มีอะไรเชื่อมต่อกับ original อีก การเปลี่ยนแปลงใดๆ ใน original จะไม่กระทบกับ deep_copy'''


import copy

# สร้างคลาสที่มี attribute เป็น list
class MyClass:
    def __init__(self, value, items):
        self.value = value
        self.items = items

# สร้างออบเจกต์ต้นฉบับ
original = MyClass(10, [1, 2, [3, 4]])

# 1. Assign ( = )
assign_copy = original

# 2. Shallow copy
shallow_copy = copy.copy(original)

# 3. Deep copy
deep_copy = copy.deepcopy(original)

# ทำการเปลี่ยนแปลงบางอย่างใน attribute ที่เป็นโครงสร้างซ้อนกัน
original.items[2][0] = 99  # เปลี่ยนค่าด้านในของ list
original.value = 20        # เปลี่ยน value


# แสดงค่าใน original และสำเนาทั้งสาม
print("Original:", original.value, original.items)
print("Assign Copy:", assign_copy.value, assign_copy.items)
print("Shallow Copy:", shallow_copy.value, shallow_copy.items)
print("Deep Copy:", deep_copy.value, deep_copy.items)
