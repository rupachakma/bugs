from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from App.models import Items

# Create your views here.
def home(request):
    products=Items.objects.all()
    return render(request,"home.html",{'products':products})



def signuppage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password2")
        if pass1 == pass2:
            myuser = User.objects.create_user(name,email,pass1)
            myuser.save()
            return redirect("loginpage")
        else:
            return redirect("signuppage")
    return render(request,"signup.html")

def loginpage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        user = authenticate(user_name=name,password=password)
        if user is not None:
            return redirect("loginpage")
        else:
            return redirect("homepage")
        

    return render(request,"login.html")

def addpage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        description=request.POST.get("desc")
        quantity=request.POST.get("quantity")
        price=request.POST.get("price")

        products=Items(
            name=name,
            description=description,
            quantity=quantity,
            price=price
            )
        products.save()
        print(products)
        return redirect("homepage")
    return render(request,"home.html")

def updatepage(request,id):
    if request.method == "POST":
        name=request.POST.get("name")
        description=request.POST.get("desc")
        quantity=request.POST.get("quantity")
        price=request.POST.get("price")

        products=Items(
            id=id,
            name=name,
            description=description,
            quantity=quantity,
            price=price
            )
        products.save()
        print(products)
        return redirect("homepage")
    return render(request,"home.html")

def deletepage(request,id):
    products=Items.objects.get(id==id)
    products.delete()
    return redirect("homepage")