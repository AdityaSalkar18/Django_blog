from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from app.models import Profile
from app.models import Post
from app.models import Feedback
from datetime import datetime
from django.contrib import messages
import os


#Create your views here.
@login_required(login_url='login')
def myprofile(request):
    user=Profile.objects.get(user=request.user)
    context = {'user': user}
    return render(request,'myprofile.html',context)

    #return HttpResponse("this is about page")
    
def profile(request):
    if request.method == "POST":
        user= request.user
        profile=Profile.objects.get(user=user)
        
        pname =  request.POST.get('pname')
        pimage =  request.FILES.get('pimage')
        email =  request.POST.get('email')
        profession =  request.POST.get('profession')
        clgname =  request.POST.get('clgname')
        noblog =  request.POST.get('noblog')
        ilink = request.POST.get('ilink')
        flink = request.POST.get('flink')
        llink = request.POST.get('llink')
        aboutme = request.POST.get('aboutme')
        profile.pname=pname
        profile.pimage=pimage
        profile.email=email
        profile.profession=profession
        profile.clgname=clgname
        profile.noblog=noblog
        profile.ilink=ilink
        profile.flink=flink
        profile.llink=llink
        profile.aboutme=aboutme
        
        #profile = Profile( pname=pname , pimage=pimage, email=email, profession=profession, clgname=clgname, noblog=noblog)
        profile.save()
        return HttpResponseRedirect('/myprofile/')
   
    
    return render(request, 'profile.html')

def createblog(request):
    user=Profile.objects.get(user=request.user)
    context = {'user': user}
    
    if request.method == "POST":
        author = request.user
        category = request.POST.get('category')
        title = request.POST.get('title')
        stype = request.POST.get('stype')
        slink = request.POST.get('slink')
        
        bimage = request.FILES.get('bimage')
        content = request.POST.get('content')
        post = Post(author=author , category=category, title=title, stype=stype, slink=slink,  content=content, bimage=bimage,  timeStamp=datetime.today())
        post.save()
        
        return HttpResponseRedirect('/home/')
    
    return render(request, 'createblog.html',context)

def myblog(request):
    # posts = Post.objects.filter(author='author')
    
    allPosts = Post.objects.filter(author = request.user)
    
    context = {'allPosts':allPosts}
    
    return render(request, 'myblog.html',context)
    

def myfeedbacks(request):
    allFeedbacks = Feedback.objects.filter(toauthor = request.user)
    
    context = {'allFeedbacks':allFeedbacks}
    
    return render(request, 'myfeedbacks.html',context) 



def home(request):
    
    allPosts = Post.objects.all()
    
    context = {'allPosts':allPosts}
    
    return render(request, 'home.html',context)
    #return HttpResponse("this is home page")
    
    
def blog(request,slug):
    post = Post.objects.get(slug=slug)
    context = {'post' : post }
    
    
    return render(request, 'blog.html',context)

def editblog(request,slug):
    
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        if len(request.FILES) !=0:
           if len(post.bimage) >0:
               os.remove(post.bimage.path)
           post.bimage = request.FILES['bimage'] 
               
        post.author = request.user
        post.category = request.POST.get('category')
        post.title = request.POST.get('title')
        post.stype = request.POST.get('stype')
        post.slink = request.POST.get('slink')
        # post.bimage = request.FILES.get('bimage')
        post.content = request.POST.get('content')
        post.timeStamp = datetime.today()
        post.save()
        
        return redirect('/myblog/')
        
    
    return render(request, 'editblog.html',{'post':post})
       


def feedback(request,slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        toauthor = post.author
        fcategory = post.category
        ftitle = post.title
        sender = request.user
        fcontent = request.POST.get('fcontent')
        feedback = Feedback(toauthor=toauthor , fcategory=fcategory, ftitle=ftitle, fcontent=fcontent, sender=sender ,  timeStamp=datetime.today())
        feedback.save()
        messages.success(request,"Feedback Send Successfully")
        return render(request, 'feedback.html',{'post':post})
    return render(request, 'feedback.html',{'post':post})          

def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not Same")
        else:
            
          my_user=User.objects.create_user(uname,email,pass1)
          my_user.save()
          profile=Profile(user=my_user)
          profile.save()
          return redirect('login')
    
    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")
        
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

