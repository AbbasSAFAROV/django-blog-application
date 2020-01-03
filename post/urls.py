from django.urls import path
from .views import addarticle,detail,update,delete , dashboard ,articles , myarticles

urlpatterns = [
    path('addarticle/', addarticle , name = "addarticle"),
    path('detail/<int:id>', detail ,name = "detail"),
    path('update/<int:id>', update , name = "update"),
    path('delete/<int:id>', delete ,name = "delete"),
    path('dashboard/', dashboard ,name = "dashboard"),
    path('articles', articles ,name = "articles"),
    path('myarticles/', myarticles ,name = "myarticles"),
    
]