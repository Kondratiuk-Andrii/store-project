from django.contrib import admin
from django.utils.safestring import mark_safe

from products.admin import BasketAdmin
from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_superuser', 'is_staff', 'is_verified_email')
    inlines = (BasketAdmin,)
    list_editable = ('is_superuser', 'is_staff')
    fields = (
        'username', 'get_html_image', 'first_name', 'last_name',
        'email', 'is_superuser', 'is_staff', 'is_verified_email', ('last_login',
                                                                   'date_joined'))
    readonly_fields = ('username', 'last_login', 'date_joined', 'get_html_image', 'is_verified_email')
    ordering = ('id',)
    list_filter = ('is_superuser', 'is_staff',)

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=150>")
        else:
            return "Нет фото"

    get_html_image.short_description = "Аватар"


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
