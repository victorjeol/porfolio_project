from django.forms import forms
from django.shortcuts import redirect, render
from django.contrib import messages


from django.contrib.auth.models import User, auth


# Create your views here.



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if not username:
               messages.error(request,"pls fill in the details")
               return render(request, 'user/register.html')
            
        if password1==password2:
            messages.error(request,"password not matching")
            if User.objects.filter(username=username).exists():
                messages.error(request,"username taken")
            # elif User.objects.filter(email=email).exists():
            #     # messages.warning(request,"email taken")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1 )
                user.save();
                messages.success(request,"user created")
                
        else:
             messages.error(request,"password not matching")
             return render(request, 'user/register.html')
        return redirect('login')
      
   
    return render(request, 'user/register.html')


# def login(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect("dashbord")
#         else:
#             messages.error(request,"invalid credentials")
#     return render(request, 'user/login.html')



def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashbord')
        else:
            messages.error(request,"invalid credentials")
    return render(request, 'user/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')
    