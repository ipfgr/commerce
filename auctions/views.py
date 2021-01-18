from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Product
from .models import User


def index(request):
    return render(request, "auctions/index.html",{
        "items":Product.objects.filter(active=True)
    })

def product(request,id):
    if request.method == "GET":
        entry = Product.objects.get(title=id)
        return render (request, "auctions/product.html", {
            "id":entry.auto_increment_id,
            "title":entry.title,
            "descr":entry.description,
            "strbid":entry.startbid,
            "imgurl":entry.imgurl,
            "category":entry.category,
            "active":entry.active,
            "email":entry.email,
            
        })
    if request.method == "POST":
        title= request.POST.get("title")
        updatebid = request.POST.get("updbid")
        pageid=request.POST.get("id")
        entry = Product.objects.get(title=title)
        if entry.startbid < int(updatebid):
            Product.objects.filter(auto_increment_id=pageid).update(startbid=updatebid)
            return render (request, "auctions/product.html", {
                "id":entry.auto_increment_id,
                "title":entry.title,
                "descr":entry.description,
                "strbid":entry.startbid,
                "imgurl":entry.imgurl,
                "category":entry.category,
                "active":entry.active,
                "email":entry.email,
                "message": "Bid placed"
            })
        elif(entry.startbid > int(updatebid)): 
            return render (request, "auctions/product.html", {
                "id":entry.auto_increment_id,
                "title":entry.title,
                "descr":entry.description,
                "strbid":entry.startbid,
                "imgurl":entry.imgurl,
                "category":entry.category,
                "active":entry.active,
                "email":entry.email,
                "error": "Bid is lower then current"
                
            })


def categories(request):
    pass

def watchlist(request):
    pass

def add(request):
    

    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        startbid=request.POST.get("startbid")
        url=request.POST.get("imgurl")
        category=request.POST.get("category")
        email=request.POST.get("email")

        if Product.objects.filter(title=title).exists():
            return render(request, "auctions/add.html", {
                "name": title
    })
        else:
            add=Product(title=title, description=description, startbid=startbid, imgurl=url, category=category,email=email, active = True)
            add.save()
            return index(request)
    
    return render(request, "auctions/add.html", {
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
