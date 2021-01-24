from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Product
from .models import User
from .models import Comment
from .models import Category
from .models import Bid
from .models import WatchListForUser
from datetime import datetime
from .forms import CommentsForm

commentform = CommentsForm()  # set user form for comments

# Index page fuction
def index(request):
    catlist = Category.objects.all()
    return render(
        request,
        "auctions/index.html",
        {"items": Product.objects.filter(active=True), "categories_list": catlist},
    )


# return page shows listings in choosen category
def category(request, ident):
    categ_id = Category.objects.filter(categories=str(ident))
    filtered_products = Product.objects.filter(category_id=categ_id[0])
    return render(
        request,
        "auctions/category.html",
        {"filtered_products": filtered_products, "category_name": ident},
    )


# show choosen product
def product(request, id):
    entry = Product.objects.get(title=id)
    close_button = 0
    current_bid = 0
    current_bid = (
        Bid.objects.filter(product_id=entry.auto_increment_id).order_by("id").last()
    )
    # Check if post autor is loggin , show button close
    if entry.author == request.user.username:
        close_button = 1
    else:
        close_button = 0

    if request.method == "GET":
        newcomment = request.GET.get("newcomment")
        currentuser = request.user.username

        cm = Comment.objects.filter(title_id=entry.auto_increment_id)

        if newcomment is not None:
            newc = Comment(title_id=entry.auto_increment_id, comment_text=newcomment)
            newc.save()

        # default product output
        context = {
            "id": entry.auto_increment_id,
            "title": entry.title,
            "descr": entry.description,
            "strbid": entry.startbid,
            "imgurl": entry.imgurl,
            "category": entry.category,
            "active": entry.active,
            "email": entry.email,
            "form": commentform,
            "comment_obj": cm[:5],
            "close_button": close_button,
        }
        return render(request, "auctions/product.html", context)

    # check for anny buttons pressed on product page
    if request.method == "POST":
        title = request.POST.get("title")
        updatebid = request.POST.get("updbid")
        pageid = request.POST.get("id")
        entry = Product.objects.get(title=title)
        close_value = request.POST.get("end")

        # Check if close listing button pressed
        if close_value == "close_bid":
            # write winner name to database
            max_bid_user = (
                Bid.objects.filter(product_id=entry.auto_increment_id)
                .order_by("id")
                .last()
            )
            # update listing entry
            Product.objects.filter(auto_increment_id=pageid).update(
                active=False, winner=max_bid_user.user
            )
            # return to index page
            return HttpResponseRedirect(reverse(index))

        # if owner dont close listing we check for new bids placed
        else:

            if current_bid.bid < int(updatebid):
                newbid = Bid(
                    user=request.user.username,
                    bid=updatebid,
                    product_id=entry.auto_increment_id,
                )
                newbid.save()
                # Context for return page with sucess "bid placed" message
                context = {
                    "id": entry.auto_increment_id,
                    "title": entry.title,
                    "descr": entry.description,
                    "strbid": entry.startbid,
                    "imgurl": entry.imgurl,
                    "category": entry.category,
                    "active": entry.active,
                    "email": entry.email,
                    "form": commentform,
                    "close_button": close_button,
                    "message": "Bid placed",
                    "current_bid": int(updatebid),
                }
                return render(request, "auctions/product.html", context)

            elif current_bid.bid >= int(updatebid):
                # Context for return page with error "bid lower then current" message
                context = {
                    "id": entry.auto_increment_id,
                    "title": entry.title,
                    "descr": entry.description,
                    "strbid": entry.startbid,
                    "imgurl": entry.imgurl,
                    "category": entry.category,
                    "active": entry.active,
                    "email": entry.email,
                    "form": commentform,
                    "close_button": close_button,
                    "error": "Bid is lower then current",
                    "current_bid": current_bid.bid,
                }
                return render(request, "auctions/product.html", context)


# Return  categories list
def categories(request):
    catlist = Category.objects.all()
    return render(request, "auctions/categories.html", {"categories": catlist})

# Return  categories list
def watchlist(request):
    current_user=request.user.username
    #if user puss button "Add to Watchlist" we come here
    if request.method == "POST":
        watchlist_item = request.POST.get("watchlist")
        watchlist=WatchListForUser(user=current_user, watchlist=watchlist_item)
        watchlist.save()
        return HttpResponseRedirect(reverse(index))
    
    if request.method == "GET":
        #get all items from user watchlist and renderto the page
        watchlist_items = WatchListForUser.objects.filter(user=current_user)
        items_w = []
        for i in watchlist_items:
            items_w.append(Product.objects.get(title=i.watchlist))
        return render(request, "auctions/watchlist.html", {
            "watchlist_items": items_w
        })
    

#Display page with autintificated user winnings items
def my_winnings(request):
    current_user= request.user.username
    winning_items = Product.objects.filter(active=False, winner=current_user)
    return render(request, 'auctions/winnings.html', {
            "winning_items":winning_items,
            "current_user":current_user
        } )

# Return page for add new listing
def add(request):
    catlist = Category.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        startbid = request.POST.get("startbid")
        url = request.POST.get("imgurl")
        ctg = Category.objects.get(categories=request.POST.get("category"))
        email = request.POST.get("email")
        author = request.POST.get("author")
        if Product.objects.filter(title=title).exists():
            return render(
                request, "auctions/add.html", {"name": title, "categories": catlist}
            )
        else:
            add = Product(
                title=title,
                description=description,
                startbid=startbid,
                imgurl=url,
                category_id=ctg.id,
                email=email,
                active=True,
                author=author,
            )
            add.save()

            just_saved_product = Product.objects.get(title=title)
            null_current_bid = Bid(
                product_id=just_saved_product.auto_increment_id, bid=0, user=author
            )
            null_current_bid.save()
            # return to index page
            return HttpResponseRedirect(reverse(index))

    return render(request, "auctions/add.html", {"categories": catlist})


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
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
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
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
