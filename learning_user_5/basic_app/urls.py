from django.urls import path
from basic_app import views

#TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns = [
    path('',views.index,name="index"),
    # path('basic_app/',views.index,name="basic_app"),
    path('register/',views.register,name='register'),
    # path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]