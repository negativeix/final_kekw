'''# สร้าง branch ใหม่ชื่อ feature/add-file
git checkout -b feature/add-file

# สร้างไฟล์ example.txt และเพิ่มข้อความในไฟล์
echo "Hello Git" > example.txt

# เพิ่มไฟล์ทั้งหมดเข้าสู่ staging area
git add .

# Commit การเปลี่ยนแปลงพร้อมข้อความ
git commit -m "Add example.txt"

# Push branch และการเปลี่ยนแปลงไปยัง remote repository
git push origin feature/add-file
'''