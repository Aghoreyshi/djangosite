from django.contrib import admin
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


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'body', 'slug']}),
    ]
    #inlines = [CategoryInline]
    list_display = ['title', 'pub_date', 'modified_date', 'published_recently']
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Poll, PollAdmin)
admin.site.register(Entry, EntryAdmin)
