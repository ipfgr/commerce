from django.contrib import admin
from .models import User
from .models import Product
from .models import Comment
from .models import Bids

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Bids)
