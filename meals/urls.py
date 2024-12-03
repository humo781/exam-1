from django.urls import path
from .views import meals_management, main_page


app_name = 'meals'
urlpatterns = [
    path('', main_page),
    path('meal/', meals_management, name='meal')
]