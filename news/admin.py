from django.contrib import admin

# Register your models here.
from news.models import Category, New, Images


class NewImageInline(admin.TabularInline):
    model = Images
    extra = 5
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
class NewAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']
    list_filter = ['status','category']
    inlines = [NewImageInline]
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','news','image']


admin.site.register(Category,CategoryAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Images,ImagesAdmin)