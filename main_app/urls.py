from django.urls import path
from .views import MainPageView, HomePageView, AboutPageView, ContactPageView, ServicesPageView, login_user, logout_user, register_user, contact, contact_success

app_name = 'main_app'

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    #path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('contact/', contact, name='contact'),
    path('contact_success/', contact_success, name='contact_success'),
]
