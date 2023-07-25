from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno =models.AutoField(primary_key=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    category = models.CharField(max_length=20)
    bimage = models.ImageField(upload_to="bimages/", default="")
    title = models.CharField(max_length=50)
    stype = models.CharField(max_length=20,null=True,blank=True)
    slink = models.CharField(max_length=50,null=True,blank=True)
    content = models.TextField()
    slug = AutoSlugField(populate_from='title',unique=True,null=True,blank=True)
    timeStamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return  self.title
    
    def geturl(self):
        return f'/posts/{self.slug}/'
    
    def feedback(self):
        return f'/feedback/{self.slug}/'
    
    def editblog(self):
        return f'/editblog/{self.slug}/'
    
    
    
   
    
    
    
    
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    sno =models.AutoField(primary_key=True)
    pname = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    profession = models.CharField(max_length=20,null=True,blank=True)
    clgname = models.CharField(max_length=50,null=True,blank=True)
    noblog = models.CharField(max_length=20,null=True,blank=True)
    pimage = models.ImageField(upload_to="pimages/",default="",null=True,blank=True)
    ilink = models.CharField(max_length=20,null=True,blank=True)
    flink = models.CharField(max_length=20,null=True,blank=True)
    llink = models.CharField(max_length=20,null=True,blank=True)
    aboutme = models.TextField(max_length=100,null=True,blank=True)
    
    
    
    def __str__(self):
        return  f'{self.pname}' 
    
    
    
    
class Feedback(models.Model):
    sno =models.AutoField(primary_key=True)
    toauthor = models.ForeignKey(User,on_delete=models.CASCADE)
    fcategory = models.CharField(max_length=20)
    ftitle = models.CharField(max_length=50)
    sender = models.CharField(max_length=20)
    fcontent = models.TextField()
    
    timeStamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return  self.ftitle
    
    