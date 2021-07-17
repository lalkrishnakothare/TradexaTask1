from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'text', 'created_at', 'updated_at',]

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)



