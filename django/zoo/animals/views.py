from django.shortcuts import render
from animals.models import Animal

# Create your views here.
def index_view(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', context={'animals':animals})
