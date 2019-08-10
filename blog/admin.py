from django.contrib import admin
from .models import Blog
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

class Customized_Admin(ImportExportModelAdmin):
    list_display=('id','title','pub_date')
    search_fields=('title','body')
    list_filter=('title','pub_date')
    list_display_links=('id','title')

# Register your models here.

admin.site.register(Blog,Customized_Admin)
admin.site.unregister(Group)