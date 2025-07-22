# วิธีการ Deploy ไปยัง PythonAnywhere

## ขั้นตอนที่ 1: Clone Repository

1. ไปที่ "Files" tab ใน PythonAnywhere
2. เปิด "Bash console"
3. รันคำสั่ง:
```bash
cd ~
git clone https://github.com/ITaAnuthida/fitfood.git
cd fitfood
```

## ขั้นตอนที่ 2: สร้าง Virtual Environment

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## ขั้นตอนที่ 3: ตั้งค่า Database

```bash
python manage.py migrate
python manage.py createsuperuser  # ถ้าต้องการ
```

## ขั้นตอนที่ 4: ตั้งค่า Web App

1. ไปที่ "Web" tab
2. คลิก "Add a new web app"
3. เลือก "Manual configuration"
4. เลือก Python 3.9
5. ในส่วน "Code":
   - Source code: `/home/ITaAnuthida/fitfood`
   - WSGI configuration file: `/var/www/ITaAnuthida_pythonanywhere_com_wsgi.py`

## ขั้นตอนที่ 5: แก้ไขไฟล์ WSGI

1. คลิกที่ WSGI configuration file link
2. ลบเนื้อหาทั้งหมดและแทนที่ด้วยเนื้อหาจากไฟล์ `pythonanywhere_wsgi.py`

## ขั้นตอนที่ 6: ตั้งค่า Static Files

1. ในส่วน "Static files" ของ Web tab:
   - URL: `/static/`
   - Directory: `/home/ITaAnuthida/fitfood/staticfiles/`

2. รันคำสั่งเพื่อ collect static files:
```bash
cd ~/fitfood
source venv/bin/activate
python manage.py collectstatic
```

## ขั้นตอนที่ 7: ตั้งค่า Virtual Environment

1. ในส่วน "Virtualenv" ของ Web tab:
   - Path: `/home/ITaAnuthida/fitfood/venv`

## ขั้นตอนที่ 8: Reload Web App

1. คลิกปุ่ม "Reload" สีเขียว
2. เยี่ยมชมเว็บไซต์ที่ `https://ITaAnuthida.pythonanywhere.com`

## หมายเหตุ:

- ถ้าต้องการใช้ production settings ให้แก้ไขไฟล์ WSGI:
  `os.environ['DJANGO_SETTINGS_MODULE'] = 'one.production_settings'`

- ตรวจสอบ error logs ได้ที่ "Error log" ใน Web tab

- ถ้ามีการเปลี่ยนแปลงโค้ดใหม่ ให้:
  1. `cd ~/fitfood`
  2. `git pull origin main`
  3. `source venv/bin/activate`
  4. `python manage.py migrate` (ถ้ามี migration ใหม่)
  5. `python manage.py collectstatic`
  6. Reload web app
