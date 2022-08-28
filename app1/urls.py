from django.urls import path
from app1 import views

urlpatterns = [
    path('user/', views.userList.as_view()),
    path('user/<int:pk>/', views.userDetails.as_view()),
    path('incident/', views.incidentList.as_view()),
    path('incident/<int:pk>/', views.incidentDetails.as_view()),

]
