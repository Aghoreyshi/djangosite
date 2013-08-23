from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget

from polls.models import Choice, Poll
from blog.models import Entry, Category


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question', 'pub_date', 'published_recently']
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'


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


admin.site.register(Poll, PollAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
