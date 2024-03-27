from django.contrib import admin
from .models import task

# Register your models here.

admin.site.register(task)

class taskAdmin(admin.ModelAdmin):
    list_display =  ('title', 'body')
    search_fields = ('title', 'body')
    list_filter = ('title', 'body')
    list_per_page = 25
    ordering = ('important', )
    