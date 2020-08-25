from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete')
]