from django.shortcuts import render,redirect
from .models import UserProfile
# Create your views here.

def home(request):
        if request.method == 'POST' and request.FILES['img']:
            name = request.POST['name']
            img =request.FILES['img']
            video=request.FILES['video']
            user = UserProfile(name=name,img=img,video=video)
            user.save()
            return redirect('/')
        
        else:
            data = UserProfile.objects.all()
            return render(request ,'index.html' , {'data':data})