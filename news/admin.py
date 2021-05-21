from django.contrib import admin

# Register your models here.
from news.models import Category, New, Images


class NewImageInline(admin.TabularInline):
    model = Images
    extra = 5
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','status']
    list_filter = ['status']
    radeonly_fields=('image_tag',)

class NewAdmin(admin.ModelAdmin):
    list_display = ['title','category','image_tag','status']
    list_filter = ['status','category']
    inlines = [NewImageInline]
    readonly_fields = ('image_tag',)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','news','image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Images,ImagesAdmin)