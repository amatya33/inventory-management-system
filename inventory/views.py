from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Display devices in index.html

def display_device(request, cls):
    items = cls.objects.all()
    context = {
        'items' : items,
        'header' : cls.__name__,
    }

    return render(request, 'index.html', context) # 3 arguments

def display_laptops(request):
    return display_device(request, Laptop)

def display_desktops(request):
    return display_device(request, Desktop)

def display_mobiles(request):
    return display_device(request, Mobile)

# Add devices 

def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        
        if form.is_valid():
                form.save()
                return redirect('index')
 
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})

def add_laptop(request):
    return add_device(request, LaptopForm)

def add_desktop(request):
    return add_device(request, DesktopForm)

def add_mobile(request):
    return add_device(request, MobileForm)

# Edit Device
# takes primary key, model and cls as form, parameter

def edit_device(request,pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method = "POST":
        form = LaptopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = LaptopForm(instance=item)

        return render(request, 'edit_item.html', {'form':form})

