from django.urls import path
from .views import taxi_management


app_name = 'taxi'
urlpatterns = [
    path('taxi', taxi_management, name='taxi')
]
