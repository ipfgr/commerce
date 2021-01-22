from django.contrib import admin
from .models import User
from .models import Product
from .models import Comment
from .models import Category
from .models import Bid
from .models import WatchListForUser

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(WatchListForUser)