from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myapp.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.method=="POST":
        tittle=request.POST.get("tittle")
        author=request.POST.get("author")
        description=request.POST.get("description")
        date=request.POST.get("date")
        post=Post(tittle=tittle,author=author,description=description,date=date)
        post.save()
        
    return render(request,"home.html")

@login_required(login_url="loginpage")
def post(request):
    allpost=Post.objects.all()
    context={'allpost': allpost}
    return render(request,"post.html",context)

def loginp(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("create_account")
    
        else:
            print(request,"something wrong")
        
    return render(request,"loginp.html")
    

def create_account(request):
    if request.method=="POST":
        username=request.POST.get("username")
        gmail=request.POST.get("gmail")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password2")
        if pass1!=pass2:
            print("your password is wrong")
        else:
            user=User.objects.create_user(username,gmail,pass1)
            user.save()
            
    return render(request,"create_account.html")

    