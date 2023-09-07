from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index_view(request):
   context = {
      "banner": Banner.objects.last(),
      "car_expert": Car_expert.objects.all(),
      "servis": Servis.objects.all(),
      "about_us": About_us.objects.all(),
      "gallery":  Gallery.objects.all(),
      "amazing_team": Amazing_team.objects.all(),
      "employee": Employee.objects.all(),
      "contact": Contact.objects.all()
   }
   return render(request, 'index.html', context)


def create_contact_view(request):
   if request.method == "POST":
      name = request.POST['name']
      email = request.POST['email']
      message = request.POST['message']
      Contact.objects.create(
         name=name,
         email=email,
         message=message,
      )
      return redirect('index_url')
   context = {
      "banner": Banner.objects.last(),
      "car_expert": Car_expert.objects.all(),
      "servis": Servis.objects.all(),
      "about_us": About_us.objects.all(),
      "gallery": Gallery.objects.all(),
      "amazing_team": Amazing_team.objects.all(),
      "employee": Employee.objects.all(),
      "contact": Contact.objects.all()
   }
   return render(request, 'index.html',context)