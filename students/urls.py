from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/search/', views.search_students, name='search'),
    path('api/students/', views.student_api, name='student_api'),
    path('', views.dashboard, name='home'),
]