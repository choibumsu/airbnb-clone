from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# same with @admin.register(models.User) decorator
# admin.site.register(models.User, CustomUserAdmin)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "currency", "language")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
