from django.contrib import admin

# Register your models here.
from .models import Menu,achievement,Choice

admin.site.register(achievement)
admin.site.register(Choice)
admin.site.register(Menu)
