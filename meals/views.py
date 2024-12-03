from django.shortcuts import render
from .models import Meal


def meals_management(request):
    meal_name = request.POST.get('meal_name')
    ingredients = request.POST.get('ingredients')
    price = request.POST.get('price')
    sort = request.POST.get('sort')
    cuisine = request.POST.get('cuisine')

    if meal_name and ingredients and price and sort and cuisine:
        Meal.objects.create(
            meal_name=meal_name,
            ingredients=ingredients,
            price=price,
            sort=sort,
            cuisine=cuisine
        )
        meals = Meal.objects.all()
        ctx = {'meals': meals}
        return render(request, 'meals_management.html', ctx)
    else:
        return render(request, 'meals_management.html')

def main_page(request):
    return render(request, 'main_page.html')
