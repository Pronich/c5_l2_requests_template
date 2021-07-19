from django.urls import path
from calculator.views import calc_recipes_view

urlpatterns = [
    path('dish/<str:dish_name>/', calc_recipes_view)

    # здесь зарегистрируйте вашу view-функцию
]