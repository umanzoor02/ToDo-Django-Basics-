from django.urls import path
from . import views 

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('marks_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done' ),
    path('marks_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone' ),
    path('edit/<int:pk>/', views.edit, name='edit'), 
    path('delete/<int:pk>/', views.delete, name='delete'), 
]