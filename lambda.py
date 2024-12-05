'''lambda ใน Python คือการสร้างฟังก์ชันแบบย่อที่ไม่มีชื่อ (anonymous function) ซึ่งสามารถเขียนในบรรทัดเดียว ใช้สำหรับงานที่ต้องการฟังก์ชันเล็ก ๆ แบบง่าย ๆ โดยไม่ต้องประกาศด้วยคำสั่ง def

รูปแบบทั่วไปของ lambda:
python
คัดลอกโค้ด
lambda arguments: expression
arguments: คือพารามิเตอร์ของฟังก์ชัน (เหมือนในฟังก์ชันปกติ)
expression: คือค่าที่จะถูกคำนวณและคืนค่า (ต้องเป็น statement เดียว)
ตัวอย่างพื้นฐานของ lambda:
python
คัดลอกโค้ด'''
# Lambda function ที่รับตัวเลขสองตัวและคืนค่าผลรวม
add = lambda x, y: x + y

print(add(5, 3))  # Output: 8
เทียบเท่ากับการเขียนฟังก์ชันปกติ:python
def add(x, y):
    return x + y

print(add(5, 3))  # Output: 8
# ตัวอย่างการใช้งาน lambda: ใช้กับฟังก์ชันในตัว (built-in functions) เช่น map, filter, sorted, และ reduce:

python# ใช้ lambda กับ map เพื่อเพิ่มตัวเลขในลิสต์
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# ใช้ lambda กับ filter เพื่อกรองตัวเลขที่มากกว่า 2
filtered = list(filter(lambda x: x > 2, numbers))
print(filtered)  # Output: [3, 4]

# ใช้ lambda กับ sorted เพื่อเรียงข้อมูลตามความยาวของ string
strings = ["apple", "kiwi", "banana"]
sorted_strings = sorted(strings, key=lambda x: len(x))
print(sorted_strings)  # Output: ['kiwi', 'apple', 'banana']
#สร้างฟังก์ชันง่าย ๆ ในบรรทัดเดียว:python
# ฟังก์ชันคำนวณค่า 2x + 1
func = lambda x: 2*x + 1
print(func(3))  # Output: 7
ใช้งานร่วมกับ dictionary:

python
# เลือกฟังก์ชันตาม key ใน dictionary
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "undefined"
}

print(operations["add"](5, 3))        # Output: 8
print(operations["multiply"](4, 2))  # Output: 8
ข้อควรระวัง:
Lambda ไม่สามารถมีหลาย statement:

python
คัดลอกโค้ด
# จะเกิดข้อผิดพลาด เพราะ lambda จำกัดที่ expression เดียว
lambda x: (x + 1, x - 1)# Error
อ่านยากกว่า def: ถ้าโค้ดยุ่งยากหรือมีความซับซ้อน ควรใช้ฟังก์ชันปกติ (def) เพื่อให้โค้ดอ่านง่ายและดูแลรักษาง่ายขึ้น

สรุป:ใช้ lambda สำหรับงานเล็ก ๆ ที่ต้องการฟังก์ชันแบบง่าย
ถ้างานซับซ้อนหรือใช้หลาย statement ให้ใช้ def แทน
ตัวอย่างที่เหมาะสมสำหรับ lambda เช่นใน map, filter, และ sorted