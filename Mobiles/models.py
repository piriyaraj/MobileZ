from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from django.db import models

# Create your models here.

class Network(models.Model):
    technology=models.CharField(max_length=100,null=True,blank=True)
    band2G=models.CharField(max_length=200,null=True,blank=True)
    band3G=models.CharField(max_length=200,null=True,blank=True)
    band4G=models.CharField(max_length=200,null=True,blank=True)
    band5G = models.CharField(max_length=200,null=True,blank=True)
    speed= models.CharField(max_length=100,null=True,blank=True)
    GPRS= models.CharField(max_length=100,null=True,blank=True)
    EDGE = models.CharField(max_length=100,null=True,blank=True)

class Lunch(models.Model):
    Announced = models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(max_length=100,null=True,blank=True)

class Body(models.Model):
    Dimensions = models.CharField(max_length=100,null=True,blank=True)
    Weight = models.CharField(max_length=100,null=True,blank=True)
    Build = models.CharField(max_length=100,null=True,blank=True)
    SIM = models.CharField(max_length=100,null=True,blank=True)

class Display(models.Model):
    Type = models.CharField(max_length=100,null=True,blank=True)
    Size = models.CharField(max_length=100,null=True,blank=True)
    Resolution = models.CharField(max_length=100,null=True,blank=True)
    Protection = models.CharField(max_length=100,null=True,blank=True)


class Platform(models.Model):
    OS = models.CharField(max_length=100,null=True,blank=True)
    Chipset = models.CharField(max_length=100,null=True,blank=True)
    CPU = models.CharField(max_length=100,null=True,blank=True)
    GPU = models.CharField(max_length=100,null=True,blank=True)

class Memory(models.Model):
    CardSlot = models.CharField(max_length=100,null=True,blank=True)
    Internal = models.CharField(max_length=100,null=True,blank=True)

class MainCamera(models.Model):
    Triple = models.CharField(max_length=100,null=True,blank=True)
    Features = models.CharField(max_length=100,null=True,blank=True)
    Video = models.CharField(max_length=100,null=True,blank=True)


class SelfieCamera(models.Model):
    Single = models.CharField(max_length=100,null=True,blank=True)
    Features = models.CharField(max_length=100,null=True,blank=True)
    Video = models.CharField(max_length=100,null=True,blank=True)

class Sound(models.Model):
    Loudspeaker = models.CharField(max_length=100,null=True,blank=True)
    Jack = models.CharField(max_length=100,null=True,blank=True)

class Comms(models.Model):
    Wlan=models.CharField(max_length=100,null=True,blank=True)
    Bluetooth=models.CharField(max_length=100,null=True,blank=True)
    Positioning=models.CharField(max_length=100,null=True,blank=True)
    NFC=models.CharField(max_length=100,null=True,blank=True)
    Radio=models.CharField(max_length=100,null=True,blank=True)
    USB=models.CharField(max_length=100,null=True,blank=True)

class Features(models.Model):
    Sensors=models.CharField(max_length=300,null=True,blank=True)
    
class Battery(models.Model):
    Type=models.CharField(max_length=100,null=True,blank=True)
    Charging=models.CharField(max_length=100,null=True,blank=True)

class Misc(models.Model):
    Colors=models.CharField(max_length=100,null=True,blank=True)
    Models=models.CharField(max_length=100,null=True,blank=True)
    Price=models.CharField(max_length=100,null=True,blank=True)

class PhoneImage(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    alt=models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to ='mobiles/')

class Brands(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to ='brands/',null=True,blank=True)

class mobilePost(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    network=models.ForeignKey(Network,on_delete=models.CASCADE,null=True,blank=True)
    lunch=models.ForeignKey(Lunch,on_delete=models.CASCADE,null=True,blank=True)
    body=models.ForeignKey(Body,on_delete=models.CASCADE,null=True,blank=True)
    display=models.ForeignKey(Display,on_delete=models.CASCADE,null=True,blank=True)
    platform=models.ForeignKey(Platform,on_delete=models.CASCADE,null=True,blank=True)
    memory=models.ForeignKey(Memory,on_delete=models.CASCADE,null=True,blank=True)
    maincamera=models.ForeignKey(MainCamera,on_delete=models.CASCADE,null=True,blank=True)
    selfiecamera=models.ForeignKey(SelfieCamera,on_delete=models.CASCADE,null=True,blank=True)
    sound=models.ForeignKey(Sound,on_delete=models.CASCADE,null=True,blank=True)
    comms=models.ForeignKey(Comms,on_delete=models.CASCADE,null=True,blank=True)
    features=models.ForeignKey(Features,on_delete=models.CASCADE,null=True,blank=True)
    battery=models.ForeignKey(Battery,on_delete=models.CASCADE,null=True,blank=True)    
    misc=models.ForeignKey(Misc,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ManyToManyField(PhoneImage,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

