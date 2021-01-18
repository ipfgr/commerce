from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add", views.add, name="add"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("product", views.product, name="product"),
    path("product/<str:id>", views.product, name="product")
]
