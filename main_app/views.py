from django.shortcuts import render
from .models import Plant

plants = [
    {'name': 'Monstera', 'species': 'Philodendron', 'description': 'Native to Southern Mexico, when given a chance to flower; produces a mild pineapple/strawberry flavored edible fruit.'},
    {'name': 'Jose Buono', 'species': 'Philodendron', 'description': 'Native to Colombia, this plants displays paddle-shaped leaves and have white variegation details.'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants
    })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {
         'plant': plant
    })