from django.contrib import admin

# Register your models here.
from news.models import Category, New


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
class NewAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']
    list_filter = ['status','category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(New,NewAdmin)