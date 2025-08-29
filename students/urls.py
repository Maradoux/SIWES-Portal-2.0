from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='student_register'),
    path('status/', views.status, name='student_status'),
]
