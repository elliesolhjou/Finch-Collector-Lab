from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Finch

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch
    })

class CreateFinch(CreateView):
    model=Finch
    fields='__all__'

class UpdateFinch(UpdateView):
    model = Finch
    fields = '__all__'


class DeleteFinch(DeleteView):
    model= Finch
    success_url = '/finches'