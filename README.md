# Food Django Project

โปรเจค Django สำหรับการจัดการข้อมูลอาหาร

## การติดตั้ง

1. Clone repository:
```bash
git clone <your-repository-url>
cd one
```

2. สร้าง virtual environment:
```bash
python -m venv venv
```

3. เปิดใช้งาน virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

5. รัน migrations:
```bash
python manage.py migrate
```

6. สร้าง superuser (ถ้าต้องการ):
```bash
python manage.py createsuperuser
```

7. รันเซิร์ฟเวอร์:
```bash
python manage.py runserver
```

## การ Deploy ไปยัง PythonAnywhere

1. อัปโหลดโค้ดไปยัง PythonAnywhere
2. สร้าง virtual environment ใน PythonAnywhere
3. ติดตั้ง requirements
4. ตั้งค่า WSGI application
5. ตั้งค่า static files

## โครงสร้างโปรเจค

- `food/` - Django app หลัก
- `one/` - โฟลเดอร์ settings และ configuration
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)

## Features

- จัดการข้อมูลอาหาร
- ระบบ admin
- Templates สำหรับแสดงผล
