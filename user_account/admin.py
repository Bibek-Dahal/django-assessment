from django.contrib import admin
from .models import User,Role
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    list_display = ('id','email', 'first_name', 'last_name', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'roles','is_superuser', 'groups', 'user_permissions'),
        }),
        # (_('Important dates'), {'fields': ( 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone_number','password1', 'password2'),
        }),
    )
    ordering = ['phone_number']


admin.site.register(User, CustomUserAdmin)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["id"]