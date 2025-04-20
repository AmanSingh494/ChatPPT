from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import chat,getResponse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',chat,name='chat'),
path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login')
,
path('getResponse/', getResponse, name='getResponse'),
]
