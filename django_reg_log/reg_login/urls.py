from django.urls import path
from . import views

urlpatterns = [
    path('regis/',views.registration,name='regis'),
    # path('registration/', views.registration, name='registration'),
    path('home/', views.home, name="home"),
    path('login/',views.login_view,name='login'),
]
