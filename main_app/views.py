import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Pot, Photo
from .forms import WateredForm, StatusForm

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
    id_list = plant.pots.all().values_list('id')
    pots_plant_doesnt_have = Pot.objects.exclude(id__in=id_list)
    watered_form = WateredForm()
    status_form = StatusForm()
    return render(request, 'plants/detail.html', {
      'plant': plant, 'watered_form': watered_form,
      'plant': plant, 'status_form': status_form,
      'pots': pots_plant_doesnt_have
    })
      

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    #success_url = '/plants'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['species', 'description']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'

def add_watered(request, plant_id):
  form = WateredForm(request.POST)
  if form.is_valid():
    new_watered = form.save(commit=False)
    new_watered.plant_id = plant_id
    new_watered.save()
  return redirect('detail', plant_id=plant_id) 

def add_status(request, plant_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.plant_id = plant_id
        new_status.save()
    return redirect('detail', plant_id=plant_id)

class PotList(ListView):
    model = Pot

class PotDetail(DetailView):
    model = Pot

class PotCreate(CreateView):
    model = Pot
    fields = '__all__'

class PotUpdate(UpdateView):
    model = Pot
    fields = ['medium']

class PotDelete(DeleteView):
    model = Pot
    success_url = '/pots'

def assoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.add(pot_id)
    return redirect('detail', plant_id=plant_id)

def unassoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id=plant_id)

def add_photo(request, plant_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, plant_id=plant_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', plant_id=plant_id)