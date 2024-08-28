from django.contrib import admin

from blog.models import Blogs


# Register your models here.
@admin.register(Blogs)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sign_of_publication',)