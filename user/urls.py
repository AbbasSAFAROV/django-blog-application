from django.urls import path
from .views import register , loginUser , logoutUser

urlpatterns = [
    path('register/', register , name = "register"),
    path('loginUser/', loginUser ,name = "loginUser"),
    path('logoutUser/', logoutUser , name = "logoutUser"),
]