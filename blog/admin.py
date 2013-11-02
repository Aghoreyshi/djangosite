from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django import forms

from blog.models import Entry, Category
from pagedown.widgets import AdminPagedownWidget

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    fieldsets = [
        (None, {'fields': ['title', 'slug']}),
    ]
    prepopulated_fields = {"slug": ("title",)}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        widgets = {
            'body' : AdminPagedownWidget(),
        }

class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    fieldsets = [
        (None, {'fields': ['title', 'body', 'categories', 'slug']}),
    ]
    list_display = ['title', 'pub_date', 'modified_date', 'published_recently']
    list_filter = ['pub_date']
    search_fields = ['title', 'body']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
