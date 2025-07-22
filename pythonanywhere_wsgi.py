# ==================================================================================
# WSGI file for PythonAnywhere
# แก้ไขไฟล์นี้ใน PythonAnywhere Web tab
# ==================================================================================

import os
import sys

# เพิ่ม path ของโปรเจค
path = '/home/ITaAnuthida/fitfood'
if path not in sys.path:
    sys.path.append(path)

# ตั้งค่า Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'one.settings'

# สำหรับ production ให้ใช้ production_settings.py
# os.environ['DJANGO_SETTINGS_MODULE'] = 'one.production_settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
