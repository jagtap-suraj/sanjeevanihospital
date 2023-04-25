from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('<int:pk>/edit/', views.edit_patient, name='patient_edit'),
    path('<int:pk>/delete/', views.delete_patient, name='patient_delete'),
    path('add/patient_form/', views.add_patient, name='patient_form'),
]
