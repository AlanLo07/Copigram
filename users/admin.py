from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk','user','phone_number')
    list_editable=("website","picture")
    search_fields=(
        'user__email',
        'user_username',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )
    list_filter=(
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    fieldsets = (
        ('Profile',{
            'fields': (
                'phone_number',
                'picture'
            ),
        }),
        ('Extra info',{
            'fields': (
                'website',
                'bio'
            )
        }),
        ('Metadata',{
            'fields': (
                'created',
                'modified',
                'pk',
            )
        }),
    )
    readonly_fields = (
        'created',
        'modified',
        'pk',
    )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)