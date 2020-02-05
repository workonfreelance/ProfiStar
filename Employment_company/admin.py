from django.contrib import admin
from .models import Job,Tag,Profile,ShoppingBasket

# @admin.register(Job)
# class PostAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Tag)
admin.site.register(Job)
admin.site.register(Profile)
admin.site.register(ShoppingBasket)
# # admin.site.register(Cities)