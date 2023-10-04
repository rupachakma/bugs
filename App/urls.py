from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage,name="signuppage"),
    path('loginpage/', views.loginpage,name="loginpage"),
    path('home/', views.home,name="homepage"),
    path('addpage/', views.addpage,name="addpage"),
    path('updatepage/<str:id>', views.updatepage,name="updatepage"),
    path('deletepage/<str:id>', views.deletepage,name="deletepage"),
    
]

