import email
from email import message
from os import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template import context




from .models import Project, Contact, Service, Video, Painting, Pop, Reflector, Wallpaper, Project2

# Create your views here.

def index(request):
    projects = Project.objects.all()
    videos = Video.objects.all()
    
    context ={
        'projects': projects,
        'videos': videos

         
    }
    return render(request, 'porfolio/index.html', context)

def painting(request):
    paintings = Painting.objects.all()
   
    
    context ={
        'paintings': paintings
          
    }
    return render(request, 'porfolio/painting.html', context)

def reflector(request):
    reflectors = Reflector.objects.all()
    context ={
        'reflectors': reflectors
          
    }
    return render(request, 'porfolio/reflector.html', context)
def pop(request):
    pops = Pop.objects.all()
   
    
    context ={
      'pops': pops
          
    }
    return render(request, 'porfolio/pop.html', context)

def wallpaper(request): 
    wallpapers = Wallpaper.objects.all()
    context ={
        'wallpapers': wallpapers
          
    }
    return render(request, 'porfolio/wallpaper.html', context)

def project2(request):
    pros = Project2.objects.all()
   
    
    context ={
        'pros': pros,
          
    }
    return render(request, 'porfolio/project.html', context)

def about(request):
    
     return render(request, "porfolio/about.html")

def contact(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
          myname = request.POST['name']
          myemail = request.POST['email']
          myphone = request.POST['phone']
          mymessage = request.POST['message']
         
          if not myname:
            #    messages.error(request,"pls type your full name")
               return render(request, "porfolio/contact.html")
      
          # return redirect('index')
          ContactForm = Contact.objects.create(name=myname, email=myemail, message=mymessage, phone=myphone)
          messages.success(request, 'successfully created we will respond to u shortly')
          context = {
            'contacts': contact

          }

          return render(request, "porfolio/contact.html", context)
    else:
          return render(request, "porfolio/contact.html")



def service(request):
     services = Service.objects.all()
     context ={
          'services': services

     }
     return render(request, "porfolio/services.html", context)

