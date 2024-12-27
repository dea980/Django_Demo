from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'), ## Schedule
    path('create/', views.schedule_create, name='schedule_create'), ## Create Schedule
    path('edit/<int:pk>/', views.schedule_edit, name='schedule_edit'), ## edit Schedule
    path('delete/<int:pk>/', views.schedule_delete, name='schedule_delete'), ## Delete Schedule
    path('toggle-status/<int:pk>/', views.schedule_toggle_status, name='schedule_toggle_status'),## Toggle Status
]