from django.contrib import admin
from .models import Blog, Category, Series

# Register your models here.

admin.site.register(Category)
admin.site.register(Series)

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display    =   ['author','view']
    list_filter     =   ['author',]
    list_per_page   =   50
    readonly_fields =   ['edited','date_stamp','time_edited']
    exclude         =   ['like','dislike','slug']