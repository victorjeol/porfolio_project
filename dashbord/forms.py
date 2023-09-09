from django import forms
from porfolio.models import  Project, Pop, Project2, Painting,  Wallpaper, Reflector, Contact


class  ContactForm(forms.ModelForm):
    class Meta:
        model =  Contact
        fields = ['name', 'email', 'message', 'phone']


class  ProjectForm(forms.ModelForm):
    class Meta:
        model =  Project
        fields = ['image']

class  Project2Form(forms.ModelForm):
    class Meta:
        model =  Project2
        fields = ['image']


class  ReflectorForm(forms.ModelForm):
    class Meta:
        model = Reflector
        fields = ['image']

class  PaintingForm(forms.ModelForm):
    class Meta:
        model =  Painting
        fields = ['image']

class  WallpaperForm(forms.ModelForm):
    class Meta:
        model =  Wallpaper
        fields = ['image']
class  PopForm(forms.ModelForm):
    class Meta:
        model = Pop
        fields = ['image']