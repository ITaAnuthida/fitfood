from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),      # หน้าแรก
    path('food/', views.food, name='food'),   # หน้าแสดงสูตรอาหาร
    path('profile/', views.profile, name='profile'),  # หน้าแสดงโปรไฟล์
    path('basetemplates/', views.basetemplates, name='basetemplates'),  # หน้าเทมเพลตพื้นฐาน
]