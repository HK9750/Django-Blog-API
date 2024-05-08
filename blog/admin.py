from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at']
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Category)
