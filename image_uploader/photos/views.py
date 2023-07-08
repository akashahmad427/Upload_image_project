from django.shortcuts import render
from .models import Images
from .forms import Newform
# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Newform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    
    form = Newform()
    img = Images.objects.all()
    return render(request,'photos/home.html',{'image':img,'form':form})

