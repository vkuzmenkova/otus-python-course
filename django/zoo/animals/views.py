from django.shortcuts import render
from win32timezone import now

from animals.models import Animal, Food

# Create your views here.
from animals.tasks import send_email
from celery import current_app


def index_view(request):
    animals = Animal.objects.all()

    if request.method == 'POST':
        print(now())
        task = current_app.send_email.delay("hi", "text")
        task_id = task.id
        print(now())

    return render(request, 'animals/index.html',
                  context={'animals': animals, 'task_id': task_id})


def food_view(request):
    foods = Food.objects.prefetch_related('kinds').all()
    return render(request, 'animals/foods.html', context={'foods': foods})
