from django.contrib import admin
from .models import Job,Tag,Profile,UserComment

# @admin.register(Job)
# class PostAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Tag)
admin.site.register(Job)
admin.site.register(Profile)
admin.site.register(UserComment)
# # admin.site.register(Cities)