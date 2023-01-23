from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import User
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_superuser', 'is_staff')
    inlines = (BasketAdmin,)
    list_editable = ('is_superuser', 'is_staff')
    fields = ('username', 'get_html_image', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', ('last_login',
                                                                                                             'date_joined'))
    readonly_fields = ('username', 'last_login', 'date_joined', 'get_html_image')
    ordering = ('id',)
    list_filter = ('is_superuser', 'is_staff',)

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=150>")
        else:
            return "Нет фото"

    get_html_image.short_description = "Аватар"
