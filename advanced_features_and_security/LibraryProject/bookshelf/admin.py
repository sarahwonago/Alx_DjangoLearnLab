from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (_("Additional Info"), {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Additional Info"), {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_staff",
    )
    search_fields = ("username", "email", "first_name", "last_name")


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns to display
    list_filter = ("author", "publication_year")  # filter sidebar
    search_fields = ("title", "author")  # search bar
