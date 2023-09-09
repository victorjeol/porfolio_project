from distutils.command.upload import upload
from email import message
from os import name
from turtle import title
from django.db import models
from django.core import validators
from django.core.validators import FileExtensionValidator
from django.db.models.fields.files import FileField


class Project(models.Model):
    image = models.ImageField(upload_to='image')

class Project2(models.Model):
    image = models.ImageField(upload_to='image')

class Painting(models.Model):
    image = models.ImageField()

class Reflector(models.Model):
    image = models.ImageField()

class Pop(models.Model):
    image = models.ImageField()
    
class Wallpaper(models.Model):
    image = models.ImageField()

    


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()

class Service(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    description = models.TextField()

class Video(models.Model):
    videoFile = models.FileField(upload_to='uploads/videoFiles', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])