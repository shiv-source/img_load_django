from django.shortcuts import render,redirect
from .models import UserProfile
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        user = UserProfile(name=name)
        user.save()
        return redirect('/')
    else:
        data = UserProfile.objects.all()
        return render(request ,'index.html' , {'data':data})