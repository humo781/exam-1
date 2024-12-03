from django.shortcuts import render
from .models import Taxi


def taxi_management(request):
    taxi_name = request.POST.get('taxi_name')
    licence_plate = request.POST.get('licence_plate')
    driver_name = request.POST.get('driver_name')
    passenger_capacity = request.POST.get('passenger_capacity')
    car_model = request.POST.get('car_model')
    status = request.POST.get('status')

    if taxi_name and licence_plate and driver_name and passenger_capacity and car_model and status:
        Taxi.objects.create(
            taxi_name=taxi_name,
            licence_plate=licence_plate,
            driver_name=driver_name,
            passenger_capacity=passenger_capacity,
            car_model=car_model,
            status=status,
        )
        taxis = Taxi.objects.all()
        ctx = {'taxis': taxis}
        return render(request, 'taxi_management.html', ctx)
    else:
        return render(request, 'taxi_management.html')
