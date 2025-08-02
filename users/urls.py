from django.urls import path
from .views import home, about, register_portal, profile, ticket, register_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register-portal/', register_portal, name='register_portal'),
    path('profile/', profile, name='profile'),
    path('ticket/', ticket, name='ticket'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
