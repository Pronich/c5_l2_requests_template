from django.shortcuts import render
from pprint import pprint

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def calc_recipes_view(request, dish_name):
    cnt_dish = int(request.GET.get('servings', 1))
    if cnt_dish > 1:
        elements = {}
        for key, value in DATA[dish_name].items():
            elements[key] = value * cnt_dish
    else:
        elements = DATA[dish_name]
    context = {'recipe': elements}
    pprint(context)
    # context = elements
    return render(request, 'calculator/index.html', context)



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
