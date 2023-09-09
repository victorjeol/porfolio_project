from django.forms import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from porfolio.models import  Painting, Contact, Project2, Wallpaper, Pop, Reflector, Video, Service, Project
from .forms import ProjectForm, PopForm, ReflectorForm, PaintingForm, WallpaperForm, Project2Form,  ContactForm


# Create your views here.
@login_required
def dashbord(request):
    return render(request, 'dashboard/dashbord.html')
@login_required
def all_service(request):
    return render(request, 'dashboard/all_service.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')



@login_required
def reflector(request):
    reflectors = Reflector.objects.all()
    if request.method == 'POST':
        form = ReflectorForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
    else:
        form = ReflectorForm()
    context ={
        'reflectors': reflectors,
        'form': form, 
          
    }
    return render(request, 'dashboard/reflector.html', context)

@login_required    
def reflector_delete(request, pk):
    reflectors = Reflector.objects.get(pk=pk)
    reflectors.delete()
    return redirect('reflect')

@login_required
def contact(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        form =  ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context ={
        'form': form,
        'contacts': contacts 
          
    }

    return render(request, 'dashboard/contact.html', context)

@login_required   
def contact_delete(request, pk):
    contacts = Contact.objects.get(pk=pk)
    contacts.delete()
    return redirect('cont')



@login_required
def pop(request):
    pops = Pop.objects.all()
    if request.method == 'POST':
         form = PopForm(request.POST,request.FILES)
         if form.is_valid():
                form.save()
    else:
        form = PopForm()
    context ={
      'pops': pops,
      'form': form, 
          
    }   
    return render(request, 'dashboard/pop.html', context)

@login_required
def pop_delete(request, pk):
    pops = Pop.objects.get(pk=pk)
    pops.delete()
    return redirect('pop')


@login_required
def painting(request):
    paintings = Painting.objects.all()
    if request.method == 'POST':
        form =  PaintingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PaintingForm()
    context ={
        'paintings': paintings,
        'form': form, 
          
    }
    return render(request, 'dashboard/painting.html', context)

@login_required    
def pain_delete(request, pk):
    paintings = Painting.objects.get(pk=pk)
    paintings.delete()
    return redirect('pat')

@login_required
def wallpaper(request):
    wallpapers = Wallpaper.objects.all()
    if request.method == 'POST':
        form = WallpaperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        
    else:
        form = WallpaperForm()
    context ={
        'wallpapers': wallpapers,
        'form': form, 
          
    }
    return render(request, 'dashboard/wallpaper.html', context)

@login_required    
def wallpaper_delete(request, pk):
    wallpapers = Wallpaper.objects.get(pk=pk)
    wallpapers.delete()
    return redirect('wall')

@login_required
def inde(request):
    
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProjectForm()

   
    context ={
        'projects': projects,
        'form': form,    
       
    }
    return render(request, 'dashboard/project.html', context)

@login_required
def inde_delete(request, pk):
    projects = Project.objects.get(pk=pk)
    projects.delete()
    return redirect('inde')


@login_required
def pro(request):
    pros = Project2.objects.all()
    if request.method == 'POST':
        form = Project2Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
       
    else:
        form = Project2Form()
    context ={
        'pros': pros, 
        'form': form,    
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def pro_delete(request, pk):
    pros = Project2.objects.get(pk=pk)
    pros.delete()
    return redirect('pro')

