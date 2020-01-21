from django.contrib import admin
from .models import Form

# @admin.register(Job)
# class PostAdmin(admin.ModelAdmin):
#     list_display = (['titel'])
    # list_filter = (['tags'])

admin.site.register(Form)
# admin.site.register(Job)
# admin.site.register(Cities)