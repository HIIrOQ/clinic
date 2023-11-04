from django.contrib import admin
from .models import Doctor

# Register your models here.


@admin.register(Doctor)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_num',
        'email',
        'exp',
        'speciality',
        'photo',
    ]
