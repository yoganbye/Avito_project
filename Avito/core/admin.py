from django.contrib import admin
from .models import Profile, CategoriesAd, Ad, Comment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from datetime import timedelta
from django.utils import timezone


admin.site.unregister(User)

class ProfileInLine(admin.StackedInline):
    model = Profile
    

@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [ProfileInLine]


def delete_views_count(modeladmin, request, queryset):
    queryset.update(views_count = 0)


def delete_very_old_posts(modeladmin, request, queryset):
    queryset.filter(date_pub__lte=timezone.now() - timedelta(weeks=2)).delete()


class CommentInLine(admin.StackedInline):
    model = Comment
    fields = ['author', 'text', 'in_announce', 'date_publish']
    readonly_fields = ['date_publish']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information', {'fields': ['author']}),
        ('Categories', {'fields': ['categories']}),
        ('Ad content', {'fields': ['heading', 'description', 'image', 'price']}), 
        ('Other inforamtion', {'fields': ['date_pub', 'date_edit', 'views_count']}),     
    ]
    readonly_fields = ['date_pub', 'date_edit', 'views_count']
    list_display = ('author', 'heading', 'views_count', 'date_pub')
    list_filter = ('categories', 'date_pub')
    search_fields = ['author__username', 'description', 'heading']
    actions = [delete_views_count, delete_very_old_posts]
    inlines = [CommentInLine]


@admin.register(CategoriesAd)
class CategoriesAdAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Categories', {'fields': ['name']}),
    ]
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ['name',]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information', {'fields': ['author']}),
        ('Comment content', {'fields': ['text', 'in_announce']}), 
        ('Other inforamtion', {'fields': ['date_publish']}), 
    ]

    readonly_fields = ['date_publish']
    list_display = ('author', 'in_announce','date_publish')
    list_filter = ('author', 'in_announce','date_publish')
    search_fields = ['author__username', 'in_announce', 'text']