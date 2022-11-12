from django.contrib import admin

from Extract.models import brand, post

# Register your models here.


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('url', 'released', 'posted')
    search_fields = ('url', )


@admin.register(brand)
class  BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastpost', 'count', 'havenewpost')
    search_fields = ('name', )
    ordering = ('name',)
