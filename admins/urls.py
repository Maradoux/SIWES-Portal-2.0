from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('applicants/', views.applicants, name='admin_applicants'),
]
