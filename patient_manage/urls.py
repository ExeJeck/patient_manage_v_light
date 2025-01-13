from django.urls import path

from . import views

app_name = 'patient_manage'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('patients/', views.PatientsListView.as_view(), name='patients_page'),
    path('about/', views.about_page, name='about_page'),
    path('contacts/', views.contacts_page, name='contacts_page'),
    path('add_patient/', views.patient_create, name='patient_create'),
    path('patient/<int:pk>/update/', views.patient_update, name='patient_update'),
    path('delete/', views.record_delete, name='record_delete'),
    path("test_time/", views.test_time, name='test_time'),
]