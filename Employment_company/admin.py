from django.contrib import admin
from .models import Form,Job,Tag

# @admin.register(Job)
# class PostAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Tag)
admin.site.register(Job)
# # admin.site.register(Cities)