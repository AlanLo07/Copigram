from django.contrib import admin
from posts.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'user',
        'title',
        'photo',
    )
    list_display_links=('pk','user',)
    list_editable=("title",)
    list_filter=(
        'created',
        'modified',
    )
    fieldsets = (
        ('Info',{
            'fields': (
                'title',
                'user',
                'profile',
                'photo'
            ),
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

# Register your models here.
