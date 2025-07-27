from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone", "role")
    list_filter = ("id", "first_name", "last_name", "role")
    search_fields = ("id", "first_name", "last_name", "email")
