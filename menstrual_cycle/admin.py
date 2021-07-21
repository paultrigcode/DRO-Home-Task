from django.contrib import admin
from .models import CycleSetting
# Register your models here.
from django.contrib.auth.models import User

class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id','username',] # new
admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
admin.site.register(CycleSetting)
