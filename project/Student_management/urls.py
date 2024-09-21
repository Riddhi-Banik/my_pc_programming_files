from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.Student_form_fill, name='formURL'),
    path('view/', views.Viewing, name='viewURL'),
    
]
