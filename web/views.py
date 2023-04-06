from django.shortcuts import render
from .models import InfoWorker


# Create your views here.

def index(request):
    workers = InfoWorker.objects.all()
    context = {"worker_list": workers}
    return render(request, 'index.html', context=context)


